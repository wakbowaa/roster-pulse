# Roster Pulse

### Dispatch note

Fair rotation begins after eligibility, not before it.

A coordinator freezes a member roster, one capability profile per member, a decline policy, and a response window. When a task arrives, GenLayer validators identify every profile that covers all frozen requirements. Roster Pulse then selects the eligible member with the lowest completed-duty count, using roster order only as a deterministic tie break.

### Pulse states

`IDLE -> ASSIGNED -> ACCEPTED -> COMPLETED`

`ASSIGNED -> valid decline or timeout -> ASSIGNED | UNFILLED`

The assignee alone may accept, decline, or complete. A decline is effective only when validator consensus finds that its reason satisfies the frozen policy. Anyone can expire an abandoned assignment after its deadline, so rotation cannot be held hostage.

### Division of authority

- Consensus returns the complete eligible index set and a coverage explanation for every member.
- Deterministic code chooses the least-used eligible member.
- Completion counts increase only on acceptance.
- Declined and timed-out members are excluded from the current task, not erased from the roster.

### Bench check

```bash
genvm-lint contracts/contract.py
python -m pytest -q
```

Roster Pulse is a standalone Intelligent Contract. It has no website, token, escrow, or hidden scheduler.
