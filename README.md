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
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Vue.js_Logo_2.svg/960px-Vue.js_Logo_2.svg.png?_=20170919082558" height="40" alt="nextjs logo"  />
  <img width="12" />
  <img src="https://raw.githubusercontent.com/tomchristie/uvicorn/main/docs/uvicorn.png" height="40" alt="uvicorn logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" height="40" alt="fastapi logo"  />
  <img width="12" />
  <img src="https://www.ingenia.com/assets/images/tools/17.png" height="40" alt="langchain logo"  />
  <img width="12" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Postgresql_elephant.svg/960px-Postgresql_elephant.svg.png" height="40" alt="gemini logo"  />
  <img width="12" />
  <img src="https://www.trychroma.com/img/favicon.ico" height="40" alt="huggingface logo"  />
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
  <img src="https://github.com/Wisawathep/ReadmeTools/blob/main/Pet%20Shop%20AICS/Architecture.png" height="600"  />
  <img width="12" />
</div>

# Document Loader
Loads raw knowledge documents from text files and converts them into a unified document format for further processing in the RAG pipeline.
# Text Cleaner
Preprocesses raw text by removing unnecessary whitespace, formatting inconsistencies, and unwanted characters to improve document quality before chunking.
# Chunker
Splits documents into smaller semantic chunks while preserving their structure and metadata, enabling more accurate retrieval during question answering.
# Embedder
Generates dense vector embeddings for each text chunk using the BAAI/bge-m3 embedding model, allowing semantic similarity search instead of keyword matching.
# ChromaDB
Stores vector embeddings and metadata for all knowledge chunks, enabling efficient semantic retrieval of the most relevant information based on user queries.
# Input Guardrail
Validates user input before processing by detecting invalid, malicious, or out-of-scope requests to protect the system from prompt injection and unsafe inputs.
# Prompt Builder
Constructs the final prompt by combining the system instructions, retrieved knowledge context, and the user's question before sending it to the language model.
# Output Guardrail
Validates the generated response to ensure it is consistent with the retrieved context and reduces the risk of hallucinated or unsupported information.
# PostgreSQL
Stores conversation history, including user messages and AI responses, to support multi-turn conversations, session management, and future analytics.

## 📜 Result
<div align="center">
  <img src="https://github.com/Wisawathep/ReadmeTools/blob/main/Pet%20Shop%20AICS/home1.png" height="600"  />
  <img width="12" />
  <img src="https://github.com/Wisawathep/ReadmeTools/blob/main/Pet%20Shop%20AICS/home2.png" height="600"  />
  <img width="12" />
  <img src="https://github.com/Wisawathep/ReadmeTools/blob/main/Pet%20Shop%20AICS/home3.png" height="600"  />
  <img width="12" />  
  <img src="https://github.com/Wisawathep/ReadmeTools/blob/main/Pet%20Shop%20AICS/chat1.png.png" height="600"  />
  <img width="12" />  
  <img src="https://github.com/Wisawathep/ReadmeTools/blob/main/Pet%20Shop%20AICS/chat2.png" height="600"  />
  <img width="12" />  
  <img src="https://github.com/Wisawathep/ReadmeTools/blob/main/Pet%20Shop%20AICS/chat3.png" height="600"  />
  <img width="12" />  
  <img src="https://github.com/Wisawathep/ReadmeTools/blob/main/Pet%20Shop%20AICS/chat4.png" height="600"  />
  <img width="12" />  
</div>

## 📜 Test Case
<div align="center">
  <img src="https://github.com/Wisawathep/ReadmeTools/blob/main/Pet%20Shop%20AICS/test%20case%20ex.png" height="600"  />
  <img width="12" />
</div>

***

<h5 align="center">COMPUTER ENGINEERING<br>KING MONGKUT'S UNIVERSITY OF TECHNOLOGY NORTH BANGKOK, A.Y. 2023/27</h5>
<p align="center">
  <img width="100" height="100" src="https://github.com/Wisawathep/ReadmeTools/blob/main/Kmutnb/Logo.png">
</p>
