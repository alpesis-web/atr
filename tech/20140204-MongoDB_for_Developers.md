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
