# 🤖 Agentic AI Chatbot with Groq

An **End-to-End Agentic AI Chatbot** built with **Groq** for ultra-fast inference and support for **multiple LLMs**.  
This chatbot can act as a basic conversational assistant, perform reasoning tasks, and dynamically switch between LLMs based on the use case.

---

## 🚀 Features
- ⚡ **Groq-powered inference** – lightning-fast LLM responses
- 🔄 **Multi-LLM Support** – choose from different models (LLaMA, Gemma, etc.)
- 🧠 **Agentic AI** – supports reasoning, tool use, and multi-step workflows
- 🖥️ **User-Friendly Interface** – simple UI to chat, select models, and see outputs
- 🧩 **Multiple Use Cases** – basic chatbot, Q&A, reasoning agent, and more

---

## 🛠️ Tech Stack
- **Backend:** Python, Groq API, LangChain
- **Frontend:** Streamlit

---

## 📸 Demo
<img width="1906" height="1052" alt="image" src="https://github.com/user-attachments/assets/0032784d-81d7-4160-9ebd-661f42b4f3d1" />


---

## 📂 Project Structure
```bash
.
├── app.py                 # Main entry point for running the chatbot
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── src/                   # Source code
│   ├── langgraphaeg/      # Language graph logic
│   │   └── graphicbuilder.py
│   │
│   ├── LLMS/              # LLM integration layer
│   │   └── groq_llm.py
│   │
│   ├── nodes/             # Node-based logic
│   │   ├── basic_chatbot_node.py
│   │   └── __init__.py
│   │
│   ├── state/             # State management
│   │   └── state.py
│   │
│   ├── tools/             # Tools for agents (extendable)
│   │   └── __init__.py
│   │
│   └── ui/                # UI components
│       ├── main.py        # Streamlit / UI entry point
│       ├── loadui.py      # UI loader
│       ├── display_result.py
│       └── uiconfigfile.json  # UI configuration
│
└── venv/                  # Virtual environment (not committed to Git)

