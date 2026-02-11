# Contratos de API Interna — FeedDigest

Esse documento define os endpoints internos entre os serviços.
O Gateway (Node/TS) é o único que chama esses endpoints. Eles **não** são expostos ao público.

> O `user_id` é sempre enviado como query parameter pelo Gateway, que o extrai do JWT.

---

## Feed Service (`http://feed-service:8001`)

### `GET /health`

Verifica se o serviço está no ar.

**Response** `200`

```json
{ "status": "ok" }
```

---

### `GET /feeds?user_id={user_id}`

Lista os feeds cadastrados por um usuário.

**Response** `200`

```json
[
  {
    "id": 1,
    "url": "https://feeds.bbci.co.uk/news/rss.xml",
    "title": "BBC News",
    "user_id": "abc-123",
    "created_at": "2026-02-11T12:00:00Z"
  }
]
```

---

### `POST /feeds?user_id={user_id}`

Cadastra um novo feed.

**Request body**

```json
{
  "url": "https://feeds.bbci.co.uk/news/rss.xml"
}
```

**Response** `201`

```json
{
  "id": 1,
  "url": "https://feeds.bbci.co.uk/news/rss.xml",
  "title": "BBC News",
  "user_id": "abc-123",
  "created_at": "2026-02-11T12:00:00Z"
}
```

**Erros**

- `400` — URL inválida ou feed não encontrado
- `409` — Feed já cadastrado pra esse usuário

---

### `POST /feeds/{feed_id}/fetch`

Busca novos artigos de um feed específico (parseia o RSS).

**Response** `200`

```json
{
  "feed_id": 1,
  "new_articles": 5,
  "articles": [
    {
      "id": 10,
      "title": "Título do artigo",
      "link": "https://bbc.co.uk/artigo-1",
      "content": "<p>Conteúdo bruto em HTML...</p>",
      "published_at": "2026-02-11T10:30:00Z",
      "feed_id": 1
    }
  ]
}
```

**Erros**

- `404` — Feed não encontrado

---

### `GET /articles?feed_id={feed_id}`

Lista artigos de um feed.

**Response** `200`

```json
[
  {
    "id": 10,
    "title": "Título do artigo",
    "link": "https://bbc.co.uk/artigo-1",
    "content": "<p>Conteúdo bruto...</p>",
    "published_at": "2026-02-11T10:30:00Z",
    "feed_id": 1,
    "summary": "Resumo gerado por IA ou null se ainda não foi gerado"
  }
]
```

---

### `GET /articles/{article_id}`

Detalhe de um artigo específico.

**Response** `200`

```json
{
  "id": 10,
  "title": "Título do artigo",
  "link": "https://bbc.co.uk/artigo-1",
  "content": "<p>Conteúdo bruto completo...</p>",
  "published_at": "2026-02-11T10:30:00Z",
  "feed_id": 1,
  "summary": "Resumo gerado por IA ou null"
}
```

**Erros**

- `404` — Artigo não encontrado

---

## Summarizer Service (`http://summarizer:8002`)

### `GET /health`

**Response** `200`

```json
{ "status": "ok" }
```

---

### `POST /summarize`

Recebe o texto de um artigo e retorna um resumo.

**Request body**

```json
{
  "article_id": 10,
  "text": "Texto completo do artigo aqui...",
  "language": "pt"
}
```

**Response** `200`

```json
{
  "article_id": 10,
  "summary": "Resumo em 3 a 5 frases gerado pela IA."
}
```

**Erros**

- `400` — Texto vazio ou inválido
- `503` — Serviço de IA indisponível (fallback)
