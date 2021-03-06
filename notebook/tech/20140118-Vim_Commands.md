Jan 18 2014 | Vim | Kelly Chan
# Vim Commands

1. Basic: edit, move, copy/paste/change, search/find/replace, file open/save
2. Advance: customization, extensions

## 1. Basic

### Normal Mode 
1. edit  
    - to insert: `i` 
    - to delete: `x`
    - to exit: `esc`

2. move  
    - to move: `hjkl`, h - left, l - right, j - down, k - up
    - (move) back word: `b`
    - (move) next word: `w`
    - (move) end of line: `$`
    - (move) page up/down: `ctrl + u/d`
    - (move) top of the file: `gg`

3. copy, paste, change   
    - to yank/copy: `y(xxx)`
    - (yank) current line: `yy`
    - to paste: `p`
    - to change: `c`
    - (change) word: `cw`

4. search, find, replace  
    - to search: `/(words)`
    - (search) top/end: `#` to top, `*` to end
    - to find: `f(a letter)`
    - (find) former/next: `,` for former, `;` to next
    - to replace: `:%s/(word to be replaced)/(word replaced)/g`, g for global

5. coding </>
    - shift: `:line,line<` or `:line,line>`

### Command Mode 
- to write/save: `:w file_path`  
- to open file: `:e file_path`

---

## 2. Customization and Extensions
Plugins:  
- MiniBufExplorer
- Python_fold


### MiniBufExplorer
to list all buffers: `:ls`  
to open the nth buffer file: `:b<n>`  
to close the buffer file: `:bd`  


### Python_fold
fold: `zc`  
unfold: single - `zo`, all - `zr`
