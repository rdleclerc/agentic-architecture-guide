# Agent-to-agent message contracts

Version: 1.0
Audience: coding agents and architects working on multi-agent systems.

Cross-agent coordination covers ownership and integrator role. A2A contracts cover the messages themselves. The failure mode this prevents is folklore A2A: two agents work together because someone wrote a script that hardcoded what one produces and what the other expects. There is no schema, no version, no contract for partial messages, no idempotency rule, no replay rule, and no audit trail. The pair works until either side is edited.

---

## 1. Every A2A message type declares seven things

```text
1. Schema
   Typed shape of the message. Required fields, optional fields, types,
   units, allowed values. No payload field is "any."

2. Direction
   Request, reply, broadcast, signal, or event. Reply messages reference
   the request they answer. Broadcasts have no required reply.

3. Idempotency
   Is sending the same message twice safe? If yes, by what mechanism
   (idempotency key, content hash, dedup window). If no, what is the
   replay rule and what state in the receiver tracks "already handled."

4. Versioning
   How does the contract evolve? Field additions are usually safe; field
   removals or semantic changes require an explicit version bump and a
   migration plan. The receiver should know which versions it accepts.

5. Authority
   Which agent is authorized to send this message type. Which agent is
   authorized to act on it. Senders that do not have authority should be
   rejected at the receiver, not at the network.

6. Failure attribution
   How does the sender know the receiver failed? How does the receiver
   know the sender did not get the reply? Which class of failure (see
   docs/exception-taxonomy.md) does each side attribute to, and what
   does each side do next.

7. Audit
   Where is the message recorded? A2A traffic that does not appear in
   any audit surface is invisible to operators and to future agents
   debugging what happened.
```

---

## 2. Message schemas: minimum required structure

Every A2A message has at least these fields:

```python
@dataclass
class A2AMessage:
    # Identity
    message_id: str          # unique per send
    correlation_id: str      # ties request and reply
    causation_id: str | None # the message that caused this one

    # Routing
    from_agent: str
    to_agent: str
    type: str                # message type name (registry-keyed)
    version: str             # semver of the type's schema

    # Timing
    sent_at: datetime
    expires_at: datetime | None

    # Authority
    auth_token: str | None   # if cross-tenant or cross-trust-zone

    # Payload
    payload: dict            # typed per `type` and `version`
```

The payload type is keyed by the registered name and version. A receiver that does not recognize the type/version pair rejects the message; it does not "best-effort" decode it.

---

## 3. Idempotency patterns

### 3.1 Idempotency key

The sender supplies a key. The receiver records the key with the result. Repeated sends with the same key return the same result. This is the safest pattern when the receiver has durable state.

### 3.2 Content hash

The receiver hashes the payload and treats two messages with the same hash inside a dedup window as the same message. Useful when senders may re-send without remembering the previous send.

### 3.3 At-most-once via reservation

The receiver reserves a slot for the message_id, processes, and releases. A second send with the same message_id sees the reservation and returns the cached result.

### 3.4 At-least-once with idempotent handler

The handler itself is idempotent: the same input produces the same effect regardless of how many times it is invoked. Useful when the message bus cannot guarantee deduplication.

The handler's idempotency must be documented. "It happens to be idempotent because of how it's written today" is folklore.

---

## 4. Versioning

A2A contracts evolve. The rule is:

```text
safe (no version bump):
  - add an optional field
  - add a new enum value the receiver tolerates
  - add a new message type

unsafe (requires version bump and migration):
  - remove a field
  - rename a field
  - change a field's type or units
  - change a field's semantics
  - tighten a validation rule
```

The receiver advertises which versions it accepts. The sender chooses the highest mutually supported version. Migration plans cover both forward and backward compatibility windows.

---

## 5. Authority and trust

A2A authority answers "who is allowed to send this message type and who is allowed to act on it."

```text
- declared in a registry, not in agent prompts
- enforced at the receiver (network and bus may not be trustworthy)
- audited (every authority decision is logged)
- revocable (deprecation path for retired agents)
```

A receiver that processes messages without checking authority will be exploited the moment any agent in the system is compromised, mis-configured, or replaced by a sidecar with weaker invariants.

---

## 6. Failure attribution between agents

Both sides of an A2A pair need to know whose problem a failure is.

```text
sender's perspective                receiver's perspective
- request acknowledged but no reply  - received message but cannot act
   within timeout: receiver problem    on it: signal back unrecoverable
- request rejected at validation:    - received valid message but
   sender problem (bad payload)        downstream failed: signal back
- network error: bus problem,         (recoverable, degraded, or
   sender retries per recoverable      unrecoverable)
   class
```

Each failure attaches to one of the three exception classes (`docs/exception-taxonomy.md`) and triggers the corresponding behavior.

---

## 7. Audit surface

Every A2A message is recorded in at least one of:

```text
- structured event log (preferred for high volume)
- durable state record (preferred for state-changing messages)
- trace span (preferred for request/reply latency)
```

A2A traffic that does not appear in any audit surface is invisible. Invisible coordination is folklore by another name.

---

## 8. Common smells

```text
- payloads typed as `dict` or `any` with no schema
- "we'll add versioning when we need it"
- handlers that succeed differently on retry without saying so
- broadcasts with no recorded receivers
- replies that do not reference the request they answer
- authority decisions made in agent system prompts instead of a registry
```

---

## 9. Cross-references

- Architecture: section 5.17 (A2A message contracts), section 5.13 (Adoption states and cross-agent coordination)
- Anti-pattern: section 9.12 (Implicit A2A folklore)
- Field lesson: section 12.10 (Modularity is a runtime property), section 12.11 (Errors are classes, not surprises)
- Tool design (analogous contract for tool calls): `docs/tool-design.md`
- Cross-agent operating model: `docs/cross-agent-operating-model.md`
