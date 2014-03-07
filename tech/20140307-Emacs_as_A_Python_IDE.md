Mar 7 2014 | emacs, IDE | Kelly Chan
# Emacs as A Python IDE

## 1. Installation

- 1. download [Emacs](http://ftp.gnu.org/gnu/emacs/windows/)
- 2. `pip install elpy` and `pip install elpy rope jedi`

## 2. Plugins and Settings

plugins
- [ido](http://www.emacswiki.org/emacs/InteractivelyDoThings)

### 1. modes

#### (1) ido-mode

enable ido-mode: `M-x ido-mode`  
`.emacs` settings
```lisp
(require 'ido)
(ido-mode t)
```
commands:  
- `C-x b`: switch between buffers

## 3. Programming

`C-c C-c`: run script

---
### References
1. [Emacs as A Python IDE](http://www.jesshamrick.com/2012/09/18/emacs-as-a-python-ide/)
