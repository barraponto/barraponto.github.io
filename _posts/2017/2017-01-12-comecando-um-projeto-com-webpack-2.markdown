---
layout: post
title: Começando um projeto com Webpack 2
description: Como usar Webpack 2 com PostCSS, Babel, ESLint e Hot Module Reloading
category: desenvolvimento
tags: webpack javascript mentoria
date: '2017-01-12 23:04'
---

Eu adotei o Webpack porque ele resolveu, pra mim, o problema de configurar o
ambiente de desenvolvimento Web moderno. Com ele eu consigo automatizar a
análise do javascript para evitar erros de sintaxe ou estilo de código, também o
preprocessamento de extensões (typescript, postcss), a inclusão de dependências,
a otimização do arquivo, a atualização em tempo real no browser... E o que mais
aparecer.

Eu acho a solução robusta e acabei criando meu arquivo de configuração padrão,
que eu pretendo documentar aqui como alternativa para os infinitos geradores
que, em geral, funcionam melhor do que a minha configuração -- mas são mais
difíceis de entender (principalmente porque nem tentam se explicar).

Vou anotar aqui passo a passo como configurei o meu Webpack. Aceito sugestões de
melhorias!

## Empacotamento (bundling)

Como instalar: `yarn add --dev webpack`

O [Webpack][webpack] tem esse nome porque ele nasceu para empacotar o seu Javascript.
Assim, no lugar de escrever mil tags `<script>`  no final do seu HTML, você só
escreve uma, que aponta para o arquivo que o Webpack gera pra você. (Na verdade,
eu não vou escrever nem essa tag, porque eu vou deixar o Webpack escrever pra
mim).

Funciona de forma simples: no seu arquivo `index.js` (ou qualquer outro nome),
você pode importar as dependências usando o estilo do ES6 (`import`) ou do
CommonJS (`require`). Eu vou usar exclusivamente o `import`, o que vai me exigir
preprocessar tudo com o [BabelJS][babel]. Segura a peruca que vale a pena.

Primeiro passo: definir o seu ponto de entrada. Isto é, explicar pra
configuração do Webpack que você vai começar a partir de um arquivo Javascript
específico. Você pode ter mais de um ponto de entrada, mas eu geralmente não
preciso disso.

```javascript
const path = require('path');

module.exports = {
  entry: path.join(__dirname, 'src', 'index.js'),
  output: {
    path: path.join(__dirname, 'dist'),
    filename: 'app.js'
  }
};
```

