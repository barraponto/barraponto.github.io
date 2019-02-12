---
layout: "post"
title: "Atualizando dependencias do seu projeto com NPM"
date: "2019-02-11 23:57"
category: desenvolvimento
tags: npm package.json node
---

Depois de um tempo sem mexer em um projeto, eu costumo rodar `npm outdated` para
descobrir o que eu preciso atualizar. Geralmente vejo uma tabelinha assim:

![Resultados do comando `npm outdated` mostrando pacotes desatualizados](/assets/images/npm-outdated-output.png)

Descobri que posso preguiçosamente rodar `npm update --save` para atualizar os
pacotes que estão no alcance do que está declarado no arquivo `package.json`.
Por padrão, `npm install` anota as versões com `^`, o que significa que ele pode
atualizar o segundo número da versão (o _minor_) mas não o primeiro (o _major_).
Dá pra ver o que ele vai fazer se vc reparar na coluna _Wanted_ acima.

A primeira dependência, no entanto, não vai se atualizar fácil assim. Como o
primeiro número (_major_) mudou, é sinal de mudanças incompatíveis, que podem
exigir intervenção manual. Chequei o que mudou no pacote e não era nada pra se
preocupar, então precisava atualizar essa última dependência e bastou um
comando: `npm install --save eslint-config-prettier@latest`. Essa tag `@latest`
garante que o npm instala a última versão mesmo indo além do declarado no
`package.json` (mas o `--save` atualiza o `package.json` também).

Nota: dois anos atrás eu publiquei como fazer esta atualização com `yarn`. Desde
então o `npm` melhorou muito e eu abandonei o `yarn`.
