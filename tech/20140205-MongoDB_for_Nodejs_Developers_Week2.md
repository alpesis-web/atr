Feb 5 2014 | MongoDB, database, node.js | Kelly Chan
# MongoDB for Node.js Developers

MongoDB: [course](https://education.mongodb.com/courses/10gen/M101JS/2014_March/about)

Table of Contents
- Week 1: [Introduction](https://github.com/KellyChan/notebook/blob/master/tech/20140203-MongoDB_for_Nodejs_Developers_Week1.md)
- Week 2: [CRUD](https://github.com/KellyChan/notebook/blob/master/tech/20140205-MongoDB_for_Nodejs_Developers_Week2.md)
- Week 3: Schema Design
- Week 4: Performance
- Week 5: 
- Week 6:

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
db.scores.count({type: "exam"})
```
### 3. Update
### 4. Remove
