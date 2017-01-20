---
layout: post
title: 'SQLAlchemy: Configurando multiplas relações com a mesma tabela'
description: Como fazer uma só referência (backref) com duas relações diferentes
date: '2016-02-18 22:16'
category: desenvolvimento
tags: python sqlalchemy flask
---

Um dos meus alunos na [Thinkful][thinkful-service] precisou configurar duas
relações de uma modelo `Game` com o modelo`User`. Pra isso é preciso declarar
qual campo de _foreign key_ está sendo usado. O modelo do `Game` ficou assim:

```python
class Game(Base):
    id = Column(Integer, primary_key=True)

    player1_id = Column(Integer, ForeignKey('users.id'))
    player1 = relationship('User', uselist=False, foreign_keys=['player1_id'])

    player2 = Column(Integer, ForeignKey('users.id'))
    player2 = relationship('User', uselist=False, foreign_keys=['player2_id'])
```

Simples. Mas para o `backref` no modelo `User`, eu queria apenas uma chave
listando todos os `Game` em que o `User` aparece como `player1` ou `player2`.
Para isso eu precisei definir manualmente o _primary join_:

```python
class User(Base):
    id = Column(Integer, primary_key=True)
    games = relationship(
        'Game', viewonly=True,
        primary_join='or_(User.id == Game.player1, User.id == Game.player2)')
```

Assim eu posso carregar um usuário e listar todos os seus jogos usando `user.games`:

```python
user = User.query.get(1)
games = [game for game in user.games]
```
