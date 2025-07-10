import streamlit as st
from pathlib import Path
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq

# Page setup
st.set_page_config(page_title="Finance DB Chatbot", page_icon="💰")
st.title("💬 Chat with Your Finance Transactions")

# Constants
USE_LOCALDB = "USE_LOCALDB"
USE_MYSQL = "USE_MYSQL"

# Sidebar options
options = ["Use SQLite: finance.db", "Connect to MySQL"]
selected_opt = st.sidebar.radio("Choose your database", options)

# Get connection info
if options.index(selected_opt) == 1:
    db_mode = USE_MYSQL
    mysql_host = st.sidebar.text_input("MySQL Host")
    mysql_user = st.sidebar.text_input("MySQL User")
    mysql_password = st.sidebar.text_input("MySQL Password", type="password")
    mysql_db = st.sidebar.text_input("MySQL Database Name")
else:
    db_mode = USE_LOCALDB

# API key input
api_key = st.sidebar.text_input("🧠 Groq API Key", type="password")

# Check required fields
if not db_mode:
    st.info("Please select a database mode.")

if not api_key:
    st.info("Please enter your Groq API key.")

# Setup LLM
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="Llama3-8b-8192",
    streaming=True
)

# Connect to database
@st.cache_resource(ttl="2h")
def get_database_connection(db_mode, mysql_host=None, mysql_user=None, mysql_password=None, mysql_db=None):
    if db_mode == USE_LOCALDB:
        db_path = (Path(__file__).parent / "finance.db").absolute()
        creator = lambda: sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        return SQLDatabase(create_engine("sqlite:///", creator=creator))
    elif db_mode == USE_MYSQL:
        if not (mysql_host and mysql_user and mysql_password and mysql_db):
            st.error("⚠️ Please fill in all MySQL connection details.")
            st.stop()
        return SQLDatabase(
            create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}")
        )

# Load DB
if db_mode == USE_MYSQL:
    db = get_database_connection(db_mode, mysql_host, mysql_user, mysql_password, mysql_db)
else:
    db = get_database_connection(db_mode)

# LangChain SQL Agent setup
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

# Session state messages
if "messages" not in st.session_state or st.sidebar.button("🧹 Clear chat"):
    st.session_state["messages"] = [{"role": "assistant", "content": "Ask me anything about your transactions!"}]

# Display messages
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
user_query = st.chat_input("Ask about your income, spending, accounts...")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        callback = StreamlitCallbackHandler(st.container())
        response = agent.run(user_query, callbacks=[callback])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
