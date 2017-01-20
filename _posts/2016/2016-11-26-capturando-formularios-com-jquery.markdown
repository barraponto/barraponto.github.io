---
layout: post
title: Capturando formulários com jQuery
description: Como evitar que o formulário recarregue a página usando jQuery
date: '2016-11-26 22:46'
category: desenvolvimento
tags: jquery mentoria
---

Nesse tempo todo que eu estou trabalhando como mentor na [Thinkful.com][1], a
dúvida que eu mais vejo é sobre como capturar eventos de formulários HTML com
jQuery. Toda hora alguém adiciona o botão de submit e captura o evento ali:

```javascript
  $('input[type="submit"]').on('click', function(){ ... });
```

Isso até funciona, mas observa exclusivamente esse botão. O usuário não pode,
por exemplo, apertar o botão `enter` pra enviar logo. Aí o desenvolvedor vai lá
e coloca _também_ um `.on('keydown', function(){ ... });`. **NÃO!**

O certo é capturar o evento logo no `<form>`. Clicar no botão de submit ou
apertar `enter` disparam o evento `submit` no formulário. Aí você pode trabalhar
direto nele:

```javascript
$('form').on('submit', function(event){
  event.preventDefault();
  //...
});
```

Não pode esquecer do `preventDefault`, senão você realmente envia o vocabulário
e carrega uma nova página (às vezes a mesma, mas recarrega). É fácil ver quando
alguém esqueceu: a URL fica com os valores codificados, tipo `http://meusite.com/contato?email=arroba@ponto.com&assunto=errou`.

[1]: https://www.thinkful.com/
