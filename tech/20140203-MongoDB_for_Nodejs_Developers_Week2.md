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

### 1. Insert

```
doc = {"name": "smith", "age": 30, "profession": "hacker"}
db
db.people.insert(doc)
db.people.find()

db.people.insert({"name": "jones", "age": 35, "profession": "baker"})
db.people.find()
```

### 2. Find

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

### 3. Update

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

### 4. Remove

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
```
