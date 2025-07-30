## Opçõe de servidores de LLM:
https://platform.openai.com/api-keys
https://openrouter.ai/docs/quickstart
https://app.fireworks.ai/settings/users/api-keys

## Vídeo de ajuda:
https://www.youtube.com/watch?v=7L0MnVu1KEo

## Sites úteis:
https://n8n.io/
https://github.com/langchain-ai/langchain
https://platform.openai.com/docs/overview


## Passo a Passo

As bibliotecas necessárias para rodar o ambiente virtual estão no arquivo requirements.txt

1 - Ativar o ambiente virtual ->  D:\OneDrive\Ensino\IA com MCP - TITO\LangChain\langchain\Scripts> .\activate
2 - Projeto.py estão as principais configurações.
3 - .env informar a key da api do servidor de LLM que deseja utilizar. 
4 - servidor.py ao rodar esse arquivo será criado um servidor para uma api local, depois de criado é possível intergir com a interface a partir do código gerado. 
	Basta utilizar o localhost:"porta"/"nome_do_endopoint"/playground, ex: http://localhost:8000/tradutor/playground/
	Na execução via terminal, o script mostrará somente o caminho a api, sem o enpoint e o caminho para interface, sendo necessário adicionar no link informado.
	Esse serviço sobe uma api que permite ser chamada por outros aplicativos.
5 - cliente.py exemplo de uma chamada externa para api