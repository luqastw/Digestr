# Entrypoint do Feed Service
# Aqui você cria a instância do FastAPI e registra as rotas.
#
# Seu trabalho:
# 1. Criar o app FastAPI
# 2. Importar e incluir as rotas de routes.py
# 3. Criar uma rota GET /health que retorna {"status": "ok"}
#
# Pra rodar localmente (fora do Docker):
#   uvicorn app.main:app --reload --port 8001
#
# Quando terminar, teste acessando http://localhost:8001/docs
# O FastAPI gera a documentação automaticamente.

from fastapi import FastAPI

app = FastAPI(title="FeedDigest — Feed Service")

# TODO: crie a rota /health aqui ou importe de routes.py

# TODO: importe e registre as rotas (app.include_router)
