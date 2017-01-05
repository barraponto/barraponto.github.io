---
layout: "post"
title: "Usando elementos template com jQuery"
date: "2017-01-05 13:32"
---

O elemento `<template>` introduzido no HTML5 permite colocar um código HTML na
página sem que ele seja exibido, mas permanecendo disponível para manipulação
via Javascript.

Como exemplo, veja esta lista de tarefas:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Lista de Tarefas</title>
  </head>
  <body>
    <form id="nova-tarefa">
      <input type="text" id="tarefa-texto" placeholder="A fazer...">
      <button id="adicionar-tarefa">Adicionar</button>
    </form>
    <ul id="tarefas">
      <li class="tarefa">Escrever post sobre templates no HTML<li>
    </ul>
  </body>
</html>
```

Vocë pode ver que eu coloco um `<li>` pra servir de exemplo. É conveniente, já
que me permite ir ajustando o CSS pra ver como eu quero exibir resultado final.
Uma vez que eu já tenha colocado o CSS no lugar, é hora de escrever o Javascript
-- mas primeiro, vamos esconder aquele template!

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Lista de Tarefas</title>
  </head>
  <body>
    <form id="nova-tarefa">
      <input type="text" id="tarefa-texto" placeholder="A fazer...">
      <button id="adicionar-tarefa">Adicionar</button>
    </form>
    <ul id="tarefas">
    </ul>
    <template id="tarefa-template">
      <li class="tarefa">Escrever post sobre templates no HTML<li>
    </template>
  </body>
</html>
```

Movi para fora do `<ul>` e embrulhei numa tag `<template>`. Assim ele some, mas
continua disponível para manipular no Javascript:

```javascript
$(document).ready(function(){
  $('#nova-tarefa').submit(function(event){
    event.preventDefault(); // previne que o form seja enviado pro backend
    var novatarefa = $('#tarefa-texto').val();
    $('#tarefas').append(tarefaRender(novatarefa));
    $(this).trigger('reset'); // reseta o form para os valores padrão.
  });
});

var tarefaRender = function(tarefa){
  var template = $('#tarefa-template').prop('content'); // o DOM está escondido.
  return $(template).clone().text(tarefa);
};
```

A função `tarefaRender` é responsável por pegar o DOM do template, cloná-lo e
modificá-lo. O segredo é que o DOM no template fica oculto na propriedade
`.content`, então nós precisamos usar o método `.prop` do jQuery para acessá-lo.
Em seguida, na hora de cloná-lo, nós precisamos passar o DOM do template de
volta para o template, para podermos usar o `.clone` e o `.text`.
