Feb 3 2014 | MongoDB, database, node.js | Kelly Chan
# MongoDB for Node.js Developers

MongoDB: [course](https://education.mongodb.com/courses/10gen/M101JS/2014_March/about)

Table of Contents
- Week 1: [Introduction](https://github.com/KellyChan/notebook/blob/master/tech/20140203-MongoDB_for_Nodejs_Developers_Week1.md)
- Week 2: Crud
- Week 3: Schema Design
- Week 4: 
- Week 5: 
- Week 6:

## Week 1: Introduction

MongoDB: non relational database, documentation-oriented, store JSON documents, schemaless  
- features omitted to retain scalability: joins, transactions across multiple collections  

JSON: {key: value}
Node.js: written by C++, run by javascript v8

### 1. Framework of app with MongoDB
Mongo Shell -> MongoDB (C++) <--> App (node.js) <---> clients

### 2. Installing MongoDB

- download MongoDB, zip (bin) all files to another folder
- create a db folder, /data/db is a must
- open cmd, `cd` to MongoDB folder, `mongod.exe -dbpath path/data/db`, link db folder to mongoDB
- cmd: `mkdir` to create folder, `dir` to go to path, `cls` to clean the window
- cmd: `dir mongod.exe`
- cmd: `mongod --version`, or `mongod --help`
- cmd: `mongod`, to accept the access
- cmd: `mongo localhost/test`, to check the connection
- cmd: `show dbs`, or `show collections`
- cmd: `db.mycollection.insert({"Hello": "World"})`
- cmd: `db.mycollection.find()`
- cmd: `exit` or `ctrl+c` to exit

### 3. Mongo Shell

```
show dbs
use demo
db.things.find()
db.things.insert({"a": 1, "b": 2, "c": 3})

for (var i=0; i <10; i++){db.things.insert({"x":i})}
```

### 4. JSON

```
mongo

use jsonintro

db.basic.find()
db.values.find()
db.values.find().pretty()
db.deepnested.find().pretty()
db.deepnested.findOne()

course['student']
course['student'][0].name
course['student'][0].name = "Sue"
```

### 5. Node.js

Asynchronous vs Synchronous / IO

```
// find one document in our collection
var doc = db.coll.findOne();

// print the result
printjson(doc);
```
connecting MongoDB
```
var MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://127.0.0.1:27017/test', function(err, db){

    if (err) throw err;
    
    // find one docuemnt in our collection
    db.collection('coll').findOne({}, function(err, doc){
    
        // print the result
        console.dir(doc);
        
        // close the db
        db.close();
        
    });
    
    // declare success
    console.dir("Called findOne!");
    
}
```
calling the function
```
vim script.js
vim apps.js
mongo script.js
```
