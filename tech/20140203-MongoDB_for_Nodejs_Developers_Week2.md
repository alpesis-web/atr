# MongoDB for Node.js Developers

MongoDB: [course](https://education.mongodb.com/courses/10gen/M101JS/2014_March/about)

Table of Contents
- Week 1: [Introduction](https://github.com/KellyChan/notebook/blob/master/tech/20140203-MongoDB_for_Nodejs_Developers_Week1.md)
- Week 2: [CRUD](https://github.com/KellyChan/notebook/blob/master/tech/20140203-MongoDB_for_Nodejs_Developers_Week2.md)
- Week 3: [Schema Design](https://github.com/KellyChan/notebook/blob/master/tech/20140203-MongoDB_for_Nodejs_Developers_Week3.md)
- Week 4: [Performance](https://github.com/KellyChan/notebook/blob/master/tech/20140203-MongoDB_for_Nodejs_Developers_Week4.md)
- Week 5: [t](https://github.com/KellyChan/notebook/blob/master/tech/20140203-MongoDB_for_Nodejs_Developers_Week5.md)
- Week 6: [t](https://github.com/KellyChan/notebook/blob/master/tech/20140203-MongoDB_for_Nodejs_Developers_Week6.md)

---
Feb 5 2014 | MongoDB, database, node.js | Kelly Chan
## Week 2: CRUD
| CRUD   | MongoDB | SQL    |
|:-------|:--------|:-------|
| Create | insert  | insert |
| Read   | find    | select |
| Update | update  | update |
| Delete | remove  | delete |

BSON supports
- string
- float
- array
- object
- timestamp

### Part 1. MongoDB: CRUD

#### 1. Insert

```
doc = {"name": "smith", "age": 30, "profession": "hacker"}
db
db.people.insert(doc)
db.people.find()

db.people.insert({"name": "jones", "age": 35, "profession": "baker"})
db.people.find()
```

#### 2. Find

findOne()
```
db.people.findOne()
db.people.findOne({"name": "jones"})
db.people.findOne({"name": "jones"}, {"name": true})
db.people.findOne({"name": "jones"}, {"name": true, "_id": false})
```
find()
```
db.stores.find()
db.stores.find().pretty()
it
```
querying: selection
```
db.scores.find({student: 19});
db.scores.find({student: 19, type: "essay"});
db.scores.find({student: 19, type: "essay"}, {"score": true});
db.scores.find({student: 19, type: "essay"}, {"score": true, "_id": false});
```
querying: $gt and $lt
```
db.scores.find({score: {$gt: 95}})
db.scores.find({score: {$gt: 95}, type: "essay"})
db.scores.find({score: {$gt: 95, $lt: 98}, type: "essay"})

db.scores.find({score: {$gte: 50 , $lte: 60}});
```
inequalities: strings
```
db.people.find({name: {$lt: "D"}});
db.people.find({name: {$lt: "D", $gt: "B"}});
```
$exists, $type, $regex
```
db.people.find({profession: {$exists: true}});
db.people.find({profession: {$exists: false}});

db.people.find({name: {$type: 2}});

db.people.find({name: {$regex: "a"}});
db.people.find({name: {$regex: "e$"}});
db.people.find({name: {$regex: "^A"}});
```
$or, $and
```
db.people.find({$or: [{name: {$regex: "e$"}}, {age: {$exists: true}}]});
db.people.find({$and: [{name: {$gt: "C"}}, {name: {$regex: "a"}}]});
db.people.find({name: {$gt: "C", $regex: "a"}});
```
$in, $all
```
db.accounts.find({favorite: { $all: ["pretzels","beer"]}});
db.accounts.find({name: {$in: ["howard","john"]}});
db.accounts.find({favorite: { $in: ["beer", "icecream"]}});
```
querying: dot notation
```
db.users.find({email: {work: "richard@10gen.com"}});
db.users.find({"email.word": "richard@10gen.com"});
```
cursors
```
cur = db.people.find(); null;
cur.hasNext();
cur.next();
cur.next();
cur.next();
```
a query that retrieves exam documents, sorted by score in descending order, skipping the first 50 and showing only the next 20
```
db.scores.find({type: "exam"}).sort({score: -1}).skip(50).limit(20);
```
counting
```
db.scores.count({type: "exam"});
db.scores.count({type: "essay", score:{$gt: 90}});
```

#### 3. Update

```
db.people.update({ name: "Smith"}, {name: "Thompson", salary: 50000});
```
$set, $unset, $inc
```
db.people.update({ name: "Alice"}, { $set: { age: 30 }});
db.people.update({ name: "Alice"}, { $inc: { age: 1 }});
db.people.update({ name: "Jones"}, { $unset: {profession: 1}});
```
$push, $pop, $pull, $pushAll, $pullAll, $addToSet
```
db.arrays.insert({ _id: 0, a: [1,2,3,4] });
db.arrays.findOne()

db.arrays.update({ _id: 0}, { $set: { "a.2": 5} });
db.arrays.findOne()

db.arrays.update({ _id: 0}, { $push: { a: 6} });
db.arrays.findOne()

db.arrays.update({ _id: 0}, { $pop: { a: 1} });
db.arrays.findOne()

db.arrays.update({ _id: 0}, { $pop: { a: -1} });
db.arrays.findOne()

db.arrays.update({ _id: 0}, { $pushAll: { a: [7,8,9] } });
db.arrays.findOne()

db.arrays.update({ _id: 0}, { $pull: { a: 5 } });
db.arrays.findOne()

db.arrays.update({ _id: 0}, { $pullAll: { a: [2,4,8] } });
db.arrays.findOne()

db.arrays.update({ _id: 0}, { $addToSet: { a: 5 } });
db.arrays.update({ _id: 0}, { $addToSet: { a: 5 } });
db.arrays.findOne()
```
upsert
```
db.people.update( {name: "George"}, { $set: {age: 40}}, { upsert: true} );
db.people.update( {age: { $gt: 50}}, { $set: { name: "William"}}, { upsert: true} );
```
multi-update
```
db.people.update( {}, { $set : { title: "Dr" }, { multi: true } })
db.scores.update({score: {$lt: 70}}, {$inc: {score: 20}}, {multi: true})
```

#### 4. Remove

```
db.people.remove({ name: "Alice"})
db.people.remove({ name: { $gt: "M"} })

db.people.remove()
db.people.drop()
```

getLastError
```
db.people.insert({ _id: "Smith", age: 30});
db.people.insert({ _id: "Smith", age: 30});
db.runCommand({ getLastError: 1 })

db.people.insert({ _id: "Jones", age: 30});
db.runCommand({ getLastError: 1 })

db.people.update({}, { $set: {title: "Dr"}}, {multi: true});
db.runCommand({ getLastError: 1 })

db.people.update({name: "Thompson"}, { $set: {title: "Dr"}}, {upsert: true});
db.runCommand({ getLastError: 1 })

db.people.remove()
db.runCommand({ getLastError: 1 })
```

### Part 2. Node.js Driver: CRUD

mongo -(BSON)-> mongod <-(BSON)- driver/node.js/code  

Node.js driver & CRUD  

#### 1. Insert

insert
```
var MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/course', function(err, db){
    if (err) throw err;
    
    //var doc = { 'student': 'Calvin', 'age': 6 };
    var docs = [{ 'student' : 'Calvin', 'age' : 6},
                { 'student' : 'Sussie', 'age' : 7}];
    
    db.collection('students').insert(docs, function(err, inserted){
        if (err) throw err;
        
        console.dir("Successfully inserted!" + JSON.stringify(inserted));
        return db.close();
    });
});
```

import reddit

```
var MongoClient = require('mondodb').MongoClient,
    request = require('request');

MongoClient.connect('mongodb://localhost:27017/course', function(err, db){
    if (err) throw err;
    
    request('http://www.reddit.com/r/techonology/.json', function(error, response, body){
        if (!error && response.statusCode == 200){
            var obj = JSON.parse(body);
            
            var stories = obj.data.children.map(function (story){return story.data;});
            
            db.connection('reddit').insert(stories, function(err, data){
                if (err) throw err;
                
                console.dir(data);
                
                db.close();
            });
        }
        
    });
});

```

#### 2. Find
import data

```
mongoimport -d course -c grades grades.json
mongo
use course
db.grades.find()
```

findOne

```
var MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/course', function(err, db){
    if (err) throw err;
    
    var query = { 'grade' : 100 };
    
    db.collection('grades').findOne(query, function(err, doc){
        if (err) throw err;
        
        console.dir(doc);
        db.close();
    });
});

```

find

```
var MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/course', function(err, db){
    if (err) throw err;
    
    var query = { 'grade' : 100 };
    
    db.collection('grades').find(query).toArray(function(err,docs){
        if (err) throw err;
        
        console.dir(docs);
        db.close();
    });
});

```

cursor(.each/.toArray) <--> mongod

```
var MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/course', function(err, db){
    if (err) throw err;
    
    var query = { 'grade' : 100 };
    var cursor = db.collection('grades').find(query);
    
    cursor.each(function(err, doc){
        if (err) throw err;
        
        if (doc == null){
            return db.close();
        }
        console.dir(doc.student + " got  a good grade!" ); 
    });
});

```

field projection
```
var MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/course', function(err, db){
    if (err) throw err;
    
    var query = { 'grade' : 100 };
    var projection = { 'student': 1, '_id': 0 };
    
    db.collection('grades').find(query, projection).toArray(function(err, docs){
        if (err) throw err;
        
        docs.forEach(function (doc){
            console.dir(doc);
            console.dir(doc.student + " got a good grade!");
        });
        
        db.close();
    });
});
```

$gt, $lt
```
var MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/course', function(err, db){
    if (err) throw err;
    
    var query = { 'student':'Jones', 'grade': {$gt: 80, $lt: 95} };
    
    db.collection('grades').find(query).each(function(err, docs){
        if (err) throw err;
        
        if (doc == null){
            db.close();
        }
        
        console.dir(doc);
    });
});
```

$regex
```
var MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/course', function(err, db){
    if (err) throw err;
    
    var query = { 'title' : { '$regex' : 'NSA' } };
    var projection = { 'title' : 1, '_id' : 0};
    
    db.collection('reddit').find(query, projection).each(function(err, docs){
        if (err) throw err;
        
        if (doc == null){
            db.close();
        }
        
        console.dir(doc.title);
    });
});
```

dot notation
```
var MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/course', function(err, db){
    if (err) throw err;
    
    var query = { 'media.oembed.type' : 'video' };
    var projection = { 'media.oembed.url' : 1, '_id' : 0};
    
    db.collection('reddit_front').find(query, projection).each(function(err, docs){
        if (err) throw err;
        
        if (doc == null){
            db.close();
        }
        
        console.dir(doc.title);
    });
});
```

sort, skip, limit
```
var MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/course', function(err, db){
    if (err) throw err;
    
    var grades = db.connection('grades');
    
    var cursor = grades.find({});
    cursor.skip(1);
    cursor.limit(4);
    cursor.sort('grade',1);
    //cursor.sort([['grade', 1],['student',-1]]);
    
    //var options = { 'skip': 1,
    //                'limit': 4,
    //                'sort': [['grade', 1],['student',-1]] };
    //var cursor = grades.find({}, {}, options);
    
    cursor.each(function(err, doc){
        if (err) throw err;
        if (doc == null){
            return db.close();
        }
        console.dir(doc);
    });
    
});
```

#### 3. Update

replacement, in place, multi  

replace update
```
var MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/course', function(err, db){
    if (err) throw err;
    
    var query = { 'assignment' : 'hw1' };
    
    db.connection('grades').findOne(query, function(err, doc){
        if (err) throw err;
        
        if (!doc){
            console.log('No document for assignment ' + qeury.assignment + ' found!');
            return db.close();
        }
        
        query['_id'] = doc['_id'];
        doc['date_returned'] = new Date();
        
        db.collection('grades').update(query, doc, function(err, updated){
            if (err) throw err;
            
            console.dir("Successfully updated " + updated + " document!");
            
            return db.close();
        });
    });
});
```
in place update
```
var MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/course', function(err, db){
    if (err) throw err;
    
    var query = { 'assignment' : 'hw1' };
    var operator = {$set: {'date_retruned': new Date()}};
    
    db.connection('grades').update(query, operator, function(err, updated){
        if (err) throw err;
        
        console.dir("Successfully updated " + updated + " document!");
        
        retrun db.close();
    });
});
```
multi update
```
var MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/course', function(err, db){
    if (err) throw err;
    
    var query = { };
    var operator = {$set: {'date_retruned': new Date()}};
    var options = { $multi: true};
    
    db.connection('grades').update(query, operator, options, function(err, updated){
        if (err) throw err;
        
        console.dir("Successfully updated " + updated + " document!");
        
        retrun db.close();
    });
});
```

upsert and save  
upsert
```
var MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/course', function(err, db){
    if (err) throw err;
    
    var query = { 'student' : 'Frank', 'assignment': 'hw1' };
    var operator = {'student' : 'Frank', 'assignment': 'hw1', 'grade': 100};
    var options = { 'upsert': true};
    
    db.connection('grades').update(query, operator, options, function(err, updated){
        if (err) throw err;
        
        console.dir("Successfully updated " + updated + " document!");
        
        return db.close();
    });
});
```
save: upsert to insert or replace the document
```
var MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/course', function(err, db){
    if (err) throw err;
    
    var query = { 'assignment' : 'hw2' };
    
    db.connection('grades').findOne(query, function(err, doc){
        if (err) throw err;
        
        doc['date_returned'] = new Date();
        
        db.connection('grades').save(doc, function(err, saved){
            if (err) throw err;
            
            console.dir("Successfully saved " + saved + " document!");
            
            return db.close();
        });
    });
});
```

findAndModify: only modify the first document it finds, often works with sort()
```
var MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/course', function(err, db){
    if (err) throw err;
    
    var query = { 'name' : 'comments' };
    var sort = [];
    var operator = { '$inc' : {'counter': 1} };
    var options = { 'new': true};
    
    db.connection('counters').findAndModify(query, sort, operator, options, function(err, doc){
        if (err) throw err;
        
        if (!doc){
            console.log("No counter found in the comments.");
        }else{
            console.log("Number of comments: " + doc.counter);
        }
        
        return db.close();
    });
});
```

#### 4. Remove
```
var MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/course', function(err, db){
    if (err) throw err;
    
    var query = { 'assignment' : 'hw3' };
 
    db.connection('grades').remove(query, function(err, removed){
        if (err) throw err;
        
        console.dir("Successfully removed " + removed + " documents!");
        
        return db.close();
    });
});
```

### Part 3. Case Study - Blog

blog application architecture
```
app.js  
  |---- routes  
          |------ sessions.js  
          |------ posts.js  
          |------ users.js  
```
