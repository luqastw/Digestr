# Models SQLAlchemy — definição das tabelas do banco
#
# Seu trabalho:
# 1. Criar a engine e a session do SQLAlchemy (conectando no DATABASE_URL)
# 2. Criar um Base declarativo
# 3. Definir o model Feed com os campos:
#    - id (inteiro, primary key, autoincrement)
#    - url (string, obrigatório)
#    - title (string, pode ser null — preenchido depois do primeiro parse)
#    - user_id (string, obrigatório)
#    - created_at (datetime, default=now)
# 4. Definir o model Article com os campos:
#    - id (inteiro, primary key, autoincrement)
#    - title (string)
#    - link (string, único — evita duplicatas)
#    - content (text — conteúdo bruto do artigo)
#    - published_at (datetime, pode ser null)
#    - feed_id (inteiro, foreign key pra Feed)
#    - summary (text, pode ser null — preenchido pelo Summarizer depois)
#
# Dica: pense na relação Feed → Articles (1:N)
# Um Feed tem muitos Articles. Use relationship() do SQLAlchemy.
