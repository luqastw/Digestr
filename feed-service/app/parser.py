# Parser de feeds RSS/Atom
#
# Seu trabalho:
# 1. Criar uma função que recebe uma URL de feed e retorna uma lista de artigos
# 2. Usar a biblioteca feedparser pra buscar e parsear o feed
# 3. Pra cada entry do feed, extrair:
#    - title  → entry.title
#    - link   → entry.link
#    - content → entry.summary ou entry.content[0].value (nem sempre existe)
#    - published_at → entry.published_parsed (precisa converter pra datetime)
# 4. Tratar exceções: URL inválida, feed fora do ar, campos ausentes
#
# Comece testando no terminal:
#   import feedparser
#   feed = feedparser.parse("https://feeds.bbci.co.uk/news/rss.xml")
#   print(feed.feed.title)
#   for entry in feed.entries[:3]:
#       print(entry.title)
#
# Depois de funcionar no terminal, traga a lógica pra cá.
