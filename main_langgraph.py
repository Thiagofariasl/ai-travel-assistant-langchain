import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing_extensions import TypedDict, Literal
from langgraph.graph import StateGraph, START, END
from langchain_core.runnables import RunnableConfig
import asyncio

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

modelo = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.5,
    api_key=api_key
)

prompt_consultor_praia = ChatPromptTemplate.from_messages(
    [
        ("system", "Apresente-se como Sra Praia, Você é uma especialista em viagens com destinos para praia."),
        ("human", "{query}")
    ]
)

prompt_consultor_montanha = ChatPromptTemplate.from_messages(
    [
        ("system", "Apresente-se como Sr Montanha, Você é uma especialista em viagens com destinos para montanha."),
        ("human", "{query}")
    ]
)

cadeia_praia = prompt_consultor_praia | modelo | StrOutputParser()
cadeia_montanha = prompt_consultor_montanha | modelo | StrOutputParser()

class Rota(TypedDict):
    destino: Literal["praia", "montanha"]

prompt_roteador = ChatPromptTemplate.from_messages(
    [
        ("system", "Responda apenas com 'praia' ou 'montanha'."),
        ("human", "{query}")
    ]
)

roteador = prompt_roteador | modelo | StrOutputParser()

class Estado(TypedDict):
    query: str
    destino: Rota
    resposta: str

async def no_roteador(estado: Estado, config=RunnableConfig):
    resposta = await roteador.ainvoke({"query": estado["query"]}, config)

    destino = resposta.strip().lower()

    return {"destino": {"destino": destino}}

async def no_praia(estado: Estado, config=RunnableConfig):
    return {"resposta": await cadeia_praia.ainvoke({"query": estado["query"]}, config)}

async def no_montanha(estado: Estado, config=RunnableConfig):
    return {"resposta": await cadeia_montanha.ainvoke({"query": estado["query"]}, config)}

def escolher_no(estado: Estado)->Literal["praia", "montanha"]:
    return "praia" if estado["destino"]["destino"] == "praia" else "montanha"

grafo = StateGraph(Estado)
grafo.add_node("rotear", no_roteador)
grafo.add_node("praia", no_praia)
grafo.add_node("montanha", no_montanha)

grafo.add_edge(START, "rotear")
grafo.add_conditional_edges("rotear", escolher_no)
grafo.add_edge("praia", END)
grafo.add_edge("montanha", END)

app = grafo.compile()

async def main():
    resposta = await app.ainvoke(
        {"query": "Quero escalar montanhas no sul do país"}
    )
    print(resposta["resposta"])

asyncio.run(main())




