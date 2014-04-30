Apr 30 2014 | programming, python | Kelly Chan
# Object Oriented Programming

table of contents
- Introduction
- Functions
- Draw Turtles
- Send Text
- Profanity Editor
- Movie Website
- Advance Topics

## Introduction

- if
- loop
- function


## Functions

python standard libraries
```python

webbrowser
    def open

time
    def sleep
    def ctime

os
    def rename
    def chdir
    def getcwd
```

take a break
```
import time
import webbrowser

total_break = 3
break_count = 0

print("This program started on" + time.ctime())
while (break_count < total_break):
    time.sleep(10)
    webbrowser.open(url)
    break_count += 1
```

rename files
```python
import os

def rename_files():
    
    file_list = os.listdir(r"C:\oop\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is " + saved_path)
    os.chdir(r"C:\oop\prank")
    for file_name inn file_list:
        print("Old name is " + file_name)
        print("new name is " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789")
    os.chdir(saved_path)
```

## Draw Turtles
## Send Text
## Profanity Editor
## Movie Website
## Advance Topics

---
### References
1. [The Python Standard Library](https://docs.python.org/2.7/library/)
