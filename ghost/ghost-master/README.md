Ghost-Master
=============================

## Introduction

Ghost-Master is combined ghost (the original blogging engine developed by node.js), buster (a python package to generate the static pages from Ghost), and deploy (the configuration files to deploy on the production environment - here is Ubuntu 12.04).

main folders:

- `ghost/`: the source codes of the blogging engine
- `buster/`: the library to generate the static pages
- `deploy/`: the deployment files

docs:

- AUTHOR.md: author
- LICENSE.md: license
- README.md: readme

Additionally, we developed some customed themes to apply on various scenarios.

- [ghost-theme-atr-platform](https://github.com/KellyChan/ghost-theme-atr-platform)
- [ghost-theme-libre](https://github.com/KellyChan/ghost-theme-libre)


## Customized Themes

To change a theme, 

    $ cd ghost/content/themes
    $ git clone theme_repo

And then open http://localhost:2368/admin, click `General`, to change a theme.


## LICENSE

[MIT LICENSE](LICENSE.md)
