✈️ AI Travel Assistant (LangChain + LangGraph + RAG)

An intelligent travel assistant built with LangChain, LangGraph, and LLMs (Groq).
This project demonstrates real-world AI engineering concepts such as multi-agent systems, conversational memory, and Retrieval-Augmented Generation (RAG).

🚀 Features

✈️ Destination Recommendation

Suggests travel destinations based on user interests (e.g., praias, montanhas)

🍽️ Restaurant Suggestions

Returns structured recommendations using Pydantic + JSON parsing

🧠 Conversational Memory

Maintains context across multiple interactions using session-based history

🔀 Multi-Agent Routing

Uses LangGraph to route queries dynamically:

🌊 Praia Specialist (Sra Praia)

🏔️ Montanha Specialist (Sr Montanha)

📄 RAG (Retrieval-Augmented Generation)

Answers questions based on PDF documents

Uses:

FAISS (vector database)

HuggingFace embeddings

🧠 Architecture Overview

This project combines multiple AI patterns:

Chains (LangChain) → Structured pipelines

Memory → Context-aware conversations

Agents (LangGraph) → Intelligent routing

RAG → Knowledge retrieval from documents

🛠️ Tech Stack

Python

LangChain

LangGraph

Groq (LLM API)

FAISS (Vector Store)

HuggingFace Embeddings

Pydantic

dotenv

⚙️ Setup
1. Clone o repositório
git clone https://github.com/seu-usuario/ai-travel-assistant-langchain.git
cd ai-travel-assistant-langchain
2. Crie o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
3. Instale as dependências
pip install -r requirements.txt
4. Configure o .env

Crie um arquivo .env na raiz:

GROQ_API_KEY=your_api_key_here
▶️ Como usar
🔹 1. Sugestão de viagem + restaurantes
resposta = cadeia.invoke({
    "interesse": "praias"
})
print(resposta)
🔹 2. Conversa com memória
lista_perguntas = [
    "Quero visitar um lugar no Brasil, famoso por praias e cultura.",
    "Qual a melhor época do ano para ir?"
]
🔹 3. Roteamento com agentes
resposta = await app.ainvoke({
    "query": "Quero escalar montanhas no sul do país"
})
🔹 4. Perguntas com RAG
print(responder("Como devo proceder em caso de roubo?"))
📌 Exemplos de Uso

Planejamento de viagens inteligentes

Assistente virtual com contexto

Sistemas multi-agente

Chatbots com base em documentos

🎯 Objetivo do Projeto

Este projeto foi desenvolvido para praticar e demonstrar:

Aplicações reais com LLMs

Arquitetura de sistemas com IA

Integração de múltiplos componentes (chains, agentes, RAG)

Construção de assistentes inteligentes

💡 Aprendizados

Como estruturar pipelines com LangChain

Uso de memória em aplicações conversacionais

Implementação de agentes com LangGraph

Construção de sistemas RAG completos

🚀 Próximos Passos (Melhorias)

Interface web (React ou Streamlit)

Deploy (Vercel / Docker)

Integração com APIs reais de turismo

Personalização de perfis de usuário

Cache de respostas

🤝 Contribuição

Sinta-se à vontade para abrir issues ou pull requests!
