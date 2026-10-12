# Local AI Summarizer

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-7A3BFF?logo=ollama)
![Status](https://img.shields.io/badge/Status-Learning%20Project-34D399)
![License](https://img.shields.io/badge/License-MIT-green.svg)

</div>

<p align="center">
  <a href="#getting-started"><img src="https://img.shields.io/badge/Get%20Started-Now-4B8BBE?style=for-the-badge" alt="Get Started" /></a>
  <a href="#demo"><img src="https://img.shields.io/badge/View%20Demo-Open-7A3BFF?style=for-the-badge" alt="View Demo" /></a>
</p>

## Quick start

```bash
pip install ollama
ollama pull qwen2.5:3b
python summarizer.py notes.txt
```

A learning-focused local AI project for experimenting with private, on-device summarization and lightweight agent-style workflows. This repo shows how to take a text file, send it to a local model through Ollama, and generate a concise summary without relying on external cloud APIs.

Built for developers, students, and builders who want to learn how local models and AI agents can work in practice.

---

## Why this project

This repository is a simple but practical example of local AI in action:

- run inference locally on your machine
- keep your content private
- learn how to connect Python to an LLM via Ollama
- build a foundation for future AI-agent or workflow automation ideas

It is intentionally lightweight and easy to understand, which makes it a great project for learning and experimentation.

## Features

<div align="center">

| Feature | Value |
| --- | --- |
| Local-first AI | Runs completely on your machine using Ollama. |
| Privacy-friendly | No cloud API required for the summarization flow. |
| Beginner-friendly | Small, readable Python codebase designed for learning. |
| Agent-ready foundation | Easy to extend into prompt workflows and agent-style tools. |
| Fast iteration | Great for experimenting with prompts, models, and custom logic. |

</div>

## Built with

- Python 3.9+
- Ollama
- Local LLM inference
- `qwen2.5:3b` model
- Terminal-first CLI workflow

This stack keeps the project approachable while demonstrating how local models can power useful automation.

---

## How it works

The flow is intentionally simple:

1. Read a text file from disk
2. Pass the content to an Ollama model
3. Use a system prompt to request a concise summary
4. Print the result in the terminal

This gives a clean starting point for understanding local-model pipelines and agent behavior without the overhead of a large framework.

## Architecture

```text
┌───────────────────────┐
│   User / Developer    │
│   provides text file  │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│   Python CLI Script   │
│   summarizer.py       │
│   - reads file        │
│   - formats prompt    │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│       Ollama API      │
│   local model runtime │
│   qwen2.5:3b          │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│  Structured Output    │
│  3-bullet summary     │
│  printed to terminal  │
└───────────────────────┘
```

This architecture makes the project easy to study, extend, and evolve into more advanced AI workflows or agent-style tools.

## Project structure

```text
summarizer/
├── summarizer.py   # Python script that summarizes text files
├── notes.txt       # Example input used for testing
├── README.md       # Project documentation
└── .gitignore      # Optional local project settings
```

---

## Getting started

### Prerequisites

- Python 3.9 or newer
- Ollama installed locally
- A model available in your Ollama setup, such as `qwen2.5:3b`

### Install dependency

```bash
pip install ollama
```

### Pull the model

```bash
ollama pull qwen2.5:3b
```

### Run the script

```bash
python summarizer.py path/to/file.txt
```

Example:

```bash
python summarizer.py notes.txt
```

---

## Demo

```text
$ python summarizer.py notes.txt

--- Processing 'notes.txt' using Local LLM ---

Summary:
- The article discusses rising geopolitical tension in the Middle East.
- Security risks near the Bab al-Mandab Strait could affect shipping and energy markets.
- International actors are pushing for diplomatic de-escalation to avoid broader economic disruption.
```

---

## Use cases

- summarizing notes and personal research
- testing local LLM workflows without cloud services
- learning how AI agents can consume text and produce structured output
- building a foundation for smarter automation tools and pipelines

## Future ideas

- batch processing multiple files
- custom prompts for different summary styles
- save output to a file or JSON result
- connect this with a simple web or dashboard frontend
- extend into tool-calling or agent-like behavior

## License

This project is intended for learning, experimentation, and practical local AI exploration.

---

<div align="center">

<p>
  <strong>Local AI Summarizer</strong>
</p>

<p>
  <em>Private by default. Lightweight by design. Built for learning, experimentation, and the next AI workflow.</em>
</p>

</div>
