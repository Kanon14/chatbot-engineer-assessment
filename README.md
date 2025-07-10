# chatbot-engineer-assessment

## Project Overview
This is an intelligent assistant designed for ZUS Coffee to help customers inquire about drinkware products, outlet locations, and total cost calculations. Built using LangGraph, Pinecone, and LangChain tools, the chatbot dynamically leverages multiple tools to respond accurately based on real-time product and outlet data.

## 🚀 Features
🔍 **Product Search:** Query specifications, pricing, availability, and color variants for ZUS drinkware.

📍 **Outlet Lookup:** Find outlet names, services, and operating hours based on keywords or locations.

⏰ **Outlet Open Check:** Determine whether a ZUS outlet is currently open based on local time.

🧮 **Cost Calculator:** Computes total cost of selected items and automatically applies available discounts.

📚 **Vector-based Retrieval:** Uses Pinecone Vector DB to semantically match product queries.

🤖 **LLM Agentic Workflow:** Executes dynamic tool-based responses via LangGraph and LangChain tools.

## 🚀 Tech Stacks
|Components|Technology|
|----------|----------|
|LLM|OpenAI / HuggingFace|
|Framework|LangGraph, LangChain|
|Vector Database|Pinecone|
|Backend|FastAPI|
|Frontend|Streamlit|
|Embeddings|sentence-transformers/all-MiniLM-L6-v2|
|Data Sources|YAML (products). SQLite (outlets)|
|Tool Wrappers|LangChain Tools (custom defined)|

## 📂 Project Structure
```grapql
chatbot-engineer-assessment/
│
├── streamlit_app.py           # Streamlit frontend
├── main.py                    # LangGraph agent + workflow
├── zus_store.py               # To create both outlet and product doc store
├── tools/                     # All custom tools used in the agent
│   ├── product_tool.py
│   ├── outlet_lookup_tool.py
│   ├── outlet_open_tool.py
│   ├── cost_calculator.py
│   └── __init__.py
├── data/
│   ├── zus_outlets.db         # SQLite DB of outlets
│   └── zus_products.yaml      # YAML product catalog
├── utils/
│   ├── config_loader.py       # Loads configuration from YAML
│   ├── model_loader.py        # Loads LLM provider
│   ├── outlet_store.py        # Create outlet SQLite DB
│   └── product_store.py       # Create product doc vector store
├── prompt_library/
│   └── prompt.py              # SYSTEM_PROMPT definition
├── agent/
│   └── workflow.py            # LangGraph agent workflow
├── documentation/
│   ├── zus_chatbot_report.pdf # Report on chatbot assessment from setup to test
│   └── demo.mp4               # Demo video of the chatbot in action
├── requirements.txt
└── README.md
```

## ⚙️ Setup Instructions
1. **Clone the repository:**
```bash
git clone https://github.com/Kanon14/chatbot-engineer-assessment
cd zus-chatbot
```

2. **Create and activate a Conda environment:**
```bash
conda create -n coffee_chat python=3.10 -y
conda activate coffee_chat
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Setup `.env` file:**
```bash
PINECONE_API_KEY=your_pinecone_key
OPENAI_API_KEY=your_openai_key
```

5. **Prepare outlet db and product vector store:**
```bash
python zus_store.py
```

## 🤖 How to Run (Require Two Terminals; Refer to `documentation/demo.mp4`)
1. **Execute the main.py via FastAPI:**
```bash
uvicorn main:app --reload --port 8000
```

2. **Execute the Streamlit application:**
```bash
streamlit run streamlit_app.py
```

3. **Access the application via your web browser:**
```bash
open http://localhost:<port>
```

## 💡 Example Questions
- "Show me all the tumblers with leak-proof lids."
- "Is ZUS Pavilion outlet open now?"
- "Calculate total price for Sabrina Pink and Lucky Pink cups."
- "Which cup comes with ceramic interior?"
- "What are the colors for the All-Day Cup?"
- "What is the product specification for the All-Day Cup?"


## ⚖️ Key Trade-Offs Table
| **Aspect**               | **Choice A**                            | **Choice B**                         | **Trade-Off Summary**                                                                 |
| ------------------------ | --------------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------- |
| **Data Storage**         | YAML + SQLite (Simple, Local)           | CMS or Cloud DB (Scalable, Dynamic)  | Easy to manage and setup locally, but lacks scalability or dynamic updates.           |
| **Search Approach**      | Pinecone Vector Store (Semantic Search) | Keyword DB Query                     | More flexible and accurate but may be slower; keyword is faster but fragile.          |
| **LLM API**              | OpenAI or Groq (Free) (Fast, Powerful)  | Local HuggingFace (Low cost, slower) | OpenAI is powerful and consistent, but costly. Local is cheaper but less accurate.    |
| **Tool-based Execution** | Langchain Tools (Structured, Modular)   | Prompt-only (LLM-Driven Answers)     | Tools ensure correctness but increase complexity; pure prompting is easier but risky. |          |
| **Workflow Design**      | LangGraph Agentic Flow                  | Simple Sequential Prompting          | LangGraph allows branching logic, but harder to debug than linear prompts.            |

## 📃 License
This project is provided as part of a Chatbot Engineer Assessment. For academic and evaluation use only.