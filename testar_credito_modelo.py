from dotenv import load_dotenv  
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI  

# Carrega as variáveis do .env
load_dotenv()

# Obtém a chave da API
chave_api = os.getenv("OPEN_API_KEY")
modelos = ["gpt-3.5-turbo", "gpt-4", "gpt-4o"]

for modelo_nome in modelos:
    try:
        modelo = ChatOpenAI(model=modelo_nome, api_key=chave_api)
        resposta = modelo.invoke([{"role": "user", "content": "Olá!"}])
        print(f"✅ Modelo {modelo_nome} funcionou!")
    except Exception as e:
        print(f"❌ Modelo {modelo_nome} falhou: {e}")