# AI Customer Service Chatbot | Pet Shop Chatbot
HireSense is an AI-powered resume analysis web application that uses a Retrieval-Augmented Generation (RAG) pipeline to semantically search and summarize resumes.
The system enables HR users to upload PDF resumes, retrieve relevant candidates based on job requirements, and generate concise, LLM-based summaries to support faster and more accurate screening decisions.

## ⭐ Motivation
This project was developed to explore how Retrieval-Augmented Generation (RAG) can improve the reliability of AI-powered customer support systems. 
The goal was to build a chatbot that answers customer questions based only on company knowledge, while reducing hallucinations through prompt engineering, 
guardrails, and semantic retrieval techniques. In addition to providing accurate responses, the project focuses on building a modular, 
production-oriented AI pipeline that is easy to maintain, monitor, and extend.


## 🔑 Key Features
- AI-powered customer support chatbot using Retrieval-Augmented Generation (RAG)
- Semantic search with BAAI/bge-m3 embeddings and ChromaDB
- Custom document chunking for structured company knowledge
- Input and Output Guardrails for safer AI responses
- Prompt engineering to restrict responses to the knowledge base
- Conversation history management with PostgreSQL
- FastAPI backend with Vue.js frontend


<h2 align="left">🛠️ Tech Stacks</h2>

###
Python | Javascript | Vue.js | Uvicorn | FastAPI | FastAPI | LLama (Groq) | PostgreSQL | ChromaDB | Pydantic
<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" height="40" alt="javascript logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nextjs/nextjs-original.svg" height="40" alt="nextjs logo"  />
  <img width="12" />
  <img src="https://raw.githubusercontent.com/tomchristie/uvicorn/main/docs/uvicorn.png" height="40" alt="uvicorn logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" height="40" alt="fastapi logo"  />
  <img width="12" />
  <img src="https://registry.npmmirror.com/@lobehub/icons-static-png/latest/files/dark/langchain-color.png" height="40" alt="langchain logo"  />
  <img width="12" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Google_Gemini_icon_2025.svg/960px-Google_Gemini_icon_2025.svg.png" height="40" alt="gemini logo"  />
  <img width="12" />
  <img src="https://cdn.worldvectorlogo.com/logos/huggingface-2.svg" height="40" alt="huggingface logo"  />
  <img width="12" />
  <img src="https://assets.streamlinehq.com/image/private/w_300,h_300,ar_1/f_auto/v1/icons/logos/pydantic-srs7pxjs9skodrjb64x86f.png/pydantic-ae96ag6mv67bf6hz5726v8.png?_a=DATAg1AAZAA0" height="40" alt="pydantic logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="40" alt="vscode logo"  />
  <img width="12" />
</div>

## 📚 What I Learned
Through this project, I gained hands-on experience in designing and implementing an end-to-end Retrieval-Augmented Generation (RAG) system. 
I learned how to preprocess and chunk knowledge documents, generate vector embeddings, perform semantic retrieval with ChromaDB, 
and integrate large language models into a production-style application. I also explored prompt engineering, guardrail design, 
and debugging techniques to improve response reliability and reduce hallucinations. Most importantly, this project strengthened my understanding 
of AI system architecture and the practical challenges of deploying LLM-based applications.


## ⚙️ Architecture (RAG Pipeline)
<div align="center">
  <img src="https://github.com/Wisawathep/ReadmeTools/blob/main/HireSense/HireSense%20Architecture%201.png" height="600"  />
  <img width="12" />
  <img src="https://github.com/Wisawathep/ReadmeTools/blob/main/HireSense/HireSense%20Architecture%202.png" height="600"  />
  <img width="12" />
</div>

## 🧱 File Directory Structure
```
HireSense/
├── frontend/                          # Next.js Frontend (UI Layer)
│   ├── src/app/
│   │   ├── page.js                    # Landing page
│   │   ├── workspace/
│   │   │   └── page.js                # Main workspace UI (upload, search, analyze)
│   │   └── layout.js                
│   ├── public/                        # Static assets
│   └── package.json
│
├── backend/                           # FastAPI Backend (API & AI Layer)
│   ├── app/
│   │   ├── main.py                    # FastAPI entry point
│   │   │
│   │   ├── api/                       # API routes
│   │   │   ├── health.py              # Health check endpoint
│   │   │   ├── resumes.py             # Resume upload / list / delete APIs
│   │   │   ├── search.py              # Resume search based on job requirements (RAG-based)
│   │   │   └── analyze.py             # Resume analysis (RAG-based)
│   │   │
│   │   ├── core/                      # Core configuration
│   │   │   ├── config.py              # Environment & settings
│   │   │   └── logging.py             # Logging configuration
│   │   │
│   │   ├── schemas/                   # Pydantic schemas
│   │   │   ├── resume.py              # Resume-related schemas
│   │   │   ├── search.py              # Search schemas
│   │   │   └── analyze.py             # Analysis request/response schemas
│   │   │
│   │   ├── services/                  # Business & AI logic
│   │   │   ├── parsing/
│   │   │   │   └── pdf_parser.py      # PDF resume parser
│   │   │   │
│   │   │   ├── chunking/
│   │   │   │   └── chunker.py         # Resume text chunking
│   │   │   │
│   │   │   ├── embedding/
│   │   │   │   └── embeddings.py      # Transform Chunked Text --> vector
│   │   │   │
│   │   │   ├── vector_store/
│   │   │   │   └── faiss_store.py     # FAISS vector database
│   │   │   │
│   │   │   ├── llm/
│   │   │   │   ├── provider.py        # LLM provider (Gemini)
│   │   │   │   └── .env               # LLM API keys
│   │   │   │
│   │   │   └── rag/
│   │   │       └── rag_chain.py       # RAG pipeline & agent
│   │   │
│   │   └── utils/                     # Utility helpers
│   │       └── file_handler.py        # File save / delete helpers
│   │
│   ├── requirements.txt
│   └── .env                           # Backend environment variables
│
├── .gitignore
└── README.md
```

## 📜 Result
<div align="center">
  <img src="https://github.com/Wisawathep/ReadmeTools/blob/main/HireSense/homepage_final1.png" height="600"  />
  <img width="12" />
  <img src="https://github.com/Wisawathep/ReadmeTools/blob/main/HireSense/homepage_final2.png" height="600"  />
  <img width="12" />
  <img src="https://github.com/Wisawathep/ReadmeTools/blob/main/HireSense/homepage_final4.png" height="600"  />
  <img width="12" />  
  <img src="https://github.com/Wisawathep/ReadmeTools/blob/main/HireSense/workspace_final1.png" height="600"  />
  <img width="12" />  
  <img src="https://github.com/Wisawathep/ReadmeTools/blob/main/HireSense/upload_final.png" height="600"  />
  <img width="12" />  
  <img src="https://github.com/Wisawathep/ReadmeTools/blob/main/HireSense/added_resumes_final.png" height="600"  />
  <img width="12" />  
  <img src="https://github.com/Wisawathep/ReadmeTools/blob/main/HireSense/search_final.png" height="600"  />
  <img width="12" />  
  <img src="https://github.com/Wisawathep/ReadmeTools/blob/main/HireSense/result_final.png" height="600"  />
</div>

***

<h5 align="center">COMPUTER ENGINEERING<br>KING MONGKUT'S UNIVERSITY OF TECHNOLOGY NORTH BANGKOK, A.Y. 2023/27</h5>
<p align="center">
  <img width="100" height="100" src="https://github.com/Wisawathep/ReadmeTools/blob/main/Kmutnb/Logo.png">
</p>
