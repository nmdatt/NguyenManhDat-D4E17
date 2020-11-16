from pymongo import MongoClient
from bson import ObjectId


client = MongoClient('localhost', 27017)

movie_database = client.get_database('moviedb')

movie_collection = movie_database.get_collection('movies')

all_documents= movie_collection.find()

for i in all_documents:                                               #Query / Find Documents 1
    print(i)


name = movie_collection.find({'writer':'Quentin Tarantino'})          #Query / Find Documents 2
for i in name:
    print(i['title'])

actor = movie_collection.find({'actors':'Brad Pitt'})                 #Query / Find Documents 3
for i in actor:
    print(i)

franchies = movie_collection.find({"franchies":"The Hobbit"})         #Query / Find Documents 4
for i in franchies:
    print(i)

released1 = movie_collection.find(                                    #Query / Find Documents 5
    {'year':
        {'$gt':1990,
         '$lt':2000}
    }
)
for i in released1:
    print(i)

released2 = movie_collection.find(                                      #Query / Find Documents 6
    {'$or':
        [
            {'year':{'$lt':2000}
            },
            {'year':{'$gt':2010}
            }
        ]   
    }
)
for i in released2:
    print(i)

query1 = {'_id': ObjectId("5fb133d614bdcb160a82174a")}                       #Update Documents 1
update1 ={'$set':
       {
            'synopsis' : 'A reluctant hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home - and the gold within it - from the dragon Smaug.'
       }
}
movie_collection.update_one(query1,update1)

query2 = {'_id': ObjectId("5fb133d614bdcb160a82174b")}                          #Update Documents 2
update2 = {'$set':
       {
              'synopsis' : "The dwarves, along with Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug. Bilbo Baggins is in possession of a mysterious and magical ring."
       }
}
movie_collection.update_one(query2,update2)

query3 = {'_id': ObjectId("5fb133d614bdcb160a821748")}                              #update documents 3
update3 = {'$push':
       {
              'actors' : 'Samuel L. Jackson'
       }
}
movie_collection.update_one(query3,update3)


movie_collection.find_one_and_delete({'title':"Pee Wee Herman's Big Adventure"})    #Delete Documents 1

movie_collection.find_one_and_delete({'title':"Avatar"})                            #Delete Documents 2