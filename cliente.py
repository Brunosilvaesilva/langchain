from langserve import RemoteRunnable

chain_remota = RemoteRunnable("http://localhost:8080/tradutor")
texto = chain_remota.invoke({"idioma": "espanhol", "texto": "Já deu like hoje?"})
print(texto)