## ChatSQL: AI-Powered Data Query App

Natural Language SQL Assistant | Built with Streamlit, LangChain, Groq API, SQLite & MySQL

## 🚀 Overview

ChatSQL is a smart, chat-based web application that lets users query structured databases like SQLite and MySQL using plain English. Powered by LangChain’s SQL Agent Toolkit and Groq’s LLaMA 3 LLM, this app bridges the gap between complex SQL syntax and natural user interaction.

Deployed Link - https://chatsql-ad95b8wfqbp6krcvmndw7i.streamlit.app/

<img width="2880" height="1800" alt="image" src= "https://github.com/user-attachments/assets/301e8331-7c8f-47e9-b40c-327f78c97070" />
<img width="2880" height="1800" alt="image" src= "https://github.com/user-attachments/assets/199d6265-f330-4740-ba9b-9aae6e535e68" />


## 🔧 Tech Stack

Frontend & UI: Streamlit

LLM Backend: Groq API with LLaMA 3-8B

LLM Framework: LangChain SQL Agent + Toolkit

Databases Supported: SQLite (finance.db) and MySQL

ORM & Engine: SQLAlchemy

Deployment: Localhost or Streamlit Cloud

## 🧠 Features
🔍 Chat with your finance data – Ask questions like “What’s my total spending this month?” or “Show all grocery expenses from July.”

🧑‍💻 LLaMA 3-powered natural language → SQL conversion

🗃️ SQLite & MySQL support with switchable modes

🧰 LangChain SQL AgentType used for reasoning and planning

🔐 Secure runtime API key usage (via .env or input field)

🛠️ Setup Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/ChatSQL.git
cd ChatSQL
2. Create virtual environment and install dependencies
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
3. Add your Groq API key
Either:

Add a .env file in the root with:

java
Copy
Edit
Groq API Key = "your_groq_api_key_here"
(Note: Your current .env file is included. DO NOT push it to GitHub — it's sensitive!)
Or:

Enter your key in the sidebar when running the app.

4. Run the Streamlit app
bash
Copy
Edit
streamlit run app.py
