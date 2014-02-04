Feb 3 2014 | MongoDB, database, node.js | Kelly Chan
# MongoDB for Node.js Developers

MongoDB: [course](https://education.mongodb.com/courses/10gen/M101JS/2014_March/about)

Table of Contents
- Week 1: Introduction
- Week 2: Crud
- Week 3: Schema Design

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
- cmd: `exit`

## Week 2: Crud
## Week 3: Schema Design
