Mar 7 2014 | emacs, IDE | Kelly Chan
# Emacs as A Python IDE

## 1. Installation

- 1. download [Emacs](http://ftp.gnu.org/gnu/emacs/windows/)
- 2. unzip Emacs to a folder
- 3. plugins and settings: folders `home/.emacs.d`, settings `.emacs`

folder structure:
```
-- home
    |---- .emacs
    |---- [.emacs.d]
            |------ [plugins]
            |------ [settings] (settings in .emacs)
```

## 2. Plugins and Settings

plugins
- [ido](http://www.emacswiki.org/emacs/InteractivelyDoThings)
- [auto-complete](http://www.emacswiki.org/emacs/AutoComplete)
- [python-mode](https://launchpad.net/python-mode)

### 1. ido-mode

commands:  
- `M-x ido-mode`: enable ido-mode
- `C-x b`: switch between buffers

.emacs settings
```lisp
(require 'ido)
(ido-mode t)
```

### 2. auto-complete

commands:  
install: cd to the folder, cmd:`emacs -batch -l etc/install.el`  

.emacs settings
```lisp
(add-to-list 'load-path "~/.emacs.d/auto-complete-1.3.1")
(require 'auto-complete)
(add-to-list 'ac-dictionary-directories "~/.emacs.d/ac-dict")
(require 'auto-complete-config)
(ac-config-default)
(global-auto-complete-mode t)
```

### 3. python-mode

installation:
- download and copy the folder to `~/emacs.d/plugins/python-mode`

commands:
- `M-x locate-library RET` and `python-mode RET`: check if install

.emacs settings
```lisp
(setq py-install-directory "~/.emacs.d/plugins/python-mode")
(add-to-list 'load-path py-install-directory)
(require 'python-mode)
```

## 3. Programming

manage files
- `C-x C-f`: open file
- `C-x C-s`: save file
- `C-x C-w`: save file as
- `C-x b`: switch buffers

edit files
- `M-w`: copy
- `C-y`: paste
- `tab`: 4 spaces

run python scripts
- `C-c C-p`: open python interpreter
- `C-c C-c`: run script
- `M-x shell RET`: go to python shell, `python xx.py`, to run script


---
### References
1. [Emacs as A Python IDE](http://www.jesshamrick.com/2012/09/18/emacs-as-a-python-ide/)
