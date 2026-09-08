<div align="center">
  <h1>TicketMind AI</h1>
  <p>An intelligent support ticket system that automatically categorizes, prioritizes, and routes user requests using OpenAI models.</p>
  
  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
  ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
  ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
</div>

---

## 📌 Project Overview
TicketMind AI is a backend application designed to streamline customer support workflows. By leveraging advanced Large Language Models (LLMs), the system analyzes incoming support tickets and automatically assigns the correct category, priority, and routing team.

## 🎯 Problem Statement
Customer support teams spend countless hours manually reading and triaging tickets. This manual routing creates bottlenecks, increases resolution time, and is prone to human error, ultimately degrading the customer experience.

## 💡 Why This Project Was Built
This project was built to demonstrate practical AI workflow automation. It focuses on turning unstructured user text into structured, deterministic data using LLMs, bridging the gap between raw AI capabilities and production-ready software engineering.

## ✨ Features
- **Automated Triage:** Uses GPT models to instantly classify tickets by Category, Priority, and Team.
- **Structured JSON Processing:** Employs Prompt Engineering to guarantee the LLM outputs strict JSON.
- **RESTful API:** Clean, decoupled API endpoints for seamless frontend integration.
- **Persistent Storage:** SQLite integration with SQLAlchemy ORM for reliable data management.

---

## 🏛️ System Architecture

```text
       [ User / Client ]
              │
              ▼
      ┌───────────────┐
      │ Client UI App │  (Frontend Client)
      └───────┬───────┘
              │ HTTP POST Request (JSON Payload)
              ▼
      ┌───────────────┐
      │ Flask Server  │  (Backend API Routes)
      └───────┬───────┘
              │ Prompt Creation & Input Validation
              ▼
      ┌───────────────┐
      │ OpenAI API    │  (LLM Engine - GPT Models)
      └───────┬───────┘
              │ JSON Response (Classification Data)
              ▼
      ┌───────────────┐
      │ Flask Server  │  (Response Parsing & DB Storage)
      └───────┬───────┘
              │ HTTP 201 Created (Structured JSON)
              ▼
      ┌───────────────┐
      │ Client UI App │  (Dynamic Rendering)
      └───────────────┘
```

---

## 🔄 End-to-End Request Flow
1. **Frontend:** The client submits a support ticket payload via a web interface or API.
2. **Flask Endpoint:** The backend route receives an HTTP POST request and parses the body.
3. **Prompt Engineering:** The service layer constructs a highly specific, few-shot prompt that instructs the LLM on exactly how to categorize the ticket.
4. **OpenAI API:** The Flask backend securely calls the OpenAI API to evaluate the prompt.
5. **Response Parsing:** The backend receives the LLM response, verifies it is valid JSON, and uses SQLAlchemy to store the record in the database.
6. **Frontend Rendering:** The structured classification is sent back to the client, allowing the UI to instantly update the user.

---

## 💻 Technical Documentation & Justifications

### Why Flask?
Flask was chosen for its lightweight, micro-framework architecture. It allows for rapid prototyping and fine-grained control over routing and application state without the overhead of larger frameworks.

### Why REST API & JSON?
A decoupled REST architecture ensures the backend can serve multiple clients. JSON is the universal standard for structured data transfer, making API integrations predictable.

### Why GPT Models?
OpenAI's models offer state-of-the-art semantic reasoning capabilities. Keyword-based parsers fail on nuanced language; an LLM understands intent and sentiment, leading to highly accurate classification.

### Why Prompt Engineering?
Directing the LLM requires precision. Advanced Prompt Engineering (system prompts, context setting, strict output instructions) was crucial to ensure the model returns highly deterministic JSON instead of conversational text.

### Error Handling
- **API Errors:** The application catches specific exceptions (e.g., OpenAI rate limits or connection failures) and returns appropriate HTTP status codes (e.g., 503, 429).
- **Validation:** Missing fields or unparseable JSON from the LLM are handled gracefully to prevent server crashes.

### API Key Security & Environment Variables
All secrets (like the `OPENAI_API_KEY`) and configurations (like `SECRET_KEY`) are managed strictly via `.env` files and the `os.environ` library. Keys are never committed to version control.

---

## 📂 Folder Structure

```text
├── models/                  # SQLAlchemy Database Models
│   ├── __init__.py
│   └── ticket.py
├── routes/                  # API Endpoints (Flask Blueprints)
│   ├── __init__.py
│   ├── dashboard.py
│   └── tickets.py
├── services/                # Business Logic and LLM Integration
│   ├── __init__.py
│   └── classifier.py
├── .env.example             # Template for Environment Variables
├── config.py                # Application Configuration class
├── requirements.txt         # Python Dependencies
└── README.md
```

---

## 🚀 Installation & Setup Guide

### Prerequisites
- Python 3.8+
- OpenAI API Key

### Setup Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/vaithi018/ticket-system.git
   cd "Ticket System"
   ```
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```
3. **Activate the environment:**
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Configure Environment Variables:**
   - Copy the `.env.example` file to a new file named `.env`.
   - Add your OpenAI API Key:
     ```env
     OPENAI_API_KEY=your_openai_api_key_here
     SECRET_KEY=your_secure_secret
     ```
6. **Run the application:**
   ```bash
   flask run
   ```

---

## 📸 Screenshots

| Feature | Screenshot |
|---------|------------|
| Ticket Submission UI | *[Placeholder: Add screenshot of form here]* |
| AI Classification Result | *[Placeholder: Add screenshot of JSON or UI result]* |
| Admin Dashboard | *[Placeholder: Add screenshot of grouped tickets]* |

---

## 🔮 Future Enhancements
While this version relies on direct LLM API calls, future iterations aim to implement:
- **Retrieval-Augmented Generation (RAG):** To provide the LLM with context from historical, similar tickets without exceeding context windows.
- **Vector Databases:** Integration with Pinecone to enable semantic search over past resolved tickets.
- **Agentic Workflows:** Utilizing agent frameworks to allow the model to autonomously draft replies or query knowledge bases before categorization.

---

## 🎓 Learning Outcomes
- Designing RESTful APIs with Flask and Blueprints.
- Forcing deterministic, structured JSON outputs from non-deterministic LLMs.
- Handling asynchronous third-party API calls and implementing robust backend error handling.

## 📜 License
This project is licensed under the MIT License.
