# What's New in Microsoft AI, Microsoft Foundry & Related Platforms

**Coverage Period:** March 1 - April 14, 2026
**Last Updated:** April 14, 2026

---

## Table of Contents

- [Microsoft Foundry Platform](#microsoft-foundry-platform)
- [Models & Azure OpenAI Service](#models--azure-openai-service)
- [Agent Platform & Runtime](#agent-platform--runtime)
- [Open Models & Ecosystem](#open-models--ecosystem)
- [Foundry Local (On-device AI)](#foundry-local-on-device-ai)
- [Model Deprecations & Retirements](#model-deprecations--retirements)
- [Quick Reference Timeline](#quick-reference-timeline)
- [Key Links & Resources](#key-links--resources)

---

## Microsoft Foundry Platform

### What's New in Microsoft Foundry | March 2026

- **Date:** April 9, 2026
- **Description:** Microsoft published the March 2026 Foundry roundup covering major releases across models, agents, safety, platform operations, and SDKs. Key themes include production reliability, enterprise guardrails, latency-sensitive workloads, and unified agent tooling on the v1 surface.
- **Affected Services:** Microsoft Foundry
- **Links:**
  - [What's New in Microsoft Foundry | March 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/)

### Priority Processing in Microsoft Foundry (GA)

- **Date:** March 23, 2026
- **Description:** Priority Processing became generally available for latency-sensitive AI workloads. It provides a prioritized inference lane with pay-per-call flexibility for production scenarios requiring consistent responsiveness.
- **Affected Services:** Microsoft Foundry Deployments
- **Links:**
  - [Priority Processing Announcement](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/announcing-priority-processing-in-microsoft-foundry-for-performance-sensitive-ai/4504788)

---

## Models & Azure OpenAI Service

### GPT-5.4 and GPT-5.4 Pro Released in Microsoft Foundry

- **Date:** March 5, 2026
- **Description:** GPT-5.4 became generally available, with GPT-5.4 Pro for deeper analytical workloads. Emphasis is on stronger instruction adherence, more dependable multi-step execution, and production reliability.
- **Affected Services:** Microsoft Foundry, Azure OpenAI Service
- **Links:**
  - [GPT-5.4 Announcement](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-gpt-5-4-in-microsoft-foundry/4499785)

### GPT-5.4 mini and GPT-5.4 nano Announced for Low-latency Workloads

- **Date:** March 17, 2026
- **Description:** GPT-5.4 mini and GPT-5.4 nano expanded the GPT-5.4 family for high-throughput and low-latency use cases such as classification, extraction, routing, and lightweight agent tasks.
- **Affected Services:** Microsoft Foundry, Azure OpenAI Service
- **Links:**
  - [GPT-5.4 mini and nano Announcement](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-open-ai%E2%80%99s-gpt%E2%80%915-4-mini-in-microsoft-foundry/4500569)

### Grok 4.2 GA in Foundry Model Catalog

- **Date:** March 30, 2026
- **Description:** Grok 4.2 from xAI graduated to general availability in the Foundry catalog, expanding model options for chat workloads via serverless and provisioned deployment patterns.
- **Affected Services:** Microsoft Foundry Model Catalog
- **Links:**
  - [March Foundry Update](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/)

---

## Agent Platform & Runtime

### Foundry Agent Service is GA

- **Date:** March 16, 2026
- **Description:** The next-generation Foundry Agent Service reached GA with Responses API alignment, end-to-end private networking, broader MCP authentication options (including OAuth passthrough), and GA evaluations with continuous monitoring into Azure Monitor.
- **Affected Services:** Foundry Agent Service, Azure Monitor, MCP integrations
- **Links:**
  - [Foundry Agent Service GA](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/)

### SDK 2.0 Stabilization Across Languages

- **Date:** March-April 2026
- **Description:** Stable 2.0 SDK releases were delivered across Python, JavaScript/TypeScript, and Java in March, with .NET 2.0 GA on April 1. The unified `AIProjectClient` model became central, replacing older split client patterns.
- **Affected Services:** Azure AI SDKs, Microsoft Foundry developer tooling
- **Links:**
  - [March Foundry Update](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/)

---

## Open Models & Ecosystem

### Fireworks AI on Microsoft Foundry (Public Preview)

- **Date:** March 11, 2026
- **Description:** Microsoft announced Fireworks AI integration in Foundry for high-performance open model inference. Initial model access includes DeepSeek V3.2, OpenAI gpt-oss-120b, Kimi K2.5, and MiniMax M2.5, with bring-your-own-weights support.
- **Affected Services:** Microsoft Foundry Model Catalog, Open model deployments
- **Links:**
  - [Fireworks AI on Foundry](https://azure.microsoft.com/en-us/blog/introducing-fireworks-ai-on-microsoft-foundry-bringing-high-performance-low-latency-open-model-inference-to-azure/)

### NVIDIA Nemotron Models Added to Foundry Catalog

- **Date:** March 16, 2026
- **Description:** NVIDIA Nemotron models were announced as available in the Foundry catalog at NVIDIA GTC, broadening options for open model workloads.
- **Affected Services:** Microsoft Foundry Model Catalog
- **Links:**
  - [March Foundry Update](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/)

---

## Foundry Local (On-device AI)

### Foundry Local is Generally Available

- **Date:** April 9, 2026
- **Description:** Foundry Local reached GA as Microsoft's cross-platform local AI runtime for Windows, Linux, and macOS. It supports offline inference with no per-token cloud costs, OpenAI-compatible request/response patterns, and hardware acceleration paths.
- **Affected Services:** Foundry Local, on-device AI workloads
- **Links:**
  - [Foundry Local GA](https://devblogs.microsoft.com/foundry/foundry-local-ga/)
  - [Foundry Local Documentation](https://learn.microsoft.com/en-us/azure/foundry-local/)

---

## Model Deprecations & Retirements

Understanding lifecycle signals is critical:

- **Deprecation:** no new deployments/customers for that version; existing deployments continue until retirement.
- **Retirement:** model version is removed and deployments return errors.

> **Reference:** [Azure OpenAI Model Deprecations & Retirements](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirements)

### Completed in Coverage Window

| Model / Family | Event | Date | Notes |
|---|---|---|---|
| gpt-4o Standard (2024-05-13, 2024-08-06) | Auto-upgrades started | Mar 9, 2026 | Upgrade target: gpt-5.1 |
| gpt-4o-mini Standard (2024-07-18) | Auto-upgrades started | Mar 9, 2026 | Upgrade target: gpt-4.1-mini |
| gpt-4o Standard (same versions, Standard deployment type) | Retired | Mar 31, 2026 | Other deployment types moved to Oct 1, 2026 |
| gpt-4o-mini Standard (2024-07-18, Standard deployment type) | Retired | Mar 31, 2026 | Other deployment types moved to Oct 1, 2026 |
| gpt-4.1 / gpt-4.1-mini / gpt-4.1-nano | Deprecated | Apr 14, 2026 | Retirement date: Oct 14, 2026 |

### Near-term Upcoming (After Today)

| Model / Family | Upcoming Date | Event | Upgrade Path |
|---|---|---|---|
| gpt-5-chat (preview 2025-08-07, 2025-10-03) | Apr 15, 2026 | Retirement | gpt-5.3-chat |
| gpt-5.1-chat (preview 2025-11-13) | Apr 15, 2026 | Retirement | TBD |
| o3 / o4-mini | Apr 16, 2026 | Deprecation | TBD |

### Action Items

1. Confirm all Standard `gpt-4o` / `gpt-4o-mini` traffic has moved to upgraded targets after Mar 31 retirement.
2. Stop planning new deployments on the `gpt-4.1` family as of Apr 14 deprecation.
3. Prepare for Apr 15 preview retirements in any regions still using preview chat variants.
4. Plan migrations for `o3` / `o4-mini` deprecation window starting Apr 16.
5. Continue using Azure Service Health alerts for retirement notifications.

---

## Quick Reference Timeline

| Date | Update | Type |
|---|---|---|
| Mar 5, 2026 | GPT-5.4 and GPT-5.4 Pro announced in Foundry | Model Release |
| Mar 9, 2026 | gpt-4o / gpt-4o-mini Standard auto-upgrades started | Lifecycle |
| Mar 11, 2026 | Fireworks AI on Foundry announced (public preview) | Ecosystem |
| Mar 16, 2026 | Foundry Agent Service reached GA | Agent Platform |
| Mar 17, 2026 | GPT-5.4 mini and GPT-5.4 nano announced | Model Release |
| Mar 23, 2026 | Priority Processing announced as GA | Platform |
| Mar 30, 2026 | Grok 4.2 reached GA in Foundry catalog | Model Catalog |
| Mar 31, 2026 | Standard gpt-4o and gpt-4o-mini retirement date | Lifecycle |
| Apr 1, 2026 | Azure.AI.Projects .NET 2.0 GA noted in monthly roundup | SDK |
| Apr 9, 2026 | Foundry Local reached GA | On-device AI |
| Apr 9, 2026 | March 2026 Foundry monthly roundup published | Summary |
| Apr 14, 2026 | gpt-4.1 family deprecation date | Lifecycle |

---

## Key Links & Resources

| Resource | URL |
|---|---|
| Microsoft Foundry Portal | https://ai.azure.com/ |
| March 2026 Foundry Monthly Update | https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/ |
| Foundry Agent Service GA | https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/ |
| Foundry Local GA | https://devblogs.microsoft.com/foundry/foundry-local-ga/ |
| Fireworks AI on Foundry | https://azure.microsoft.com/en-us/blog/introducing-fireworks-ai-on-microsoft-foundry-bringing-high-performance-low-latency-open-model-inference-to-azure/ |
| GPT-5.4 Announcement | https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-gpt-5-4-in-microsoft-foundry/4499785 |
| GPT-5.4 mini/nano Announcement | https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-open-ai%E2%80%99s-gpt%E2%80%915-4-mini-in-microsoft-foundry/4500569 |
| Priority Processing Announcement | https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/announcing-priority-processing-in-microsoft-foundry-for-performance-sensitive-ai/4504788 |
| Model Deprecations & Retirements | https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirements |

---

*Compiled from official Microsoft sources (Azure Blog, Microsoft Foundry Blog, Microsoft Learn, and Microsoft Tech Community).*