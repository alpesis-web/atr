Feb 4 2014 | MongoDB, python, development, blog | Kelly Chan
# MongoDB for Developers

MongoDB: [course](https://education.mongodb.com/courses/10gen/M101P/2014_February/about)  

Table of Contents
- Week 1. Introduction
- Week 2.
- Week 3.
- Week 4.
- Week 5.
- Week 6.
- Week 7.

## Week 1. Introduction
MongoDB: JSON {key: value}, document-oriented, schemaless  
(functionality) RDBMS  \-\-\-\- (functionality, scalability) MongoDB \-\-\-\- (scalability) memcached, key value store 

### 1. Framework of building an app with MongoDB

Mongo Shell --> Mongo D <---> (Http: python - bottle/pymongo) <--> users

Mongo Shell
```
mongo
MongoDB shell version: 2.2.0
connecting to: test

use test
db.things.save({a:1, b:2, c:3}) 
db.things.find()
db.things.save({a:3, b:4, c:6, d:200}) 
db.things.find()
db.things.find({a:1})

db.things.save({a:1, b:2, fruit:['apple','orange','pear']})
db.things.save({name: "andrew", address: {street: "elm drive", city:"Polo Alto"}})
db.things.find().pretty()
```

### 2. Installing MongoDB

installing MongoDB, python, bottle.py (python web framework), PyMongo

(MongoDB) Mongo Shell
```
show dbs
db.mycollection.insert({hello: "world"})
db.mycollection.find()
exit

dir \data\db
mongod --help
```

(Python/PyMongo) Python Script
```
from pymongo import MongoClient

# connect to database
connection = MongoClient("localhost", 27017)
db = connection.test

names = db.names
item = names.find_one()
print item['name']
```

### 3. Web Application
mongod <- (BSON) -> [App] Python (pymongo/bottle) <- (http) -> web page  

Python Script
```
import bottle
import pymongo

# this is the handler for the default path of the web server

@bottle.route('/')
def index():
    
    # connect to mongoDB
    connection = pymongo.MongoClient('localhost', 27017)
    
    # attach to test database
    db = connection.test
    
    # get handle for names collection
    name = db.names
    
    # find a single document
    item = name.find_one()
    
    return '<b>Hello %s!</b>' % item['name']

bottle.run(host='localhost', port = 8082)
```

### 4. JSON

JSON revisited: 
- array []: lists of thing 
- dictionary {key: value}: associate maps
```
{"fruit": ['apple','pear','peach']}
```

### 5. Schema Design with MongoDB
embeded? 16MB document limit   

### Case Study: Blog

blog in relational tables
```
authors:
	author_id,
	name,
	email,
	password

posts:
	post_id,
	author_id
	title,
	body,	
	publication_date

comments:
	comment_id,
	name, 
	email,
	comment_text

post_comments:
	post_id,
	comment_id

tags
	tag_id
	name

post_tags
	post_id
	tag_id
```

blog in document
```
posts
{
 title: "Free online class", 
 body: "...", 
 author: "someone",
 date: "...",
 comments: [{
             name: "xxx",
             email: "...",
             comment: "..."
             }],
 tags: ["education", "startups", "cycling"]
}
 
authors
{
 _id: "xxxx",
 password: "xxxx"
}

```

### 6. Bottle Framework

web browser -> HTML -> (IP->TCL(80)->http) -> python/bottle

python script
```
import bottle

@bottle.route('/')
def home_page():
    return "Hello World\n"

@bottle.route('/testpage')
def test_page():
    return "This is a test page."

bottle.debug(True)
bottle.run(host='localhost', port=8080)
```

MVC (Model View Controller)  
model --(update)----> view       <-(see)- users
      <-(manipulate)- controller <-(see)-

- view/template: handling users see  
- controller/post: handling users input  

model.py  

```

import bottle

@bottle.route('/')
def home_page():
    mythings = ['apple','orange','peach']
    return bottle.template('Hello world', username='Andrew', things=mythings)

@bottle.post('/favoriate_fruit')
def favoriate_fruit():
    fruit = bottle.request.forms.get("fruit")
    if (fruit == None or fruit == ""):
        fruit = "No fruit selected."
        
    #return bottle.template('fruit_selection.tpl', {'fruit': fruit})
    # set cookies
    bottle.response.set_cookie("fruit", fruit)
    bottle.redirect("/show_fruit")

@bottle.route('/show_fruit')
def show_fruit():
    fruit = bottle.request.get_cookie("fruit")
    return bottle.template('fruit_selection.tpl', {'fruit': fruit})

bottle.debug(True)
bottle.run(host='localhost', port=8080)

```

view.html
```
<!DOCTYPE html>
<html>
<head>
    <title>Hello World</title>
</head>

<body>
    <p>Welcome {{username}}</p>
    <ul>
        %for thing in things:
            <li>{{thing}}</li>
        %end
    </ul>
    
    <form action="/favorite_fruit" method="POST">
        What if your favorite fruit?
        <input type="text" name="fruit" size="40" value=""><br>
        <input type="submit" value="Sumbit">
    </form>
</body>
</html>

```

fruit_selection.tpl  

```
<!DOCTYPE html>
<html>
<head>
    <title>Fruit Selection Confirmation</title>
</head>

<body>
    <p>
    <p>
    Your favorite fruit is {{fruit}}
</body>
</html>
```


Mongo exception processing  


This one doesn't work.
```
import sys
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.test
users = db.users

doc = {'firstname': 'Andrew', 'lastname': 'Erlichson'}
print doc
print "about to insert the document"

try:
    users.insert(doc)
except:
    print "insert failed:", sys.exc_info()[0]

print doc
print "inserting again"
```

This one works well.
```
import sys
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.test
users = db.users

doc = {'firstname': 'Andrew', 'lastname': 'Erlichson'}
print doc
print "about to insert the document"

try:
    users.insert(doc)
except:
    print "insert failed:", sys.exc_info()[0]

print doc



doc = {'firstname': 'Andrew', 'lastname': 'Erlichson'}
print doc
print "about to insert the document"

try:
    users.insert(doc)
except:
    print "insert failed:", sys.exc_info()[0]

print doc
print "inserting again"

```
