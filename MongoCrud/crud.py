from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.PersonData

print(db)

Person = db.Person
db.Person.insert_many([
    {'name':'Neha','age':30,'country':'India' },
    {'name':'Mounika',
     'age':25,
     'country':'India'
     },
    {'name':'Almitra',
     'age':21,
     'country':'India'
     },
    {'name':'Pinaki',
     'age':23,
     'country':'India'
     },
    {'name':'Ketaki',
     'age':30,
     'country':'India'
     }]
)

db.Person.delete_many({'name':'Neha'})

db.Person.update({'age':30},{'$set':{'age':16}})

people = db.Person.find()

for p in people:
    print(p)

