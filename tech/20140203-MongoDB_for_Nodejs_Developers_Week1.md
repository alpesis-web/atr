Feb 3 2014 | MongoDB, database, node.js | Kelly Chan
# MongoDB for Node.js Developers

MongoDB: [course](https://education.mongodb.com/courses/10gen/M101JS/2014_March/about)

Table of Contents
- Week 1: [Introduction](https://github.com/KellyChan/notebook/blob/master/tech/20140203-MongoDB_for_Nodejs_Developers_Week1.md)
- Week 2: [CRUD](https://github.com/KellyChan/notebook/blob/master/tech/20140203-MongoDB_for_Nodejs_Developers_Week2.md)
- Week 3: Schema Design
- Week 4: Performance
- Week 5: 
- Week 6:

## Week 1: Introduction

MongoDB: non relational database, documentation-oriented, store JSON documents, schemaless  
- features omitted to retain scalability: joins, transactions across multiple collections  

JSON: {key: value}
Node.js: written by C++, run by V8 javascript 

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

npm: package manager for Node.js  
packages: express(web framework), consolidate, mongodb
```
npm install express
npm install consolidate
npm install Swig
package.json
npm install
```

App with MongoDB
(App) Node.js/driver <--(BSON)--> Mongod

### Case Study: Hello World

```
var http = require('http');

var server = http.createServer(function (request, response){
        response.writeHead(200, {"Content-Type": "text/plain"});
        response.end("Hello, world!\n");
}

server.listen(8000);

console.log("Server running at http://localhost:8000");
```
calling the function
```
node app.js
```

using express
```
var express = require('express'),
    app = express();

app.get('/', function(req, res){
        res.send("Hello World!");
});

app.get('*', function(req, res){
        res.send("Page not found", 404);
});

app.listen(8080);
console.log("Express server started on port 8080");
```
using express and swig
```
var express = require('express'),
    app = express(),
    cons = require('consolidate');

app.engine('html', cons.swig);
app.set('view engine', 'html');
app.set('views', __dirname + "/views");


app.get('/', function(req, res){
        res.render('hello', {'name': 'Swig'});
});

app.get('*', function(req, res){
        res.send("Page not found", 404);
});

app.listen(8080);
console.log("Express server started on port 8080");
```

view.html
```
<h1>Hello, {{name}}!</h1>
```

using express, swig and MongoDB
```
var express = require('express'),
    app = express(),
    cons = require('consolidate'),
    MongoClient = require('mongodb').MongoClient,
    Server = require('mongodb').Server;

app.engine('html', cons.swig);
app.set('view engine', 'html');
app.set('views', __dirname + "/views");


var mongoclient = new MongoClient(new Server('localhost', 27017,
                                              {'native_parser': true}));
var db = mongoclient.db('course');

app.get('/', function(req, res){
        db.collection('hello_mongo_express').findOne({}, function(err, doc){
                res.render('hello', doc);
        });
});

app.get('*', function(req, res){
        res.send("Page not found", 404);
});

mongoclient.open(function(err, mongoclient){

    if (err) throw err;
    
    app.listen(8080);
    console.log("Express server started on port 8080");
});
```
### 6. Express (web framework)
Express: Handling GET requests
- url: parameters
- get: variables

```
var express = require('express'),
    app = express(), // web framework to handle routing requests
    cons = require('consolidate'); // templating library adapter for Express
    
app.engine('html', cons.swig);
app.set('view engine', 'html');
app.set('views', __dirname + '/views');
app.use(app.rounter);

// handler for internal server errors
function errorHandler(err, req, res, next){
    console.error(err.message);
    console.error(err.stack);
    res.status(500);
    res.render('error_template', {error: err});
}

app.use(errorHandler);

app.get('/:name', function(req, res, next){
    var name = req.params.name;
    var getvar1 = req.query.getvar1;
    var getvar2 = req.query.getvar2;
    res.render('hello', {name: name, getvar1: getvar1, getvar2: getvar2});
});

app.listen(3000);
console.log('Express server listening on port 3000');
```
view.html
```
<h1>Hello, {{name}}, here are your GET variables:</h1>
<ul>
    <li>{{getvar1}}</li>
    <li>{{getvar2}}</li>
</ul>
```

Express: handling POST requests

```
var express = require('express'),
    app = express(), // web framework to handle routing requests
    cons = require('consolidate'); // templating library adapter for Express
    
app.engine('html', cons.swig);
app.set('view engine', 'html');
app.set('views', __dirname + '/views');
app.use(express.bodyParser());
app.use(app.rounter);

// handler for internal server errors
function errorHandler(err, req, res, next){
    console.error(err.message);
    console.error(err.stack);
    res.status(500);
    res.render('error_template', {error: err});
}

app.use(errorHandler);

app.get('/', function(req, res, next){
        res.render('fruitPicker', {fruits: ['apple','orange','banana', 'peach']});
});

app.post('/favorite_fruit', function(req, res, next){
        var favorite = req.body.fruit;
        if (typeof favorite == 'undefined'){
                next(Error('Please choose a fruit!'));
        }else{
                res.send("Your favorite fruit is " + favorite);
        }
});

app.listen(3000);
console.log('Express server listening on port 3000');
```
view.html
```
<html>
    <head><title>Fruit Picker</title></head>
    <body>
        <form action="/favorite_fruit" method="POST">
            <p>What is your favorite fruit?</p>
            {% for fruit in fruits %}
                <p>
                    <input type="radio" name="fruit" value="{{fruit}}">{{fruit}}</input>
                </p>
            {% end for %}
        </form>
    </body>
</html><!DOCTYPE html>
```
