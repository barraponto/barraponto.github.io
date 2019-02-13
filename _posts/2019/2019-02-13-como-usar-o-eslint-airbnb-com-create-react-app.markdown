---
layout: post
title: Como usar o Eslint/Airbnb com Create React App
date: '2019-02-13 14:18'
category: desenvolvimento
tags: eslint react
---

A princípio parece fácil: use o `create-react-app` e em seguida rode
`npm install --save-dev eslint-config-airbnb`. Finalmente, edite seu arquivo
`.eslintrc.json` e coloque algo assim nele:

```json
{
  "extends": ["airbnb"]
}
```

Seria fácil, se o CRA não pensasse tão diferente do Airbnb. Logo de cara, eu
quis rodar `npx eslint ./src` e encontrei meu primeiro desafio:
`react/jsx-filename-extension` é uma regra que exige que arquivos JSX tenham a
extensão correspondente (`.jsx`). Fácil de corrigir pra maioria dos arquivos,
mas o CRA exige que o arquivo de entrada se chame `index.js`. Deixei um
comentário `/* eslint-disable-line react/jsx-filename-extension */` nele.
O primeiro de muitos comentários de "exceções" pro Eslint.

Em seguida percebi alguns erros de variáveis não definidas: `it` e `document`.
A primeira é coisa de teste e a melhor solução foi usar regras de Eslint que
suportam o Jest corretamente: `npm install --save-dev eslint-plugin-jest`. Já
pro `document` podemos usar o suporte pra variáveis globais nativas do browser.
O arquivo `.eslintrc.json` ficou assim:

```json
{
  "env": { "browser": true },
  "extends": ["airbnb", "plugin:jest/recommended"]
}
```

Agora pra lidar com o resto dos erros reportados: no `src/App.jsx` é preciso
transformar o componente em uma função (moleza). E o `src/serviceWorker.js` tem
um monte de `console.log`, um par de `use-before-define` que são fáceis de
corrigir e um erro que eu queria [corrigir no CRA][1] que é a modificação de um
parâmetro de função. Na função `registerValidSW`, um callback comete o seguinte
deslize:

```js
.then((registration) => registration.onupdatefound = () => {...})
```   

A solução é usar o método `.addEventListener`. Fica assim:

```js
.then((registration) => registration.addEventListener('updatefound', () => {...}))
```   

Agora sim, prontos pra trabalhar... Exceto se vc for usar Enzyme pros seus
testes. Aí vc precisa criar um arquivo `src/setupTests.js` e configurar o Enzyme
nele e, se vc instalou esse módulo corretamente como uma dependência de
desenvolvimento, vc vai começar a ver o erro `import/no-extraneous-dependencies`
porque na opinião do Airbnb, dependências de desenvolviment não deveriam ser
requeridas por arquivos na pasta `src`. `¯\_(ツ)_/¯`

A melhor solução que eu achei foi adicionar uma exceção no `.eslintrc.json`, que
ficou assim:


```json
{
  "env": { "browser": true },
  "extends": ["airbnb", "plugin:jest/recommended"],
  "overrides": [
    {
      "files": "src/setupTests.js",
      "rules": {
        "import/no-extraneous-dependencies": [
          "error",
          {
            "devDependencies": true,
            "optionalDependencies": false
          }
        ]
      }
    }
  ]
}
```
Por enquanto é isso. Vamos ver de quantos jeitos mais esse par CRA/Airbnb vai
me enrolar.
