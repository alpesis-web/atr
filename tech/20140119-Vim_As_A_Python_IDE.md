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
- open vimrc  
```
:e $vim/_vimrc 
```
    
- basic settings  
    
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
    
" row number
set nu 
```

- plugins settings

```
"==================================================================
" omni-completion
"==================================================================

"自动补全  
filetype plugin indent on
set completeopt=longest,menu

"自动补全命令时候使用菜单式匹配列表  
set wildmenu
autocmd FileType ruby,eruby set omnifunc=rubycomplete#Complete
autocmd FileType python set omnifunc=pythoncomplete#Complete
autocmd FileType javascript set omnifunc=javascriptcomplete#CompleteJS
autocmd FileType html set omnifunc=htmlcomplete#CompleteTags
autocmd FileType css set omnifunc=csscomplete#CompleteCSS
autocmd FileType xml set omnifunc=xmlcomplete#CompleteTags
autocmd FileType java set omnifunc=javacomplete#Complet


"==================================================================
" Pydiction
"==================================================================

let g:pydiction_location = 'E:\development\Vim\vim74\ftplugin\complete-dict'


"==================================================================
" TagList
"==================================================================

let Tlist_Show_One_File=1
let Tlist_Exit_OnlyWindow=1

"==================================================================
" WinManager
"==================================================================

let g:winManagerWindowLayout='FileExplorer|TagList'
map wm :WMToggle<cr>

"==================================================================
" Cscope
"==================================================================

"cscope show in quickfix
set cscopequickfix=s-,c-,d-,i-,t-,e-

"==================================================================
" MiniBufExplorer
"==================================================================

let g:miniBufExplMapWindowNavVim = 1 
let g:miniBufExplMapWindowNavArrows = 1 
let g:miniBufExplMapCTabSwitchBufs = 1 
let g:miniBufExplModSelTarget = 1

"==================================================================
" Grep
"==================================================================

nnoremap <silent> <F3> :Grep<CR>

"==================================================================
" NERD_tree
"==================================================================

map <F2> :NERDTreeToggle<CR>  

```

- python settings

### 3. testing

to open QuickFix
```
:cope
```
