Jan 19 2014 | Vim, Python, IDE | Kelly Chan
# Vim As A Python IDE

### 1. plugins
To download the plugins(*.vim), and then copy them to the vim folders - plugin, ftplugin, doc, syntax, autoload
- omni-completion
- Pydiction
- TagList
- WinManager
- Cscope
- MiniBufExplorer
- Grep
- NERD_tree

### 2. vimrc
To open _vimrc, set up the plugins and other configurations  
    1. open vimrc  
```
    :e $vim/_vimrc 
```
    
    2. basic settings  
    
```
    " fileencodings  
    "set fileencodings=utf-8,cp936,big5,euc-jp,euc-kr,latin1,ucs-bom  
    set fileencodings=utf-8,gbk  
    set ambiwidth=double 
    
    "ColorScheme
    colorscheme desert
    
    "Syntax
    syntax enable
    syntax on
    
    " tab for delete  
    set smartindent  
    set smarttab  
    set expandtab  
    set tabstop=4  
    set softtabstop=4  
    set shiftwidth=4  
    set backspace=2
    set textwidth=79
    
    " mouse 
    set mouse=a
    
    " row # 
    set nu 
```


### 3. testing

to open QuickFix
```
:cope
```
