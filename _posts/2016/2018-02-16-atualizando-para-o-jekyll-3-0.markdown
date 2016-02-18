---
layout: "post"
title: "Atualizando para o Jekyll 3.0"
date: "2016-02-18 20:50"
categories: development
tags: jekyll, github
---

[Jekyll][jekyll-software] e [Github][github-service] são uma combinação simples
para manter no ar um site estático (sem banco de dados), hospedado no
próprio Github -- que assume inclusive a compilação do Jekyll!

Para isso, [a recomendação][jekyll-github-pages-setup] é sempre rodar o Jekyll
e pacotes relacionados nas versões suportadas pelo Github, automatizando a
atualização direto no Gemfile:

```ruby
source 'https://rubygems.org'

require 'json'
require 'open-uri'
versions = JSON.parse(open('https://pages.github.com/versions.json').read)

gem 'github-pages', versions['github-pages']
```

E foi assim que eu me vi precisando atualizar para o Jekyll 3. Seguindo as
[instruções do Jekyll][jekyll-upgrade] e [do Github][gh-pages-upgrade], eu
precisei fazer apenas algumas mudanças nos meus arquivos:

- Alterar meu conversor de markdown para o `kramdown`, único suportado
  pelo Github.
- Alterar meu destacador de sintaxe para `rouge`, único suportado pelo Github.
- Configurar o `kramdown` para suportar input à la Github (```) e ignorar
  quebras de linha no markdown.

[jekyll-software]: http://jekyllrb.com/
[github-service]: https://github.com/

[jekyll-github-pages-setup]: http://jekyllrb.com/docs/github-pages/#deploying-jekyll-to-github-pages
[jekyll-upgrade]: http://jekyllrb.com/docs/upgrading/2-to-3/
[gh-pages-upgrade]: https://github.com/blog/2100-github-pages-now-faster-and-simpler-with-jekyll-3-0
