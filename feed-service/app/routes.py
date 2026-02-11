# Rotas do Feed Service
# Aqui ficam os endpoints que o Gateway vai chamar.
# Consulte docs/api-contracts.md pra ver o formato esperado.
#
# Seu trabalho:
# 1. Criar um APIRouter do FastAPI
# 2. Implementar os endpoints:
#    - GET  /feeds?user_id=xxx        → lista feeds do usuário
#    - POST /feeds?user_id=xxx        → cadastra um feed (body: {url})
#    - POST /feeds/{feed_id}/fetch    → busca artigos do feed via RSS
#    - GET  /articles?feed_id=xxx     → lista artigos de um feed
#    - GET  /articles/{article_id}    → detalhe de um artigo
#
# Dica: comece pelo GET /feeds retornando uma lista vazia.
# Depois vá conectando com o banco (models.py) e o parser (parser.py).

from fastapi import APIRouter

router = APIRouter()

# TODO: implemente os endpoints aqui
