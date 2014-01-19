Jan 19 2014 | Vim, Python, IDE | Kelly Chan
# My First Vim Python IDE

### 1. plugins
To download the plugins(*.vim), and then copy them to the vim folders - <b>plugin, ftplugin, doc, syntax, autoload</b>
- [omni-completion](http://www.vim.org/scripts/script.php?script_id=1542)
- [Pydiction](http://www.vim.org/scripts/script.php?script_id=850)
- [TagList](http://www.vim.org/scripts/script.php?script_id=273)
- [WinManager](http://www.vim.org/scripts/script.php?script_id=95)
- [Cscope](http://cscope.sourceforge.net/cscope_maps.vim)
- [MiniBufExplorer](http://www.vim.org/scripts/script.php?script_id=159)
- [Grep](http://www.vim.org/scripts/script.php?script_id=311)
- [NERD_tree](http://www.vim.org/scripts/script.php?script_id=1658) 
- [Python_fold](http://www.vim.org/scripts/script.php?script_id=515)

### 2. vimrc
To open _vimrc, set up the plugins and other configurations  
- open vimrc  

```
:e $vim/_vimrc
```

    
- basic settings  
    

```
" 设置编码自动识别, 中文引号显示  
"set fileencodings=utf-8,cp936,big5,euc-jp,euc-kr,latin1,ucs-bom  
set fileencodings=utf-8,gbk  
set ambiwidth=double 


"ColorScheme
colorscheme desert

"Syntax
syntax enable
syntax on

" 允许退格键删除和tab操作  
set smartindent  
set smarttab  
set expandtab  
set tabstop=4  
set softtabstop=4  
set shiftwidth=4  
set backspace=2
set textwidth=79

" 启用鼠标  
set mouse=a

" 启用行号  
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


```
"python_fold
set foldmethod=indent "设置折叠方式  


"python run
"
if has("autocmd")

  " 自动检测文件类型并加载相应的设置
  filetype plugin indent on

  " Python 文件的一般设置，比如不要 tab 等
  autocmd FileType python setlocal et | setlocal sta | setlocal sw=4

  " Python Unittest 的一些设置
  " 可以让我们在编写 Python 代码及 unittest 测试时不需要离开 vim
  " 键入 :make 或者点击 gvim 工具条上的 make 按钮就自动执行测试用例
  autocmd FileType python compiler pyunit
  autocmd FileType python setlocal makeprg=\"E:\\development\\Python\\python.exe\"\ ./alltests.py
  autocmd BufNewFile,BufRead test*.py setlocal makeprg=\"E:\\development\\Python\\python.exe\"\ %

endif
```


### 3. Compiling Python Script

to run program
```
:make
```

to open QuickFix
```
:cope
```

to open nerdtree
```
F2
```

to open taglist
```
wm
```
