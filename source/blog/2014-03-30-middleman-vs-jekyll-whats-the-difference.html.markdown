---
title: "Middleman vs Jekyll: what's the difference?"
date: 2014-03-30
tags: dev
---

When I went shopping for static generators, [Jekyll][1] was the first one I took
for a test drive. It's been a while, though, and I can't remember why I chose
[Middleman][2] over Jekyll. But a freelance gig showed up for working with Jekyl,
so I'm bound to remember now.

Jekyll uses YAML for configuration, whereas Middleman uses plain Ruby. It is
therefore easier to break your project when configuring Middleman, since you can
introduce syntax errors and the like. The default config is damn clean in
Jekyll, although Middleman is very well documented and presents lots of useful
settings and its default files.

Now Jekyll doesn't come even close to the diversity of formats supported by
Middleman. Out of the box, Jekyll supports Markdown and Textile, with YAML
support for data and Liquid templating for everything else. Middleman has [an
extensive list of suported processors][3] and the file extensions are used to
declare the processors to be used -- and you can even combine processors! But
for most users, this just means using Sass and Haml out of the box.

Middleman is designed to be extended and as such it has a handy [extension
directory][4], including [Blogging][5] and [Syntax Highlighting][6] extensions
which are already bundled in Jekyll. It also has an officially supported
[Livereload extension][7] and a very useful [community extension for automating
deploys][8]. [Jekyll's extensions][9] are just snippets referenced in the
documentation -- I guess that's why [the most popular Jekyll plugin][10] uses
Rake to generate new user with a syntax like `rake 'new_post["this is article
title"]'`, way uglier than Middleman Blog's `middleman article "this is article
title"`.

[1]:  http://jekyllrb.com/
[2]:  http://middlemanapp.com/
[3]:  http://middlemanapp.com/basics/templates/#other-templating-languages
[4]:  http://directory.middlemanapp.com/
[5]:  https://github.com/middleman/middleman-blog
[6]:  https://github.com/middleman/middleman-syntax
[7]:  https://github.com/middleman/middleman-livereload
[8]:  https://github.com/tvaughan/middleman-deploy
[9]:  http://jekyllrb.com/docs/plugins/#available_plugins
[10]: http://octopress.org/
