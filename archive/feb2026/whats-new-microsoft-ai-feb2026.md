# What's New in Microsoft AI, Microsoft Foundry & Related Platforms

**Coverage Period:** February 2026
**Last Updated:** February 26, 2026

---

## Table of Contents

- [Microsoft Foundry](#microsoft-foundry)
- [Models & Azure OpenAI Service](#models--azure-openai-service)
- [Model Deprecations & Retirements](#model-deprecations--retirements)
- [AI Infrastructure & Hardware](#ai-infrastructure--hardware)
- [Azure Data Services for AI](#azure-data-services-for-ai)
- [Agentic AI & Frameworks](#agentic-ai--frameworks)
- [Foundry Blog Highlights](#foundry-blog-highlights)
- [Industry & Ecosystem](#industry--ecosystem)

---

## Microsoft Foundry

### Microsoft Foundry Platform Momentum

- **Date:** February 2026
- **Description:** Microsoft Foundry (formerly Azure AI Foundry) continues its momentum as the unified platform for building, deploying, and governing AI applications and multi-agent systems at scale. The platform encompasses Foundry IQ (secure data grounding API), Foundry Tools (1,400+ pre-built connectors), Foundry Agent Service (multi-agent orchestration), Foundry Control Plane (governance & observability), Foundry Models (model catalog), and Foundry Local (on-device AI). Over 80,000 enterprises are now leveraging Foundry.
- **Affected Services:** Microsoft Foundry
- **Links:**
  - [Microsoft Foundry Product Page](https://azure.microsoft.com/en-us/products/ai-foundry/)
  - [Microsoft Foundry Portal](https://ai.azure.com/)

---

## Models & Azure OpenAI Service

### Claude Sonnet 4.6 Available in Microsoft Foundry

- **Date:** February 17, 2026
- **Description:** Claude Sonnet 4.6 is now available in Microsoft Foundry, designed for teams wanting frontier performance across coding, agents, and professional work at scale. This complements the earlier Opus 4.6 release, giving customers options across the Claude model family.
- **Affected Services:** Microsoft Foundry, Azure AI Model Catalog
- **Links:**
  - [Blog Announcement](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/claude-sonnet-4-6-in-microsoft-foundry-frontier-performance-for-scale/4494873)

### Claude Opus 4.6 Available in Microsoft Foundry

- **Date:** February 5, 2026
- **Description:** Anthropic's Claude Opus 4.6 is now available in Microsoft Foundry. It is designed for coding, agents, and enterprise workflows, allowing developers to delegate complex tasks end-to-end and trust the AI to execute independently in production.
- **Affected Services:** Microsoft Foundry, Azure AI Model Catalog
- **Links:**
  - [Blog Announcement](https://azure.microsoft.com/en-us/blog/claude-opus-4-6-anthropics-powerful-model-for-coding-agents-and-enterprise-workflows-is-now-available-in-microsoft-foundry-on-azure/)

---

## AI Infrastructure & Hardware

### High-Temperature Superconductors for Datacenter Power

- **Date:** February 10, 2026
- **Description:** Microsoft is exploring high-temperature superconductors to transform datacenter power infrastructure, addressing the rising demand for efficient and reliable power delivery driven by AI and data-intensive computing workloads.
- **Affected Services:** Azure Datacenter Infrastructure
- **Links:**
  - [Blog Announcement](https://azure.microsoft.com/en-us/blog/can-high-temperature-superconductors-transform-the-power-infrastructure-of-datacenters/)

---

## Azure Data Services for AI

### PostgreSQL on Azure Supercharged for AI

- **Date:** February 2, 2026
- **Description:** Major enhancements to Azure Database for PostgreSQL for AI workloads, including: GitHub Copilot integration for SQL query writing in VS Code, seamless LLM invocation via SQL through Microsoft Foundry integration, DiskANN vector indexing for high-performance similarity search, MCP (Model Context Protocol) server for connecting PostgreSQL directly to Foundry's agent framework, zero-ETL mirroring to Microsoft Fabric, PostgreSQL 18 GA on Azure, new V6 compute SKUs, and Elastic Clusters. **Azure HorizonDB** (private preview) was also announced—a new PostgreSQL-compatible service built for AI-native workloads with scale-out compute and sub-millisecond latency.
- **Affected Services:** Azure Database for PostgreSQL, Azure HorizonDB (preview), Microsoft Foundry, Microsoft Fabric, GitHub Copilot
- **Links:**
  - [Blog Announcement](https://azure.microsoft.com/en-us/blog/postgresql-on-azure-supercharged-for-ai/)
  - [Azure Database for PostgreSQL](https://azure.microsoft.com/en-us/products/postgresql)
  - [Azure HorizonDB](https://azure.microsoft.com/en-us/products/horizondb)

---

## Agentic AI & Frameworks

### Agentic Cloud Operations

- **Date:** February 11, 2026
- **Description:** Microsoft announced "Agentic Cloud Operations," a new paradigm for running the cloud where AI agents assist with cloud operations tasks, monitoring, and incident response.
- **Affected Services:** Azure Operations, Azure Monitor, Azure Management
- **Links:**
  - [Blog Announcement](https://azure.microsoft.com/en-us/blog/agentic-cloud-operations-a-new-way-to-run-the-cloud/)

### Pantone Builds Agentic AI with AI-Ready Database

- **Date:** February 12, 2026
- **Description:** Pantone launched an AI-powered experience as an MVP using agentic AI built on Azure, showcasing how organizations can combine an AI-ready database with agentic workflows to gather real user feedback and iterate rapidly.
- **Affected Services:** Azure Database Services, Microsoft Foundry
- **Links:**
  - [Blog Announcement](https://azure.microsoft.com/en-us/blog/the-data-behind-the-design-how-pantone-built-agentic-ai-with-an-ai-ready-database/)

### Agents League Community Challenge

- **Date:** February 16–27, 2026
- **Description:** An AI Agents Challenge inviting developers to build agents, watch live competitions, and win prizes. Part of Microsoft's push to grow the agentic AI developer ecosystem.
- **Affected Services:** Microsoft Foundry, Azure AI
- **Links:**
  - [Agents League](https://aka.ms/agentsleague)

---

## Foundry Blog Highlights

Key posts from the [Microsoft Foundry Blog](https://devblogs.microsoft.com/foundry/) published in February 2026.

### Microsoft Agent Framework Reaches Release Candidate

- **Date:** February 19, 2026
- **Description:** Microsoft Agent Framework — the successor to Semantic Kernel and AutoGen — has reached Release Candidate status for both .NET and Python. The API surface is stable and all v1.0 features are complete. The framework provides simple agent creation, type-safe function tools, graph-based workflows (sequential, concurrent, handoff, group chat), multi-provider support (Foundry, Azure OpenAI, OpenAI, GitHub Copilot, Anthropic Claude, AWS Bedrock, Ollama), and interoperability via A2A, AG-UI, and MCP standards.
- **Affected Services:** Microsoft Foundry, Agent Framework, Semantic Kernel, AutoGen
- **Links:**
  - [Blog Post](https://devblogs.microsoft.com/foundry/microsoft-agent-framework-reaches-release-candidate/)
  - [Documentation](https://learn.microsoft.com/en-us/agent-framework/)
  - [GitHub](https://github.com/microsoft/agent-framework)

### What's New in Microsoft Foundry | Dec 2025 & Jan 2026

- **Date:** February 18, 2026
- **Description:** Comprehensive roundup covering GPT-5.2 GA, GPT-5.1 Codex Max GA (77.9% SWE-Bench, 400K context, 50+ languages), Mistral Large 3, DeepSeek V3.2, Kimi-K2 Thinking, Cohere Rerank 4, GPT-image-1.5 GA, FLUX.2 [pro], updated audio models (Realtime Mini, ASR, TTS), new fine-tuning base models, Memory in Foundry Agent Service (preview), A2A Tool (preview), Computer Use (preview), Foundry MCP Server (preview), VS Code extension updates, and azure-ai-projects v2 beta SDK consolidation. Also covers AzureML SDK v1 EOL (June 30, 2026).
- **Affected Services:** Microsoft Foundry, Azure OpenAI Service, Foundry Agent Service, Azure AI SDKs
- **Links:**
  - [Blog Post](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-dec-2025-jan-2026/)

### DPO Fine-Tuning Using Microsoft Foundry SDK

- **Date:** February 13, 2026
- **Description:** Deep-dive guide on Direct Preference Optimization (DPO) fine-tuning using the Microsoft Foundry SDK. Covers how DPO simplifies model alignment by learning directly from human preference pairs without a separate reward model, delivering precise control over model behavior for safety, helpfulness, and style.
- **Affected Services:** Microsoft Foundry, Azure OpenAI Fine-Tuning
- **Links:**
  - [Blog Post](https://devblogs.microsoft.com/foundry/dpo-fine-tuning-using-microsoft-foundry-sdk/)

### Beyond the Prompt – Why and How to Fine-tune Your Own Models

- **Date:** February 6, 2026
- **Description:** Explores when and why to move beyond prompt engineering and RAG to fine-tuning. Covers how fine-tuning customizes a pretrained model with additional training to improve performance, add new skills, or ensure consistent, policy-compliant outputs at scale — addressing the behavioral alignment gap that prompting alone cannot solve.
- **Affected Services:** Microsoft Foundry, Azure OpenAI Fine-Tuning
- **Links:**
  - [Blog Post](https://devblogs.microsoft.com/foundry/beyond-the-prompt-why-and-how-to-fine-tune-your-own-models/)

---

## Model Deprecations & Retirements

Understanding Azure OpenAI model lifecycles is critical for planning. **Deprecation** means a model is no longer available to new customers but continues working for existing deployments. **Retirement** means the model is fully removed and all deployments return errors.

> **Full reference:** [Azure OpenAI Model Deprecations & Retirements](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/model-retirements)

### Imminent Retirements (Action Required Now)

| Model | Version | Retirement Date | Upgrade Path |
|-------|---------|-----------------|--------------|
| gpt-5-chat (preview) | 2025-08-07 | Mar 1, 2026 | gpt-5.2-chat |
| gpt-5-chat (preview) | 2025-10-03 | Mar 1, 2026 | gpt-5.2-chat |
| gpt-4o (2024-05-13, 2024-08-06) Standard | — | Mar 31, 2026 (auto-upgrade starts Mar 9) | gpt-5.1 |
| gpt-4o-mini (2024-07-18) Standard | — | Mar 31, 2026 (auto-upgrade starts Mar 9) | gpt-4.1-mini |

### Upcoming GA Deprecations (2026)

| Model | Version | Deprecation Date | Retirement Date | Upgrade Path |
|-------|---------|------------------|-----------------|--------------|
| o1-pro | 2025-03-19 | Mar 19, 2026 | Sep 18, 2026 | o3-pro |
| gpt-4.1 | 2025-04-14 | Apr 14, 2026 | Oct 14, 2026 | gpt-5 |
| gpt-4.1-mini | 2025-04-14 | Apr 14, 2026 | Oct 14, 2026 | gpt-5-mini |
| gpt-4.1-nano | 2025-04-14 | Apr 14, 2026 | Oct 14, 2026 | gpt-5-nano |
| o3 | 2025-04-16 | Apr 16, 2026 | Oct 16, 2026 | TBD |
| o4-mini | 2025-04-16 | Apr 16, 2026 | Oct 16, 2026 | TBD |
| codex-mini | 2025-05-16 | May 16, 2026 | Nov 15, 2026 | TBD |
| o3-pro | 2025-06-10 | Jun 10, 2026 | Dec 10, 2026 | TBD |

### Key Action Items

1. **Immediate (by Mar 1, 2026):** Migrate gpt-5-chat preview deployments to gpt-5.2-chat before retirement.
2. **By Mar 9, 2026:** Test Standard gpt-4o and gpt-4o-mini workloads — auto-upgrades begin this date.
3. **By Mar 31, 2026:** Ensure all Standard gpt-4o / gpt-4o-mini deployments are migrated or tested with auto-upgraded versions.
4. **Plan ahead:** o1 retires Jul 15, 2026 (→ o3); o3-mini retires Aug 2, 2026 (→ o4-mini).

---

## Industry & Ecosystem

### Agents League Community Challenge

- **Date:** February 16–27, 2026
- **Description:** An AI Agents Challenge inviting developers to build agents, watch live competitions, and win prizes. Part of Microsoft's push to grow the agentic AI developer ecosystem.
- **Affected Services:** Microsoft Foundry, Azure AI
- **Links:**
  - [Agents League](https://aka.ms/agentsleague)

---

## Quick Reference: Key February 2026 Updates

| Item | Type | Date | Highlight |
|------|------|------|-----------|
| Claude Sonnet 4.6 | Model Release | Feb 17 | Frontier performance for coding & agents at scale |
| Claude Opus 4.6 | Model Release | Feb 5 | End-to-end autonomous task execution |
| PostgreSQL for AI | Data Service | Feb 2 | DiskANN vectors, MCP server, Copilot SQL, HorizonDB preview |
| High-Temp Superconductors | Infrastructure | Feb 10 | Exploring superconductors for datacenter power |
| Agentic Cloud Ops | Framework | Feb 11 | AI agents for cloud operations & incident response |
| Pantone Case Study | Ecosystem | Feb 12 | Agentic AI + AI-ready database in production |
| Agents League | Community | Feb 16–27 | Developer challenge for building AI agents |
| Agent Framework RC | Foundry Blog | Feb 19 | Successor to Semantic Kernel & AutoGen hits Release Candidate |
| Foundry What's New | Foundry Blog | Feb 18 | Comprehensive Dec/Jan roundup (GPT-5.2, Codex Max, A2A, Memory, MCP) |
| DPO Fine-Tuning Guide | Foundry Blog | Feb 13 | DPO fine-tuning walkthrough using Foundry SDK |
| Fine-Tuning Guide | Foundry Blog | Feb 6 | When & how to move beyond prompting to fine-tuning |

---

## Key Links & Resources

| Resource | URL |
|----------|-----|
| Microsoft Foundry Portal | https://ai.azure.com/ |
| Microsoft Foundry Product Page | https://azure.microsoft.com/en-us/products/ai-foundry/ |
| Azure OpenAI What's New | https://learn.microsoft.com/en-us/azure/ai-foundry/openai/whats-new |
| Model Deprecations & Retirements | https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/model-retirements |
| Azure AI Blog | https://azure.microsoft.com/en-us/blog/category/ai-machine-learning/ |
| Microsoft Foundry Tech Community | https://techcommunity.microsoft.com/category/azure-ai-foundry/blog/azure-ai-foundry-blog/ |
| Foundry Models Catalog | https://azure.microsoft.com/en-us/products/ai-foundry/models/ |
| Foundry Agent Service | https://azure.microsoft.com/en-us/products/ai-foundry/agent-service/ |
| Azure Updates Feed | https://azure.microsoft.com/en-us/updates/ |

---

*This document was compiled from official Microsoft sources including Azure Blog, Microsoft Learn, and Microsoft Tech Community.*
