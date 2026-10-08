# AI Workplace Productivity Suite (WPS)

An AI-driven assistant designed to eliminate administrative fatigue by automating daily email creation, meeting note summarization, and task scheduling.

## Table of Contents
1. Key Features
2. Architecture & Tech Stack
3. System Prompts & Prompt Engineering Strategy
4. Responsible AI & Governance
5. Time Savings & ROI Metrics
6. Quick Start & Installation

---

## 1. Key Features

### Smart Email Generator
* **Context-Driven Drafting:** Generates complete emails from minimal bullet points or brief context.
* **Tone Switching:** Seamlessly converts outputs between **Formal**, **Informal**, and **Persuasive** styles.
* **Audience Adaptation:** Tailors vocabulary, brevity, and call-to-action for **Clients**, **Managers**, or **Internal Teams**.

### Meeting Notes Summarizer
* **Executive Summaries:** Translates unstructured meeting transcripts into 2-3 sentence overviews.
* **Key Decision Extraction:** Isolates strategic choices and rejected alternatives.
* **Action Item Matrix:** Automatically extracts deliverables, assigns owners, and flags explicit or inferred deadlines.

### AI Task Planner & Scheduler
* **Eisenhower Prioritization:** Categorizes tasks by Urgency and Importance.
* **Circadian Time-Blocking:** Schedules high-focus tasks during morning peak hours and batches administrative work in the afternoon.
* **Pacing & Buffers:** Automatically injects 10-15 minute rest/transition windows between high-cognitive load blocks.

---

## 2. Architecture & Tech Stack

* **Frontend:** React + Tailwind CSS (Hosted via Lovable.ai / Vercel)
* **AI Orchestration & API Layer:** OpenAI API (GPT-4o) / Google Gemini 1.5 Pro
* **Document & Database Integration:** Notion API (for task syncing) & Supabase (for context logging)

---

## 3. Production System Prompts

### Module 1: Smart Email Generator
```text
[SYSTEM INSTRUCTION]
Role: Executive Communications Specialist.
Objective: Draft targeted, highly context-aware emails based on user inputs.

Rules:
1. Identify Context, Audience (Client, Manager, Team), and Tone (Formal, Informal, Persuasive).
2. For Managers: Lead with results, state blockers immediately, keep under 150 words.
3. For Clients: Prioritize value, set clear delivery expectations, maintain warm professionalism.
4. For Team: Use clear bullet points, actionable next steps, and approachable tone.
5. Never invent dates or metrics not provided in the input prompt. Use bracket placeholders like [Date] for missing data.
