---
layout: post
title: "Como instalar o Popcorn Time no Ubuntu"
date: "2015-09-22 10:24"
category: technology
tags: ubuntu, popcorn time
---

Os canalhas da anti-pirataria começaram a [atacar a comunidade ao redor do
Popcorn Time][repressao]. E nessa onda de repressão, conseguiram [fazer recuar
o time que mantinha o repositório de pacotes para o Ubuntu][scaleback]. O que é
uma pena, pois deixa o projeto mais difícil de instalar no sistema GNU/Linux
mais popular que existe.

Esse é um projeto especial: um software livre se apoiando no poder técnico do
bittorrent para realizar o compartilhamento dos arquivos com uma interface web
arrojada, bonita, daquelas que não dá pra reclamar. E a adoção do projeto é
crescente, o que preocupa Hollywood mas me enche de esperança.

Então vamos ao assunto que importa: como instalar o PopcornTime no Ubuntu hoje?
Um tempo atrás, a solução era usar o PPA do povo da Webupd8, que permitia
manter o PopcornTime sempre atualizado. Mas essa opção já era e a equipe do
PopcornTime [não está disposta a manter um PPA ela mesma][official-ppa].

A outra solução [sugerida][ci-package] é pegar o pacote que eles preparam
automaticamente para testes. É bem simples:

* visite <https://ci.popcorntime.io/view/All/job/Popcorn-Desktop/lastStableBuild/>
* se vc não sabe se seu PC é 32bit ou 64bit, abra o terminal e digite `uname
  -m` e aperte enter.
* baixe o pacote `.deb` para seu Ubuntu
* clique duas vezes no `.deb` e deixe ele instalar!

O problema é que não vai atualizar sozinho, então vc precisa repetir esses
passos de vez em quando. Mas vale a pena!

[repressao]: http://arstechnica.co.uk/tech-policy/2015/08/two-danes-face-up-to-six-years-in-jail-for-explaining-how-to-use-popcorn-time/
[scaleback]: https://discuss.popcorntime.io/t/what-happened-to-the-webupd8team-ppa/48897/5
[official-ppa]: https://discuss.popcorntime.io/t/official-ubuntu-ppa-for-popcorn-time/48975/2
