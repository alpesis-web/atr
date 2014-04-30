Apr 30 2014 | programming, python | Kelly Chan
# Object Oriented Programming

table of contents
- Introduction
- Functions
- Classes
    - Draw Turtles
    - Send Text
    - Profanity Editor
    - Movie Website
    - Advance Topics

## Introduction

- if
- loop
- function

python built-in functions  
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
class
```python
turtle
    def __init__
    def forward
    def right
```
external Python Library
```python
twilio
```

## Functions

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

## Classes

### Draw Turtles

draw square
```python
def draw_square():
    window = turtle.Screen()
    window.gbcolor('red')

    brad = turtle.Wartle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    brad.forward(100)
    brad.right(90)
    brad.forward(300)
    brad.right(90)
```

### Send Text
```python
from twilio.rest import TwilioRestClient

acccount_sid = ""
auth_token = ""
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body = ""
    to="" # phone number
    from_="" # twilio number
)
print message.sid
```

### Profanity Editor

```python
import urllib

def read_text():
    quotes = open("C:\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()

    if "true" in output:
        alert()
        print("Profanity Alert!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")
        
read_text()
```

### Movie Website

```python
class Movie():

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image = url_poster_image
        self.trailer_youtube_url = trailer_youtube


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        

import media

toy_story = media.Movie("Toy Story", 
                        "",
                        "", 
                        "")
print(toy_story.storyline)
```

### Inheritance

`__doc__`: show the document of a module  

inheritance / method overriding
```python
class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last name - " + self.last_name)
        print("Eye color - " + self.eye_color)
        
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Construcutor Called")
        Parent.__init__(self.last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last name - " + self.last_name)
        print("Eye color - " + self.eye_color)
        print("Number of toys - " + self.number_of_toys)   

billy_cyrus = Parent("Cyrus", "blue")
billy_cyrus = Child("Cyrus", "blue", 5)
billy_cyrus.show_info()
print(billy_cyrus.last_name)
print(billy_cyrus.number_of_toys)
```

---
### References
1. [The Python Standard Library](https://docs.python.org/2.7/library/)
2. [Python Built-in Functions](https://docs.python.org/2/library/functions.html)
3. [Google Python Style Guide](http://google-styleguide.googlecode.com/svn/trunk/pyguide.html)
4. [Twilio](http://www.twilio.com/)
5. [Twilio Github Project](https://github.com/twilio/twilio-python)
