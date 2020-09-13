---
layout: "post"
title: "web too many options"
date: "2020-09-13 15:02"
---

# Web: too many options

Starting a new web project demands a choice of front-end framework. You may object, but the truth is that going with vanilla web APIs _is also a choice_. And yet this is fine, it is a follow up option to choosing the web as your platform.

Tooling options pop up. Should you go with `yarn` or `npm`? Hopefully your starter kit makes this choice for you, so let's pick `create-react-app` as an example. Keep in mind that **every starter kit will make these choices**, though they will likely choose something different.

First of all: you will use a project bundler. Webpack is the default choice for `create-react-app`, but it's also the default in `vue init` and `ng new`. You could have gone with `parcel` or `pika`. Let's not dwell.

Then... are you extending Javascript? Most projects will use babel to provide backwards support, but `create-react-app` will use it to allow for modern yet-to-be-released syntax. But what about Typescript? CRA supports it, but won't use it by default. It is a choice, nonetheless.

While we're at it -- what about CSS extensions? CSS-in-JS is a popular trend with built-in _optional_ support for CSS Modules, but maybe you're into `styled-components` or `emotion`. Auto-prefixing (for backwards compatibility) is **on** by default, but any more PostCSS or Sass is up to you.

Actually `postcss-normalize` is available by default, but opt-in to use. You may go for a full-fledged styles library such as Bootstrap or Material UI. Not going is a choice, though.

There is tooling for linting,  `eslint` with some recommended rules by default. You may add `prettier` or enforce styles manually. There are also testing tools: `jest` provides a test runner, an assertion API and a mocking API; `@testing-library/react` provides some testing utilities, but you may find the need to reach for `enzyme`.  There's no end-to-end tooling in the kit, you will have to choose between `playwright` (headless browser runner) or `cypress` (in-browser test runner) or both.

Are we done? Well, React itself offers class-based components with life cycle methods or function-based components with hooks. And there is state management (`redux`) and client-side routing (`react-router`), both optional. Oh, keep in mind that CRA hints at file organization (tests, styles and components in the same folder) but does not enforce it. Following it is a choice too.

To sum up, here's a numbered list of choices:

1. Framework?
2. Package Manager?
3. Starter kit?
4. Bundler?
5. JS Backwards compatibility?
6. Typescript?
7. CSS-in-JS?
8. Pre or Post processing CSS?
9. CSS Reset or Normalize?
10. Style libraries?
11. Code linting?
12. Code formatting?
13. Test runner?
14. Asserting library?
15. Mocking library?
16. Testing utilities?
17. End-to-end (E2E) test runner?
18. Class-based or function based components?
19. State management?
20. Client-side routing?
21. Codebase organization?

Ask a new developer to start a new project and you're bound to see `?????????????????????` above his head. That's why.
