---
layout: "post"
title: "Site estático no Gitlab Pages"
description: Dicas para quem quer hospedar Jekyll no Gitlab
date: "2016-08-23 12:30"
category: desenvolvimento
tags: jekyll gitlab github
---

Migrei o site do Github para o Gitlab, para poder usar HTTPS no meu site
estático usando o meu próprio domínio. O Github Pages [já suporta HTTPS para
sites usando os domínios `*.github.io`][1] mas para domínios customizados, como
o meu, ainda não. Dá para [usar o CloudFlare como CDN][2], mas não é uma solução
ideal (leia o artigo linkado). O Gitlab Pages é uma alternativa completa.

Curioso que o Gitlab Pages é uma extensão do serviço de Integração Contínua,
o que permite rodar qualquer comando que resulte em arquivos estáticos.
No Github Pages ou você compila localmente, na sua máquina, ou você usa o Jekyll
[na versão que o Github usa][3], com os plugins que o Github permite. Compilar
localmente ainda é uma boa idéia, mas automatizar a compilação na nuvem permite
o uso da interface web para editar os artigos direto no Github/Gitlab. De todo
modo, estou livre pra migrar para outros sistemas como [Pelican][4] ou [Hugo][5].

E para deixar documentado, o Gitlab Pages usa o Gitlab CI para
compilar e publicar o site. [As instruções são simples e tem exemplos][6].
O principal é garantir que o seu script de CI tem um job chamado `pages` que
compila os arquivos em uma pasta chamada `public`. Os nomes são obrigatórios.

Se você precisar de mais exemplos, pode ler [o script que eu uso pro meu
blog][7].

[1]: https://github.com/blog/2186-https-for-github-pages
[2]: https://konklone.com/post/github-pages-now-supports-https-so-use-it#using-a-custom-domain-with-cloudflare
[3]: https://github.com/github/pages-gem
[4]: http://blog.getpelican.com/
[5]: http://gohugo.io/
[6]: https://pages.gitlab.io/
[7]: https://gitlab.com/barraponto/barraponto.gitlab.io/blob/master/.gitlab-ci.yml
