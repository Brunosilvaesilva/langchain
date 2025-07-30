from dotenv import load_dotenv
import os
from langchain_fireworks import ChatFireworks
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Carrega a chave da API do arquivo .env
load_dotenv()
api_key = os.getenv("FIREWORKS_API_KEY")

# Instancia o modelo LLaMA v3.1 (8B) da Fireworks
modelo = ChatFireworks(
    model="accounts/fireworks/models/llama-v3p1-8b-instruct",
    api_key=api_key,
    temperature=0.7,
    max_tokens=256
)

##template de mensagens

template_mensagens = ChatPromptTemplate ([
    ("system", "Traduza o texto a seguir para {idioma}"),
    ("user", "{texto}")
])

# print(template_mensagens.invoke({"idioma": "francês", "texto": "Eu amo a zozo"}))
parser = StrOutputParser()
chain = template_mensagens | modelo | parser


texto = chain.invoke({"idioma": "francês", "texto": "Eu amo a zozo"})

print(texto)