Note que eu uso o módulo `path` do Node para evitar problemas com o Windows
(que acha que os diretórios se separam com `\` no lugar de `/`). Não que eu use
Windows, mas algum contribuidor pode usar...

Note também que embora eu prefira `export default` (ES6), eu uso
`module.exports` (CommonJS) _porque este pedaço do código roda antes do Babel_.

## Preprocessando Javascript Moderno (ES6)

Como instalar: `yarn add --dev babel-core babel-loader babel-preset-es2015`

Para poder usar `import _ from underscore` dentro do meu arquivo `index.js`, eu
preciso preprocessá-lo com BabelJS. Isso exige configurar um _loader_, que é uma
espécie de serviço do Webpack que carrega outros arquivos (e aproveita para
processar os arquivos).

```javascript
module.exports = {
  // entry, output...
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: [
          {
            loader: 'babel-loader',
            options: {presets: [['es2015', {modules: false}]]},
          },
        ],
      },
    ]
  }
};
```

O Webpack 2 permitiu ser mais explícito com as opções, por isso temos uma chave
`rules` onde colocamos todas as regras para disparar os _loaders_. No caso,
usamos o `babel-loader` quando o nome do arquivo bate com a nossa expressão
regular `/\.js$/` (que só testa se a extensão do arquivo é `.js`).

O bom aqui é que usamos o BabelJS com as regras de preprocessamento para
suportar o moderno ES6 (também conhecido como ES2015), que em breve poderemos
usar nativamente no browser. E ao configurar com `{ modules: false }`, nós
ganhamos o desejado [_tree shaking_][tree-shaking] -- uma técnica de
empacotamento que só inclui as partes das bibliotecas (tipo underscore ou
jQuery) *que eu realmente usar*. Ou seja, eu poderia importar o _underscore.js_
mas só carregar as partes necessárias para fazer o `_.contains` funcionar (se
esse fosse o único método que eu utilizasse).

A parte do `exclude: /node_modules/` é para evitar processar com o Babel as
dependências que eu importei via `npm`. Afinal, esse código já tem que vir
pronto para usar!

## Analisando potenciais erros e estilo de código (linting)

Como instalar: `yarn add --dev eslint eslint-loader eslint-config-google`

É valioso usarmos ferramentas para evitar erros de digitação, em qualquer
linguagem. Algumas ainda ajudam a garantir nossa adesão a estilos específicos de
código (espaços no lugar de tabs, uso de maiúsculas, regras pra nomear
variáveis, etc). É o caso da minha ferramenta favorita: [ESLint][eslint]. Ela
foi desenhada para funcionar bem com o ES6 (ES2015) e é a única que tolera o JSX
(necessário se vc precisar trabalhar em um projeto com React).

```javascript
module.exports = {
  // entry, output...
  module: {
    rules: [
      // babel-loader rule, other rules...
      {
        test: /\.js$/, // arquivos terminados em .js
        // enforce:pre garante que o eslint roda primeiro
        enforce: 'pre',
        use: [{loader: 'eslint-loader'}]
      },
    ]
  }
};
```

O `enforce: pre` aí é só pra garantir que essa regra se aplica *antes* das
outras. Afinal, pra que empacotar código Javascript com defeitos?

Usando o ESLint, você precisa escolher quais regras seguir. Ele oferece a opção
de instalar três padrões diferentes: [JS Standard][standardjs],
[Google][googlejs] ou [Airbnb][airbnbjs] (existem muitas outras opções, mas
essas são as que ele oferece por padrão). Eu prefiro ter os ponto-e-vírgulas nos
lugares adequados, então JS Standard não me contempla. Ainda não estou
convencido se prefiro o modo do Google ou do Airbnb, então eu vou de Google
porque o Airbnb tem um monte de regras pensadas pro React. A menos que eu vá
usar React...

Uma chatice aqui é que eu preciso escrever o arquivo `.eslintrc.js`.
É uma boa prática, mas eu queria deixar tudo no `webpack.config.js` pra poder
manter tudo num arquivo só... Então crie um arquivo `.eslintrc.js` assim:

```javascript
module.exports = {
  env: {"browser": true, "es6": true}, // define as variáveis globais disponíveis
  extends: ["eslint:recommended", "eslint-config-google"], // define conjuntos de regras
  parserOptions: {sourceType: "module"}, // suporta o `import` do ES6
};
```

## Adicionando CSS e Bootstrap

Como instalar: `yarn add --dev css-loader style-loader file-loader`

O Webpack permite embutir o CSS no pacote (bundle). Sim, o CSS pode ser
empacotado no Javascript: primeiro o CSS é todo carregado como uma grande
_string_, depois ele é adicionado em um elemento `<style>` gerado pelo
Javascript. Doido, mas funciona.

Vou usar, como exemplo, o [Bootstrap][bootstrap]. Pra isso vou utilizar alguns
loaders:

* `css-loader`: processa o CSS, resolve os `@import` e tenta carregar os demais
  arquivos relacionados (imagens, fontes, etc).
* `style-loader`: efetivamente insere o CSS no DOM, criando um elemento
  `<style>` com todo o CSS carregado pelo `css-loader`.
* `file-loader`: simplesmente copia os arquivos da origem para que eles possam
  ser acessados no diretório configurado como `output` na configuração. Eu usei
  a opção `{name: [name].[ext]}` para poder salvar os arquivos com os nomes
  originais no diretório final. O Webpack corrige as referências direitinho.

```javascript
      {
        test: /\.css$/,
        use: [
          {loader: 'style-loader'},
          {loader: 'css-loader'},
        ],
      },
      {
        test: /\.(eot|otf|svg|ttf|woff|woff2)$/,
        use: [
          {
            loader: 'file-loader',
            options: {name: 'fonts/[name].[ext]'},
          },
        ],
      },
      {
        test: /\.(gif|jpg|png|webp)$/,
        use: [
          {
            loader: 'file-loader',
            options: {name: 'images/[name].[ext]'},
          },
        ],
      }
