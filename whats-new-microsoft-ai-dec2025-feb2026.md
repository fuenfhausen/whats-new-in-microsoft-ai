# What's New in Microsoft AI, Microsoft Foundry & Related Platforms

**Coverage Period:** December 2025 – February 18, 2026  
**Last Updated:** February 18, 2026

---

## Table of Contents

- [Microsoft Foundry (formerly Azure AI Foundry)](#microsoft-foundry)
- [Models & Azure OpenAI Service](#models--azure-openai-service)
- [Model Deprecations & Retirements](#model-deprecations--retirements)
- [AI Infrastructure & Hardware](#ai-infrastructure--hardware)
- [Azure Data Services for AI](#azure-data-services-for-ai)
- [Agentic AI & Frameworks](#agentic-ai--frameworks)
- [Industry & Ecosystem](#industry--ecosystem)

---

## Microsoft Foundry

### Azure AI Foundry Rebranded to Microsoft Foundry

- **Date:** November 2025 (Ignite), continued rollout through Feb 2026
- **Description:** Azure AI Foundry has been officially rebranded to **Microsoft Foundry**, reflecting its evolution into a unified platform for building, deploying, and governing AI applications and multi-agent systems at scale. The platform now encompasses Foundry IQ (secure data grounding API), Foundry Tools (1,400+ pre-built connectors), Foundry Agent Service (multi-agent orchestration), Foundry Control Plane (governance & observability), Foundry Models (model catalog), and Foundry Local (on-device AI).
- **Affected Services:** Microsoft Foundry, Azure AI Foundry, Azure OpenAI Service
- **Links:**
  - [Microsoft Foundry Product Page](https://azure.microsoft.com/en-us/products/ai-foundry/)
  - [Ignite 2025 Announcement](https://azure.microsoft.com/en-us/blog/azure-at-microsoft-ignite-2025-all-the-intelligent-cloud-news-explained/)

### Microsoft Named a Leader in Gartner Magic Quadrant for AI Application Development Platforms

- **Date:** December 17, 2025
- **Description:** Microsoft was recognized as a Leader and positioned furthest for Completeness of Vision in the 2025 Gartner Magic Quadrant for AI Application Development Platforms. The recognition highlights Microsoft's investment in agent frameworks, orchestration, and enterprise-grade governance. More than 80,000 enterprises are leveraging Foundry. Notably, Microsoft used its own AI agents built on Microsoft Agent Framework to assemble the Gartner submission.
- **Affected Services:** Microsoft Foundry, Foundry Agent Service, Foundry IQ, Foundry Control Plane
- **Links:**
  - [Blog Announcement](https://azure.microsoft.com/en-us/blog/microsoft-named-a-leader-in-gartner-magic-quadrant-for-ai-application-development-platforms/)
  - [Gartner Report](https://www.gartner.com/reprints/?id=1-2MD44GP0&ct=251125&st=sb)

---

## Models & Azure OpenAI Service

### GPT-5.2 Generally Available in Microsoft Foundry

- **Date:** December 11, 2025
- **Description:** OpenAI's GPT-5.2 and GPT-5.2-Chat are now generally available in Microsoft Foundry. GPT-5.2 introduces deeper logical chains, richer context handling, and agentic execution capabilities. It can generate design docs, runnable code, unit tests, and deployment scripts with fewer iterations. GPT-5.2-Chat is optimized as an everyday workhorse for info-seeking, technical writing, translation, and learning. Pricing starts at $1.75/million input tokens (Global Standard).
- **Affected Services:** Microsoft Foundry, Azure OpenAI Service
- **Links:**
  - [Blog Announcement](https://azure.microsoft.com/en-us/blog/introducing-gpt-5-2-in-microsoft-foundry-the-new-standard-for-enterprise-ai/)
  - [Microsoft Foundry Portal](https://ai.azure.com/)

### Claude Opus 4.6 Available in Microsoft Foundry

- **Date:** February 5, 2026
- **Description:** Anthropic's Claude Opus 4.6 is now available in Microsoft Foundry. It is designed for coding, agents, and enterprise workflows, allowing developers to delegate complex tasks end-to-end and trust the AI to execute independently in production.
- **Affected Services:** Microsoft Foundry, Azure AI Model Catalog
- **Links:**
  - [Blog Announcement](https://azure.microsoft.com/en-us/blog/claude-opus-4-6-anthropics-powerful-model-for-coding-agents-and-enterprise-workflows-is-now-available-in-microsoft-foundry-on-azure/)

### Claude Sonnet 4.6 Available in Microsoft Foundry

- **Date:** February 17, 2026
- **Description:** Claude Sonnet 4.6 is now available in Microsoft Foundry, designed for teams wanting frontier performance across coding, agents, and professional work at scale. This complements the earlier Opus 4.6 release, giving customers options across the Claude model family.
- **Affected Services:** Microsoft Foundry, Azure AI Model Catalog
- **Links:**
  - [Blog Announcement](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/claude-sonnet-4-6-in-microsoft-foundry-frontier-performance-for-scale/4494873)

### Claude in Microsoft Foundry for Healthcare & Life Sciences

- **Date:** January 11, 2026
- **Description:** Anthropic added new tools, connectors, and skills for Claude in Microsoft Foundry purpose-built for healthcare and life sciences. The update brings advanced reasoning, agentic workflows, and model intelligence specifically designed for clinical, pharmaceutical, and life sciences use cases.
- **Affected Services:** Microsoft Foundry, Azure AI for Health
- **Links:**
  - [Blog Announcement](https://www.microsoft.com/en-us/industry/blog/healthcare/2026/01/11/bridging-the-gap-between-ai-and-medicine-claude-in-microsoft-foundry-advances-capabilities-for-healthcare-and-life-sciences-customers/)

### GPT-image-1.5 Model Released

- **Date:** December 2025
- **Description:** GPT-image-1.5 is OpenAI's latest image generation model with improved performance, quality, editing controls, and face preservation. Supports text-to-image, image-to-image editing, inpainting, and high-quality generations up to 1536x1024 pixels. Limited access model requiring application.
- **Affected Services:** Azure OpenAI Service, Microsoft Foundry
- **Links:**
  - [What's New in Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/whats-new)
  - [Limited Access Application](https://aka.ms/oai/gptimage1.5access)

### Automatic Speech Recognition (ASR) Model Update

- **Date:** December 2025
- **Description:** The new `gpt-4o-mini-transcribe-2025-12-15` model delivers ~50% lower word error rate than its predecessor on English benchmarks, improved multilingual performance (Japanese, Indic, and more), and up to 4x reduction in hallucinations on silence—ideal for noisy environments and real-world audio streams.
- **Affected Services:** Azure OpenAI Service
- **Links:**
  - [What's New in Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/whats-new)

### Realtime-mini (Speech-to-Speech) Model Update

- **Date:** December 2025
- **Description:** The `gpt-realtime-mini-2025-12-15` model now has feature parity with the full GPT Realtime model in instruction-following and function-calling. Input and output are both audio with API-only deployment.
- **Affected Services:** Azure OpenAI Service
- **Links:**
  - [What's New in Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/whats-new)

### Text-to-Speech Model Update

- **Date:** December 2025
- **Description:** The new `gpt-4o-mini-tts-2025-12-15` model sets a new benchmark for multilingual speech synthesis with more natural, human-like speech, fewer artifacts, and improved speaker similarity. Input is text, output is audio, API-only deployment.
- **Affected Services:** Azure OpenAI Service
- **Links:**
  - [What's New in Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/whats-new)

---

## AI Infrastructure & Hardware

### Maia 200: Microsoft's Custom AI Inference Accelerator

- **Date:** January 26, 2026
- **Description:** Microsoft introduced Maia 200, a breakthrough custom inference accelerator engineered to dramatically improve the economics of AI token generation. This is Microsoft's next-generation AI accelerator designed to give Azure an edge in running AI models faster and more cost efficiently.
- **Affected Services:** Azure Infrastructure, Azure AI Compute
- **Links:**
  - [Blog Announcement](https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/)

### NVIDIA Rubin Platform Readiness & AI Datacenter Strategy

- **Date:** January 5, 2026 (CES 2026)
- **Description:** Microsoft announced Azure's readiness for NVIDIA's Vera Rubin platform at CES 2026. The Vera Rubin NVL72 racks deliver 50 PF NVFP4 inference per chip and 3.6 EF per rack (5x jump over GB200 NVL72). Azure's AI superfactories—including Fairwater sites in Wisconsin and Atlanta—are pre-engineered for Rubin's power, thermal, memory, and networking requirements. Azure has already incorporated 6th-gen NVLink (~260 TB/s), ConnectX-9 1,600 Gb/s networking, and HBM4 thermal planning.
- **Affected Services:** Azure HPC, Azure AI Infrastructure, Azure Virtual Machines (GPU)
- **Links:**
  - [Blog Announcement](https://azure.microsoft.com/en-us/blog/microsofts-strategic-ai-datacenter-planning-enables-seamless-large-scale-nvidia-rubin-deployments/)
  - [Azure AI Infrastructure](https://azure.microsoft.com/en-us/solutions/high-performance-computing/ai-infrastructure)

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

### Microsoft Marketplace for AI & Agent Strategy

- **Date:** January 15, 2026
- **Description:** A new category of AI-first organizations is emerging. Microsoft Marketplace now helps organizations chart their AI and agent strategy, embedding AI across every layer of operations to accelerate delivery, scale efficiently, and unlock new business potential.
- **Affected Services:** Azure Marketplace, Microsoft Foundry
- **Links:**
  - [Blog Announcement](https://azure.microsoft.com/en-us/blog/design-your-ai-and-agent-strategy-with-microsoft-marketplace/)

---

## Industry & Ecosystem

### Azure Partner Updates — December 2025

- **Date:** December 16, 2025
- **Description:** Monthly roundup of Azure updates for partners, emphasizing that organizations leading in AI make it foundational, rethinking processes and integrating new technologies from the start to improve efficiency.
- **Affected Services:** Azure Partner Ecosystem
- **Links:**
  - [Partner Blog](https://partner.microsoft.com/en-us/blog/article/azure-updates-december-2025)

### Agents League Community Challenge

- **Date:** February 16–27, 2026
- **Description:** An AI Agents Challenge inviting developers to build agents, watch live competitions, and win prizes. Part of Microsoft's push to grow the agentic AI developer ecosystem.
- **Affected Services:** Microsoft Foundry, Azure AI
- **Links:**
  - [Agents League](https://aka.ms/agentsleague)

---

## Model Deprecations & Retirements

Understanding Azure OpenAI model lifecycles is critical for planning. **Deprecation** means a model is no longer available to new customers but continues working for existing deployments. **Retirement** means the model is fully removed and all deployments return errors.

> **Full reference:** [Azure OpenAI Model Deprecations & Retirements](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/model-retirements)

### Already Deprecated (Action Required)

These models have passed their deprecation date and are no longer available for new deployments. Existing deployments continue to work until the retirement date.

| Model | Version | Deprecated | Retirement Date | Upgrade Path |
|-------|---------|------------|-----------------|--------------|
| o1 | 2024-12-17 | Dec 17, 2025 | Jul 15, 2026 | o3 |
| gpt-4o | 2024-05-13 | May 13, 2025 | Standard: Mar 31, 2026 (auto-upgrade starts Mar 9); Provisioned/Global/Data Zone: Oct 1, 2026 | gpt-5.1 |
| gpt-4o | 2024-08-06 | Aug 6, 2025 | Standard: Mar 31, 2026 (auto-upgrade starts Mar 9); Provisioned/Global/Data Zone: Oct 1, 2026 | gpt-5.1 |
| gpt-4o | 2024-11-20 | Nov 20, 2025 | Oct 1, 2026 | gpt-5.1 |
| gpt-4o-mini | 2024-07-18 | Jul 18, 2025 | Standard: Mar 31, 2026 (auto-upgrade starts Mar 9); Provisioned/Global/Data Zone: Oct 1, 2026 | gpt-4.1-mini |
| o3-mini | 2025-01-31 | Jan 31, 2026 | Aug 2, 2026 | o4-mini |

### Upcoming Preview Model Retirements (No Deprecation Period)

| Model | Version | Retirement Date | Upgrade Path |
|-------|---------|-----------------|--------------|
| gpt-5-chat | 2025-08-07 | Mar 1, 2026 | gpt-5.2-chat |
| gpt-5-chat | 2025-10-03 | Mar 1, 2026 | gpt-5.2-chat |
| gpt-5.1-chat | 2025-11-13 | No earlier than Mar 31, 2026 | TBD |
| gpt-5.2-chat | 2025-12-11 | No earlier than Apr 1, 2026 | TBD |
| computer-use-preview | 2025-03-11 | No earlier than Apr 14, 2026 | TBD |

### Upcoming GA Deprecations (2026)

These models are still current but will reach their deprecation date in 2026. Plan your migration path now.

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
| o3-deep-research | 2025-06-26 | Jun 26, 2026 | Dec 26, 2026 | TBD |
| gpt-5-mini | 2025-08-07 | Aug 7, 2026 | Feb 6, 2027 | TBD |
| gpt-5-nano | 2025-08-07 | Aug 7, 2026 | Feb 6, 2027 | TBD |

### Fine-Tuned Model Retirements

| Model | Version | Training Retirement | Deployment Retirement |
|-------|---------|---------------------|-----------------------|
| gpt-4o (fine-tuned) | 2024-08-06 | No earlier than Sep 30, 2026 (existing customers) | Mar 31, 2027 |
| gpt-4o-mini (fine-tuned) | 2024-07-18 | No earlier than Sep 30, 2026 (existing customers) | Mar 31, 2027 |
| gpt-4.1 (fine-tuned) | 2025-04-14 | At base model retirement | 1 year after training retirement |
| gpt-4.1-mini (fine-tuned) | 2025-04-14 | At base model retirement | 1 year after training retirement |
| gpt-4.1-nano (fine-tuned) | 2025-04-14 | At base model retirement | 1 year after training retirement |
| o4-mini (fine-tuned) | 2025-04-16 | At base model retirement | 1 year after training retirement |

### Key Action Items

1. **Immediate (by Mar 2026):** Migrate gpt-5-chat preview deployments to gpt-5.2-chat before Mar 1 retirement.
2. **Near-term (by Mar 31, 2026):** Migrate Standard deployments of gpt-4o (all versions) and gpt-4o-mini before auto-upgrades begin Mar 9.
3. **Plan now:** Begin testing gpt-5.1 as the replacement for gpt-4o across Provisioned/Global/Data Zone deployments (Oct 1, 2026 deadline).
4. **Monitor:** o1 retires Jul 15, 2026 — migrate to o3. o3-mini retires Aug 2, 2026 — migrate to o4-mini.

---

## Quick Reference: Key Model Releases (Dec 2025)

| Model | Type | Key Improvement | Status |
|-------|------|-----------------|--------|
| GPT-5.2 | Reasoning/Chat | Deeper logical chains, agentic execution | GA |
| GPT-5.2-Chat | Chat | Everyday workhorse, improved info-seeking | GA |
| Claude Opus 4.6 | Reasoning/Coding | End-to-end autonomous task execution | GA |
| Claude Sonnet 4.6 | Coding/Agents | Frontier performance at scale | GA |
| GPT-image-1.5 | Image Generation | Inpainting, face preservation, 1536px | Limited Access |
| gpt-4o-mini-transcribe-2025-12-15 | ASR | 50% lower WER, 4x less hallucinations | GA |
| gpt-realtime-mini-2025-12-15 | Speech-to-Speech | Feature parity with full Realtime model | GA |
| gpt-4o-mini-tts-2025-12-15 | Text-to-Speech | Best multilingual synthesis, natural speech | GA |

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
