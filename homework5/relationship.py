from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('localhost', 27017)

relationship_database = client.get_database('relationshipdb')

users_collection = relationship_database.get_collection('user')
posts_collection = relationship_database.get_collection('posts')
comments_collection = relationship_database.get_collection('comments')

users = users_collection.find()           #find all users
for i in users:
    print(i)
print()

post = posts_collection.find()              #find all post
for i in post:
    print(i)
print()

for document in post:                                      #find all posts that was authored by "GoodGuyGreg"
    if document['username'] == 'GoodGuyGreg':
        print(document)
print()

for document in post:                                      #find all posts that was authored by "ScumbagSteve"
    if document['username'] == 'ScumbagSteve':
        print(document)
print()

comments = comments_collection.find()                            #find all comments
for i in comments:
    print(i)
print()

for obj in comments:                                          #find all comments that was authored by "GoodGuyGreg"
    if obj['username'] == 'GoodGuyGreg':
        print(obj)
print()

for obj in comments:                                            #find all comments that was authored by "ScumbagSteve"
    if obj['username'] == 'ScumbagSteve':
        print(obj)
print()

question_8 = comments_collection.find_one({'post' : ObjectId("5fb2441c6be213e2b7b4ee9e") })     #find all comments belonging to the post "Reports a bug in your code"
print(question_8)