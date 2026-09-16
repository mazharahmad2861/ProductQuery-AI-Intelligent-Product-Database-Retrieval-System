# 🛒 ProductQuery AI — Intelligent Product Database & Retrieval System

An **ProductQuery AI** built with **FastAPI, LangChain, LangGraph, FAISS, and SQLite** that enables users to search, filter, compare, and discover products using natural-language queries.

The system combines **LLM-powered intent understanding**, **hybrid retrieval**, and **product ranking** to transform conversational queries into relevant product recommendations. It uses the existing **200-product SQLite database** as the source of structured product information while maintaining a separate **FAISS vector index** for semantic retrieval.

## ✨ Key Features

* **Natural Language Product Search** — Understand queries such as *"I need a laptop for gaming"* or *"show me affordable smartphones"* using LLM-powered intent detection.
* **Hybrid RAG Retrieval** — Combines **FAISS semantic search** with **SQL-based structured filtering** to retrieve relevant products from the 200-product catalog.
* **LangGraph Agent Workflow** — Orchestrates the application through a structured pipeline:
  **Intent → Retrieval → Ranking → Response**.
* **Product Comparison** — Retrieves and structures multiple products for side-by-side comparison.
* **Intelligent Product Ranking** — Ranks retrieved products using attributes such as price, rating, and availability.
* **Structured API Responses** — Exposes the shopping assistant through a **FastAPI REST API** with automatically generated Swagger documentation.
* **Modular Architecture** — Separates intent understanding, retrieval, ranking, and response generation so individual components can be independently improved.

## 🧠 Architecture

```text
                     User Query
                         │
                         ▼
                ┌─────────────────┐
                │   FastAPI API   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   Intent Agent  │
                │  LangChain/LLM  │
                └────────┬────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Retrieval Agent    │
              │                      │
              │  ┌───────┐ ┌───────┐ │
              │  │ FAISS │ │ SQLite│ │
              │  │Vector │ │  SQL  │ │
              │  │Search │ │Filter │ │
              │  └───────┘ └───────┘ │
              └──────────┬───────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Recommendation  │
                │     / Ranking   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Response Agent  │
                └────────┬────────┘
                         │
                         ▼
                    Final JSON
```

## 🔄 How It Works

For a query such as:

> **"Find me a gaming laptop under ₹60,000 with a good rating."**

The system processes it as follows:

1. **Intent Agent** identifies the user's intent and extracts relevant constraints such as category, budget, and other attributes.
2. **Retrieval Agent** combines semantic retrieval through FAISS with structured filtering through SQLite.
3. **Ranking Agent** orders the retrieved products according to the application's ranking criteria.
4. **Response Agent** converts the results into a clean, structured response suitable for the frontend or API consumer.

## 🏗️ Technology Stack

**Backend:** FastAPI, Uvicorn 

**GenAI:** LangChain, LangGraph, OpenAI API 

**Retrieval:** FAISS, SentenceTransformers 

**Database:** SQLite 

**Language:** Python 

**API:** REST, Pydantic

## 🎯 Project Objective

The goal of this project is to demonstrate how **LLMs, RAG, vector search, structured databases, and agent orchestration** can be combined to build a practical AI application rather than relying solely on an LLM for product recommendations.