```

## Usando CSS do Futuro: PostCSS e cssnext

Como instalar: `yarn add --dev postcss-loader postcss-css-next`

Enquanto alguns browsers correm atrás pra dar suporte ao CSS3, o CSS4 já está
sendo desenvolvido pela W3C, inspirado entre outras coisas por recursos
experimentados antes em preprocessadores como Less e Sass. Para não ter que
perder tempo colocando prefixos e já poder usar a nova sintaxe, podemos usar o
[PostCSS][postcss] para processar o nosso CSS.

A configuração no Webpack é relativamente simples, mas exige mudar um pouquinho
as opções do css-loader pra dar suporte ao `@import`:

```javascript
      {
        test: /\.css$/,
        use: [
          {loader: 'style-loader'},
          {
            loader: 'css-loader',
            // aplica 1 loader anterior (postcss-loader) nos css @importados
            options: {importLoaders: 1},
          },
          // a configuração está em postcss.config.js
          {loader: 'postcss-loader'},
        ],
      },
```

Como mencionado no comentário, é preciso escrever um arquivo de configuração, o
`postcss.config.js` no mesmo diretório:

```javascript
var cssnext = require('postcss-cssnext');

module.exports = {
  plugins: [cssnext()],
};
```

Por padrão, o cssnext coloca prefixos para as últimas duas versões de cada
browser significativo (ie, chrome, firefox), todos os browsers com pelo menos
1% de usuários e o Firefox ESR (a versão estável). Isso é configurável, dá uma
olhada na documentação do [browserslist][browserslist].

## Gerando o HTML e incluindo o pacote

Como instalar: `yarn add --dev webpack-dev-server@beta html-webpack-plugin`

Quando você roda o Webpack, ele gera um arquivo `.js` com todo o código
empacotado dentro. Aí você só precisa escrever a tag `<script>` no seu HTML,
apontando para esse pacote. Mas se você é preguiçoso como eu, pode deixar o
próprio Webpack fazer o serviço. Para isso, usaremos o plugin de HTML:

```javascript
var HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  // entry, output, rules...
  plugins: [new HtmlWebpackPlugin()]
};
```

Só isso já resolve, mas fica ainda melhor se nós usarmos o servidor de
desenvolvimento do Webpack. Aí, no lugar de rodar o comando `webpack`, nós vamos
rodar o `webpack-dev-server`. Assim:

`./node_modules/.bin/webpack-dev-server --hot --content-base ./dist`

Neste caso, `dist` é o meu diretório onde ficam os arquivos compilados. Já o
`--hot` é a melhor parte: ele atualiza o código em tempo real no browser. É tipo
o live-reload, mas muito melhor!

Eu costumo colocar o comando na propriedade `scripts` do `package.json`. Fica
assim:

```json
{
  "scripts": {
    "dev-server": "webpack-dev-server --hot --content-base ./dist"
  }
}
```

Aí basta executar `npm run dev-server` e estamos prontos para usar!

## Um arquivo de teste

Como instalar: `yarn add bootstrap underscore`

Para servir de exemplo, vou mostrar um arquivo `.js` que usa o
[Underscore.js][underscore] e o Bootstrap. Note que como esses pacotes vão rodar
mesmo no browser, eu instalo sem o `--dev`.

Salve este arquivo no lugar apontado como `entry` na configuração do Webpack.

```javascript
import 'bootstrap/dist/css/bootstrap.css'; // tem que apontar pro arquivo css
import _ from 'underscore'; // ES6 é tão bonito que parece python

document.addEventListener('DOMContentLoaded', function(){
  _.each([1, 2, 3, 4], (e) => { // sintaxe de função do ES6
    console.log(e); // eslint-disable-line no-console
  });
})
```

Se você quiser ver um repositório com o resultado final, cheque
[no meu Github][modelo-webpack-config]!

[modelo-webpack-config]: https://github.com/barraponto/webpack-config
[webpack]: https://webpack.js.org/
[babel]: https://babeljs.io/
[eslint]: http://eslint.org/
[underscore]: http://underscorejs.org/
[bootstrap]: http://getbootstrap.com/
[postcss]: http://postcss.org/
[cssnext]: http://cssnext.io/
[standardjs]: http://standardjs.com/index.html
[googlejs]: https://google.github.io/styleguide/jsguide.html
[airbnbjs]: http://airbnb.io/javascript/
[browserslist]: https://github.com/ai/browserslist#config-file
[tree-shaking]: https://medium.com/@Rich_Harris/tree-shaking-versus-dead-code-elimination-d3765df85c80#.wysxxzryp
