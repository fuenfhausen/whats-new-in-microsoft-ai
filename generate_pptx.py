"""Generate a PowerPoint deck summarizing what's new in Microsoft AI (Dec 2025 - Feb 2026)."""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ── Colour palette (Microsoft-inspired) ──────────────────────────────────────
DARK_BG    = RGBColor(0x1B, 0x1B, 0x1B)
ACCENT     = RGBColor(0x00, 0x78, 0xD4)  # Microsoft blue
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY = RGBColor(0xCC, 0xCC, 0xCC)
ORANGE     = RGBColor(0xFF, 0x8C, 0x00)
GREEN      = RGBColor(0x10, 0x7C, 0x10)
PURPLE     = RGBColor(0x88, 0x61, 0xC9)

prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)

W = prs.slide_width
H = prs.slide_height


# ── Helpers ───────────────────────────────────────────────────────────────────

def _set_bg(slide, color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def _add_rect(slide, left, top, width, height, color):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape


def _add_text_box(slide, left, top, width, height, text, font_size=18,
                  bold=False, color=WHITE, alignment=PP_ALIGN.LEFT, font_name="Segoe UI"):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.bold = bold
    p.font.color.rgb = color
    p.font.name = font_name
    p.alignment = alignment
    return txBox


def _add_bullet_slide(slide, items, start_top, left=Inches(0.8), width=Inches(11.5),
                      font_size=16, color=WHITE):
    """Add a text box with bullet list items."""
    txBox = slide.shapes.add_textbox(left, start_top, width, Inches(5))
    tf = txBox.text_frame
    tf.word_wrap = True
    for i, (title, desc) in enumerate(items):
        if i > 0:
            p = tf.add_paragraph()
        else:
            p = tf.paragraphs[0]
        p.space_before = Pt(8)
        p.space_after = Pt(4)

        run_title = p.add_run()
        run_title.text = title
        run_title.font.size = Pt(font_size)
        run_title.font.bold = True
        run_title.font.color.rgb = ACCENT
        run_title.font.name = "Segoe UI"

        if desc:
            run_desc = p.add_run()
            run_desc.text = f"\n{desc}"
            run_desc.font.size = Pt(font_size - 2)
            run_desc.font.bold = False
            run_desc.font.color.rgb = color
            run_desc.font.name = "Segoe UI"
    return txBox


def _accent_bar(slide, top):
    _add_rect(slide, Inches(0.5), top, Inches(1.2), Pt(4), ACCENT)


# ── Slide 1: Title ──────────────────────────────────────────────────────────

slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
_set_bg(slide, DARK_BG)
_add_rect(slide, 0, 0, W, Inches(0.15), ACCENT)

_add_text_box(slide, Inches(0.8), Inches(1.5), Inches(11), Inches(1.5),
              "What's New in Microsoft AI", font_size=44, bold=True, color=WHITE)
_add_text_box(slide, Inches(0.8), Inches(3.0), Inches(11), Inches(1),
              "Microsoft Foundry, Azure OpenAI Service & Related Platforms",
              font_size=24, color=LIGHT_GRAY)
_add_text_box(slide, Inches(0.8), Inches(4.2), Inches(11), Inches(0.8),
              "December 2025 \u2013 February 2026", font_size=20, color=ACCENT)
_add_text_box(slide, Inches(0.8), Inches(6.2), Inches(11), Inches(0.6),
              "Sources: Azure Blog, Microsoft Learn, Microsoft Tech Community",
              font_size=14, color=LIGHT_GRAY)


# ── Slide 2: Agenda / TOC ───────────────────────────────────────────────────

slide = prs.slides.add_slide(prs.slide_layouts[6])
_set_bg(slide, DARK_BG)
_add_rect(slide, 0, 0, W, Inches(0.15), ACCENT)
_add_text_box(slide, Inches(0.8), Inches(0.5), Inches(11), Inches(0.8),
              "Agenda", font_size=36, bold=True, color=WHITE)
_accent_bar(slide, Inches(1.3))

topics = [
    ("1.", "Microsoft Foundry Platform Updates"),
    ("2.", "New Models & Azure OpenAI Service"),
    ("3.", "AI Infrastructure & Hardware"),
    ("4.", "Azure Data Services for AI"),
    ("5.", "Agentic AI & Frameworks"),
    ("6.", "Key Model Quick-Reference Table"),
]
y = Inches(1.8)
for num, topic in topics:
    _add_text_box(slide, Inches(1.0), y, Inches(0.5), Inches(0.5), num,
                  font_size=20, bold=True, color=ACCENT)
    _add_text_box(slide, Inches(1.6), y, Inches(10), Inches(0.5), topic,
                  font_size=20, color=WHITE)
    y += Inches(0.65)


# ── Slide 3: Microsoft Foundry ──────────────────────────────────────────────

slide = prs.slides.add_slide(prs.slide_layouts[6])
_set_bg(slide, DARK_BG)
_add_rect(slide, 0, 0, W, Inches(0.15), ACCENT)
_add_text_box(slide, Inches(0.8), Inches(0.4), Inches(11), Inches(0.7),
              "Microsoft Foundry Platform", font_size=34, bold=True, color=WHITE)
_accent_bar(slide, Inches(1.1))

items = [
    ("Azure AI Foundry \u2192 Microsoft Foundry Rebrand",
     "Unified platform for building, deploying & governing AI apps and multi-agent systems. "
     "Includes Foundry IQ, Tools (1,400+ connectors), Agent Service, Control Plane, Models & Local."),
    ("Gartner MQ Leader \u2013 AI App Development Platforms (Dec 17, 2025)",
     "Positioned furthest for Completeness of Vision. 80,000+ enterprises using Foundry. "
     "Microsoft used its own AI agents to prepare the Gartner submission."),
    ("Foundry Key Pillars",
     "\u2022 Foundry IQ \u2013 Secure data grounding API for enterprise data\n"
     "\u2022 Foundry Agent Service \u2013 Multi-agent orchestration\n"
     "\u2022 Foundry Control Plane \u2013 Org-wide governance & observability\n"
     "\u2022 Foundry Local \u2013 On-device AI for low-latency / offline scenarios"),
]
_add_bullet_slide(slide, items, Inches(1.5))


# ── Slide 4: New Models - GPT-5.2 ───────────────────────────────────────────

slide = prs.slides.add_slide(prs.slide_layouts[6])
_set_bg(slide, DARK_BG)
_add_rect(slide, 0, 0, W, Inches(0.15), ACCENT)
_add_text_box(slide, Inches(0.8), Inches(0.4), Inches(11), Inches(0.7),
              "GPT-5.2 \u2013 The New Enterprise Standard", font_size=34, bold=True, color=WHITE)
_accent_bar(slide, Inches(1.1))

items = [
    ("GPT-5.2 (GA \u2013 Dec 11, 2025)",
     "Deeper logical chains, richer context handling, agentic execution. "
     "Generates design docs, runnable code, unit tests & deployment scripts with fewer iterations."),
    ("GPT-5.2-Chat (GA)",
     "Everyday workhorse optimized for info-seeking, technical writing, translation, "
     "career guidance & studying. Clear improvements over GPT-5.1-Chat."),
    ("Key Capabilities",
     "\u2022 Multi-step logical chains with explainable plans\n"
     "\u2022 Context-aware planning over large inputs (codebases, briefs)\n"
     "\u2022 Agentic execution across design \u2192 implementation \u2192 testing \u2192 deployment\n"
     "\u2022 Enterprise-grade safety, managed identities & policy enforcement"),
    ("Pricing",
     "GPT-5.2 Global Standard: $1.75 / million input tokens, $14.00 / million output tokens"),
]
_add_bullet_slide(slide, items, Inches(1.5))


# ── Slide 5: New Models - Claude ─────────────────────────────────────────────

slide = prs.slides.add_slide(prs.slide_layouts[6])
_set_bg(slide, DARK_BG)
_add_rect(slide, 0, 0, W, Inches(0.15), ACCENT)
_add_text_box(slide, Inches(0.8), Inches(0.4), Inches(11), Inches(0.7),
              "Anthropic Claude Models in Microsoft Foundry", font_size=34, bold=True, color=WHITE)
_accent_bar(slide, Inches(1.1))

items = [
    ("Claude Opus 4.6 (Feb 5, 2026)",
     "Most powerful Claude model for coding, agents & enterprise workflows. "
     "Delegates complex tasks end-to-end with autonomous production execution."),
    ("Claude Sonnet 4.6 (Feb 17, 2026)",
     "Frontier performance across coding, agents & professional work at scale. "
     "Complements Opus for teams needing a balance of performance and throughput."),
    ("Claude for Healthcare & Life Sciences (Jan 11, 2026)",
     "New tools, connectors & skills purpose-built for clinical, pharmaceutical "
     "and life sciences use cases \u2013 advanced reasoning & agentic workflows for healthcare."),
]
_add_bullet_slide(slide, items, Inches(1.5))


# ── Slide 6: New Models - Multimodal / Audio ─────────────────────────────────

slide = prs.slides.add_slide(prs.slide_layouts[6])
_set_bg(slide, DARK_BG)
_add_rect(slide, 0, 0, W, Inches(0.15), ACCENT)
_add_text_box(slide, Inches(0.8), Inches(0.4), Inches(11), Inches(0.7),
              "Image & Audio Model Updates (Dec 2025)", font_size=34, bold=True, color=WHITE)
_accent_bar(slide, Inches(1.1))

items = [
    ("GPT-image-1.5 (Limited Access)",
     "Latest image generation: inpainting, face preservation, image editing, up to 1536\u00d71024px. "
     "Successor to GPT-image-1 with improved quality & editing controls."),
    ("gpt-4o-mini-transcribe-2025-12-15 (ASR)",
     "~50% lower word error rate vs. predecessor. Improved multilingual performance. "
     "4\u00d7 reduction in hallucinations on silence \u2013 ideal for noisy, real-world audio."),
    ("gpt-realtime-mini-2025-12-15 (Speech-to-Speech)",
     "Feature parity with full GPT Realtime model in instruction-following & function-calling. "
     "Audio in \u2192 audio out, API-only."),
    ("gpt-4o-mini-tts-2025-12-15 (Text-to-Speech)",
     "New benchmark for multilingual synthesis. More natural, human-like speech with "
     "fewer artifacts and improved speaker similarity."),
]
_add_bullet_slide(slide, items, Inches(1.5))


# ── Slide 7: AI Infrastructure & Hardware ────────────────────────────────────

slide = prs.slides.add_slide(prs.slide_layouts[6])
_set_bg(slide, DARK_BG)
_add_rect(slide, 0, 0, W, Inches(0.15), ACCENT)
_add_text_box(slide, Inches(0.8), Inches(0.4), Inches(11), Inches(0.7),
              "AI Infrastructure & Hardware", font_size=34, bold=True, color=WHITE)
_accent_bar(slide, Inches(1.1))

items = [
    ("Maia 200 \u2013 Custom AI Inference Accelerator (Jan 26, 2026)",
     "Microsoft\u2019s next-gen custom silicon engineered to dramatically improve the economics "
     "of AI token generation. Gives Azure an edge in running models faster & more cost-efficiently."),
    ("NVIDIA Rubin Platform Readiness \u2013 CES 2026 (Jan 5, 2026)",
     "Azure superfactories pre-engineered for Vera Rubin NVL72 racks: 50 PF/chip, 3.6 EF/rack (5\u00d7 jump). "
     "6th-gen NVLink (~260 TB/s), ConnectX-9 1,600 Gb/s, HBM4 thermal planning already integrated."),
    ("High-Temperature Superconductors (Feb 10, 2026)",
     "Exploring superconductor technology to transform datacenter power infrastructure, "
     "addressing rising power demands from AI workloads."),
]
_add_bullet_slide(slide, items, Inches(1.5))


# ── Slide 8: Azure Data Services ────────────────────────────────────────────

slide = prs.slides.add_slide(prs.slide_layouts[6])
_set_bg(slide, DARK_BG)
_add_rect(slide, 0, 0, W, Inches(0.15), ACCENT)
_add_text_box(slide, Inches(0.8), Inches(0.4), Inches(11), Inches(0.7),
              "Azure Data Services for AI", font_size=34, bold=True, color=WHITE)
_accent_bar(slide, Inches(1.1))

items = [
    ("PostgreSQL on Azure \u2013 Supercharged for AI (Feb 2, 2026)",
     "\u2022 GitHub Copilot integration for SQL in VS Code\n"
     "\u2022 Invoke LLMs via SQL through Microsoft Foundry integration\n"
     "\u2022 DiskANN vector indexing for high-performance similarity search\n"
     "\u2022 MCP server connecting PostgreSQL \u2192 Foundry Agent Framework\n"
     "\u2022 Zero-ETL mirroring to Microsoft Fabric\n"
     "\u2022 PostgreSQL 18 GA, new V6 compute SKUs, Elastic Clusters"),
    ("Azure HorizonDB (Private Preview)",
     "New PostgreSQL-compatible service built for AI-native workloads. "
     "Scale-out compute, sub-millisecond latency, built-in AI features."),
]
_add_bullet_slide(slide, items, Inches(1.5))


# ── Slide 9: Agentic AI ─────────────────────────────────────────────────────

slide = prs.slides.add_slide(prs.slide_layouts[6])
_set_bg(slide, DARK_BG)
_add_rect(slide, 0, 0, W, Inches(0.15), ACCENT)
_add_text_box(slide, Inches(0.8), Inches(0.4), Inches(11), Inches(0.7),
              "Agentic AI & Frameworks", font_size=34, bold=True, color=WHITE)
_accent_bar(slide, Inches(1.1))

items = [
    ("Agentic Cloud Operations (Feb 11, 2026)",
     "New paradigm where AI agents assist with cloud operations \u2013 monitoring, "
     "incident response & management tasks powered by the Foundry platform."),
    ("Microsoft Marketplace for AI & Agent Strategy (Jan 15, 2026)",
     "New marketplace category helping organizations embed AI across every layer of operations. "
     "Accelerate delivery, scale efficiently & unlock new business potential."),
    ("Pantone \u2013 Agentic AI Case Study (Feb 12, 2026)",
     "Pantone launched an AI-powered experience combining an AI-ready database with "
     "agentic workflows, iterating rapidly on real user feedback."),
    ("Agents League Community Challenge (Feb 16\u201327, 2026)",
     "Developer challenge: build agents, compete live, win prizes. "
     "Part of Microsoft\u2019s push to grow the agentic AI developer ecosystem."),
]
_add_bullet_slide(slide, items, Inches(1.5))


# ── Slide 10: Model Quick-Reference Table ───────────────────────────────────

slide = prs.slides.add_slide(prs.slide_layouts[6])
_set_bg(slide, DARK_BG)
_add_rect(slide, 0, 0, W, Inches(0.15), ACCENT)
_add_text_box(slide, Inches(0.8), Inches(0.4), Inches(11), Inches(0.7),
              "Key Model Releases \u2013 Quick Reference", font_size=34, bold=True, color=WHITE)
_accent_bar(slide, Inches(1.1))

# Table
rows, cols = 9, 4
tbl_shape = slide.shapes.add_table(rows, cols, Inches(0.5), Inches(1.5),
                                    Inches(12.3), Inches(5.0))
table = tbl_shape.table

# Column widths
table.columns[0].width = Inches(3.5)
table.columns[1].width = Inches(2.5)
table.columns[2].width = Inches(4.5)
table.columns[3].width = Inches(1.8)

headers = ["Model", "Type", "Key Improvement", "Status"]
data = [
    ["GPT-5.2", "Reasoning/Chat", "Deeper logical chains, agentic execution", "GA"],
    ["GPT-5.2-Chat", "Chat", "Everyday workhorse, improved info-seeking", "GA"],
    ["Claude Opus 4.6", "Reasoning/Coding", "End-to-end autonomous task execution", "GA"],
    ["Claude Sonnet 4.6", "Coding/Agents", "Frontier performance at scale", "GA"],
    ["GPT-image-1.5", "Image Gen", "Inpainting, face preservation, 1536px", "Limited"],
    ["gpt-4o-mini-transcribe", "ASR", "50% lower WER, 4\u00d7 less hallucinations", "GA"],
    ["gpt-realtime-mini", "Speech-to-Speech", "Feature parity with full Realtime", "GA"],
    ["gpt-4o-mini-tts", "Text-to-Speech", "Best multilingual synthesis", "GA"],
]

def _style_cell(cell, text, bold=False, bg=None, fg=WHITE, size=13):
    cell.text = ""
    p = cell.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = fg
    run.font.name = "Segoe UI"
    cell.vertical_anchor = MSO_ANCHOR.MIDDLE
    if bg:
        cell.fill.solid()
        cell.fill.fore_color.rgb = bg

for i, h in enumerate(headers):
    _style_cell(table.cell(0, i), h, bold=True, bg=ACCENT, fg=WHITE, size=14)

row_bg = [RGBColor(0x2A, 0x2A, 0x2A), RGBColor(0x22, 0x22, 0x22)]
for r, row_data in enumerate(data):
    bg = row_bg[r % 2]
    for c, val in enumerate(row_data):
        _style_cell(table.cell(r + 1, c), val, bg=bg, fg=WHITE)


# ── Slide 11: Key Links ─────────────────────────────────────────────────────

slide = prs.slides.add_slide(prs.slide_layouts[6])
_set_bg(slide, DARK_BG)
_add_rect(slide, 0, 0, W, Inches(0.15), ACCENT)
_add_text_box(slide, Inches(0.8), Inches(0.4), Inches(11), Inches(0.7),
              "Key Links & Resources", font_size=34, bold=True, color=WHITE)
_accent_bar(slide, Inches(1.1))

links = [
    ("Microsoft Foundry Portal", "https://ai.azure.com/"),
    ("Foundry Product Page", "https://azure.microsoft.com/en-us/products/ai-foundry/"),
    ("Azure OpenAI What\u2019s New", "https://learn.microsoft.com/en-us/azure/ai-foundry/openai/whats-new"),
    ("Azure AI Blog", "https://azure.microsoft.com/en-us/blog/category/ai-machine-learning/"),
    ("Foundry Tech Community", "https://techcommunity.microsoft.com/category/azure-ai-foundry/blog/azure-ai-foundry-blog/"),
    ("Foundry Models Catalog", "https://azure.microsoft.com/en-us/products/ai-foundry/models/"),
    ("Foundry Agent Service", "https://azure.microsoft.com/en-us/products/ai-foundry/agent-service/"),
    ("Azure Updates Feed", "https://azure.microsoft.com/en-us/updates/"),
]

y = Inches(1.6)
for name, url in links:
    _add_text_box(slide, Inches(1.0), y, Inches(4), Inches(0.4), name,
                  font_size=16, bold=True, color=ACCENT)
    _add_text_box(slide, Inches(5.2), y, Inches(7.5), Inches(0.4), url,
                  font_size=14, color=LIGHT_GRAY)
    y += Inches(0.55)


# ── Slide 12: Closing ───────────────────────────────────────────────────────

slide = prs.slides.add_slide(prs.slide_layouts[6])
_set_bg(slide, DARK_BG)
_add_rect(slide, 0, 0, W, Inches(0.15), ACCENT)

_add_text_box(slide, Inches(0.8), Inches(2.5), Inches(11.5), Inches(1.2),
              "Start Building with Microsoft Foundry",
              font_size=40, bold=True, color=WHITE, alignment=PP_ALIGN.CENTER)
_add_text_box(slide, Inches(0.8), Inches(3.8), Inches(11.5), Inches(0.8),
              "https://ai.azure.com",
              font_size=24, color=ACCENT, alignment=PP_ALIGN.CENTER)
_add_text_box(slide, Inches(0.8), Inches(5.5), Inches(11.5), Inches(0.6),
              "Compiled from official Microsoft sources \u2013 February 2026",
              font_size=14, color=LIGHT_GRAY, alignment=PP_ALIGN.CENTER)


# ── Save ─────────────────────────────────────────────────────────────────────

output = r"c:\Users\petfue\Repos\whats-new-in-microsoft-ai\whats-new-microsoft-ai-dec2025-feb2026.pptx"
prs.save(output)
print(f"Saved: {output}")
