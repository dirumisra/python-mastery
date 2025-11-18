# Generative AI Project - Library Stack

This project uses a set of Python libraries for building Generative AI applications, including LLM pipelines, vector databases, embeddings, and web deployment.

---

## Core Python & Environment

| Library           | Purpose |
|-----------------|---------|
| `python-dotenv`  | Load environment variables from a `.env` file securely (e.g., API keys, secrets). |
| `requests`       | Make HTTP requests to APIs or web services. |
| `pydantic`       | Data validation and settings management (used in LangChain & FastAPI). |

---

## OpenAI & LangChain Stack

| Library                  | Purpose |
|-------------------------|---------|
| `openai`                | Official SDK for OpenAI models (GPT, embeddings). Handles API calls to generate text or embeddings. |
| `langchain`             | Framework for building pipelines and workflows with LLMs (chains, prompts, tools, agents). |
| `langchain-community`   | Extra LangChain integrations, utilities, and community-built extensions. |
| `tiktoken`              | Efficient tokenizer used to count tokens for OpenAI models (important for cost control and prompt engineering). |

---

## Vector Databases & RAG (Retrieval-Augmented Generation)

| Library                  | Purpose |
|-------------------------|---------|
| `chromadb`               | Local or in-memory vector database to store embeddings for semantic search or RAG workflows. |
| `faiss-cpu`              | High-performance vector similarity search engine from Facebook AI (used for fast retrieval of embeddings). |
| `sentence-transformers`  | Pretrained models to convert text into embeddings locally (alternative to OpenAI embeddings). |

---

## App Development & Deployment

| Library           | Purpose |
|-----------------|---------|
| `streamlit`      | Build interactive AI dashboards, chatbots, and web apps quickly. |
| `fastapi`        | Lightweight API framework for production-ready backend endpoints. |
| `uvicorn`        | ASGI server for running FastAPI apps efficiently. |

---

## Utilities & Performance

| Library           | Purpose |
|-----------------|---------|
| `tabulate`       | Pretty-print tables in the console (useful for debugging). |
| `numpy`          | Fundamental library for numerical operations, vectors, and matrices. |
| `pandas`         | Data manipulation and analysis for tabular data (CSV, JSON, Excel). |
| `tqdm`           | Progress bars for loops, downloads, or long-running tasks. |
| `rich`           | Enhanced console output with color, tables, and logging. |

---

## Optional but Recommended

| Library           | Purpose |
|-----------------|---------|
| `typeguard`      | Runtime type checking for Python (helps debug data flows). |
| `pytest`         | Testing framework to write unit and integration tests. |
| `notebook`       | Jupyter Notebook support in VS Code for interactive experiments. |

---

This setup ensures a solid **Generative AI environment**, ready for **experiments, web apps, and production-ready pipelines**.
