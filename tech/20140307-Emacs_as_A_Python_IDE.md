Mar 7 2014 | emacs, IDE | Kelly Chan
# Emacs as A Python IDE

## 1. Installation

- 1. download [Emacs](http://ftp.gnu.org/gnu/emacs/windows/)
- 2. `pip install elpy` and `pip install elpy rope jedi`

## 2. Plugins and Settings

plugins
- [ido](http://www.emacswiki.org/emacs/InteractivelyDoThings)
- [auto-complete](http://www.emacswiki.org/emacs/AutoComplete)

### 1. ido-mode

`.emacs` settings
```lisp
(require 'ido)
(ido-mode t)
```
commands:  
- `M-x ido-mode`: enable ido-mode
- `C-x b`: switch between buffers

### 2. auto-complete

install: cd to the folder, cmd:`emacs -batch -l etc/install.el`
`.emacs` settings
```lisp
(add-to-list 'load-path "~/.emacs.d/auto-complete-1.3.1")
(require 'auto-complete)
(add-to-list 'ac-dictionary-directories "~/.emacs.d/ac-dict")
(require 'auto-complete-config)
(ac-config-default)
(global-auto-complete-mode t)
```

## 3. Programming

`C-c C-c`: run script

---
### References
1. [Emacs as A Python IDE](http://www.jesshamrick.com/2012/09/18/emacs-as-a-python-ide/)
