---
layout: "post"
title: "Atualizando o package.json com yarn"
date: "2017-02-25 18:38"
---

O comando `yarn upgrade` vai respeitar as versões no arquivo `package.json` e
atualizar as dependências no package.json. O problema é que ele não marca as
atualizações no `package.json`, nem excede as versões especificadas. Quando se
tem testes apropriadamente escritos, é conveniente atualizar tudo e ver se algo
quebra.

Eu vi que o yarn oferece um comando `yarn outdated`, que lista as dependências
desatualizadas. Como eu sou fã de linha de comando, pensei em usar a saída dele
como entrada para o `yarn upgrade`. Meu problema é que a saída é num formato
ruim de processar.

Então eu usei a saída em json: `yarn outdated --json` e uma ferramenta de linha
de comando para processar json: [jq][jq-tool]. Isso permite pegar o json e
filtrar exatamente o que eu preciso: os nomes dos pacotes. Aí eu uso o `xargs`
pra juntar tudo como parametros do `yarn`. É uma linha só:

```sh
yarn outdated --json | jq '.data.body[][0]' | xargs yarn upgrade
```

Ponto pro time da linha de comando :)

[jq-tool]: https://stedolan.github.io/jq/
