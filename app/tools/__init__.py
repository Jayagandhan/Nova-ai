"""
Tool architecture foundation (see master spec sections 6-7).

Every external capability Nova can perform (YouTube search, Gmail send,
etc.) will eventually be implemented as an independent `Tool` registered
in a `ToolRegistry`, so that the agent orchestrator (Phase 9) can select
and invoke tools dynamically instead of relying on hard-coded
if/elif branching.

Phase 0 only establishes the interface and an empty registry. Concrete
tools are added in Phases 3-7.
"""
