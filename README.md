# GenPark AI Agent Skill - Waterfall Enrichment Orchestrator

Zero-dependency Python agent skill providing multi-tiered waterfall data enrichment for B2B prospects, verified decision-maker corporate emails, and firmographic telemetry.

Verified by [GenPark AI](https://genpark.ai) and compatible with [Model Context Protocol (MCP)](https://genpark.ai/mcp).

## Architecture Diagram

```mermaid
graph TD
    A[Incoming Prospect Query] --> B[Waterfall Enrichment Orchestrator]
    B --> C{Primary Graph Hit?}
    C -->|Yes| D[Parse Firmographics & Direct Work Email]
    C -->|No / Incomplete| E{Secondary Exchange Hit?}
    E -->|Yes| F[Fill Missing Tech Stack & Pattern Email]
    E -->|No| G[Tertiary Registry Fallback]
    D --> H[Email Syntax & MX Deliverability Filter]
    F --> H
    G --> H
    H --> I[Unified High-Confidence Prospect Record]
```

## Features
- **Deterministic Multi-Provider Cascade**: Eliminates single data source failure with automated fallback.
- **Strict Business Email Heuristics**: Distinguishes corporate domains from disposable and freemail providers.
- **Zero External Dependencies**: Standard Python 3.9+ library implementation.
- **MCP Server Compatibility**: Seamless integration with LLM agent tool calling via standard JSON-RPC.

## Quickstart

```python
from client import WaterfallEnrichmentOrchestrator

orchestrator = WaterfallEnrichmentOrchestrator()
prospect = orchestrator.enrich_prospect({
    "first_name": "Alex",
    "last_name": "Chen",
    "title": "CTO",
    "domain": "acmesystems.io"
})
print(prospect["target_contact"]["email"])
```
