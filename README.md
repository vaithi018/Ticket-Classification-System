<div align="center">
  <h1>TicketMind AI</h1>
  <p>An intelligent support ticket system that automatically categorizes, prioritizes, and routes user requests using OpenAI models.</p>
  
  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)
  ![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
  ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
</div>

---

## 📌 Project Overview
TicketMind AI is a full-stack AI application that streamlines the process of customer support. By leveraging modern web frameworks and advanced Large Language Models (LLMs), the system provides deterministic, structured outputs from unstructured user inputs to automatically categorize and route tickets.

## 🎯 Problem Statement
Customer support teams spend countless hours manually reading and triaging tickets. This manual routing creates bottlenecks, increases resolution time, and is prone to human error, ultimately degrading the customer experience.

## 💡 Why This Project Was Built
This project was developed to bridge the gap between complex AI capabilities and practical software engineering. It demonstrates how to integrate state-of-the-art LLMs into a robust RESTful API architecture, focusing on reliability, deterministic output generation, and seamless user experience.

## ✨ Features
- **Intelligent Processing:** Utilizes GPT models to analyze unstructured data contextually.
- **Structured JSON Outputs:** Employs advanced Prompt Engineering to guarantee predictable JSON responses.
- **Robust API Design:** Built on FastAPI for high performance, automatic validation, and asynchronous processing.
- **Modern UI:** A responsive frontend for seamless user interaction.

---

## 🏛️ System Architecture

```text
       [ User ]
          │
          ▼
  ┌───────────────┐
  │ Frontend UI   │  (React/HTML/JS)
  └───────┬───────┘
          │ HTTP POST Request (JSON Payload)
          ▼
  ┌───────────────┐
  │ FastAPI Server │  (Backend API)
  └───────┬───────┘
          │ Prompt Creation & Request Validation
          ▼
  ┌───────────────┐
  │ OpenAI GPT-4.1 │  (LLM Engine)
  └───────┬───────┘
          │ JSON Response containing Extracted Data
          ▼
  ┌───────────────┐
  │ FastAPI Server │  (Response Parsing & Error Handling)
  └───────┬───────┘
          │ HTTP 200 OK (Structured JSON)
          ▼
  ┌───────────────┐
  │ Frontend UI   │  (Dynamic Rendering)
  └───────────────┘
```

---

## 🔄 End-to-End Request Flow
1. **Frontend:** The User submits data via the frontend interface.
2. **FastAPI Endpoint:** The backend receives an HTTP POST request. It validates the input using Pydantic models.
3. **Prompt Engineering:** The service layer constructs a highly specific, few-shot prompt combining the user's data with strict formatting instructions.
4. **OpenAI API:** The FastAPI backend securely calls the OpenAI API, requesting a structured response.
5. **Response Parsing:** The backend receives the LLM response, validates the generated JSON schema, and handles any rate limits or API errors gracefully.
6. **Frontend Rendering:** The structured JSON is sent back to the frontend, updating the UI dynamically for the user.

---

## 💻 Tech Stack & Technical Justification

### Why FastAPI?
Chosen for its exceptionally high performance and native asynchronous support (`asyncio`). Its integration with Pydantic ensures strict request/response data validation, which is critical when handling unpredictable LLM inputs.

### Why GPT-4.1 (OpenAI API)?
State-of-the-art reasoning capabilities. Essential for complex tasks requiring contextual understanding rather than simple keyword matching.

### Why REST API & JSON?
A decoupled REST architecture ensures the backend can serve multiple clients. JSON is the universal standard for structured data transfer, making API integrations predictable and language-agnostic.

### Why Prompt Engineering?
Directing the LLM requires more than just passing data. Advanced Prompt Engineering (system prompts, few-shot examples, format enforcement) was crucial to ensure the model returns highly deterministic JSON instead of conversational text.

### Error Handling & Validation
- **Pydantic Models:** Enforce strict data types on all incoming requests.
- **Try/Except Blocks:** Specifically catch rate limit exceptions rather than generic exceptions.

### Security
- **Environment Variables:** All secrets (API Keys, Database URIs) are managed via `.env` files and are never committed to version control.
- **CORS:** Configured to only allow requests from specific frontend origins.

---

## 🚀 Installation & Setup Guide

### Prerequisites
- Python 3.9+
- OpenAI API Key

### Backend Setup
1. Clone the repository: `git clone https://github.com/vaithi018/Ticket-Classification-System.git`
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file based on `.env.example`:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```
6. Start the FastAPI server: `uvicorn app.main:app --reload`

---

## 🔮 Future Enhancements
While this version relies on direct LLM API calls, future iterations aim to implement:
- **Retrieval-Augmented Generation (RAG):** To provide the LLM with context from historical data without exceeding context windows.
- **Vector Databases:** Integration with Pinecone or ChromaDB for semantic search capabilities.
- **Agentic Workflows:** Utilizing frameworks like LangChain to allow the model to autonomously query databases before generating a response.

---

## 🎓 Learning Outcomes
- Designing and securing decoupled RESTful APIs using FastAPI.
- Forcing deterministic outputs from non-deterministic LLMs.
- Handling asynchronous API calls and implementing robust error handling for third-party services.

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
