from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('localhost', 27017)

relationship_database = client.get_database('relationshipdb')

users_collection = relationship_database.get_collection('user')
posts_collection = relationship_database.get_collection('posts')
comments_collection = relationship_database.get_collection('comments')

users = [
    {
        'username' : 'GoodGuyGreg',
        'first_name' : "Good Guy",
        'last_name' : "Greg"
    },
    {
        'username' : 'ScumbagSteve',
        'full_name' :
                {
                    'first' : "Scumbag",
                    'last' : "Steve"
                }
    }
]
users_collection.insert_many(users)

posts = [
    {
        'username' : 'GoodGuyGreg',
        'title' : 'Passes out at party',
        'body' : 'Wakes up early and cleans house'
    },
    {
        'username' : 'GoodGuyGreg',
        'title' : 'Steals your identity',
        'body' : 'Raises your credit score'
    },
    {
        'username' : 'GoodGuyGreg',
        'title' : 'Reports a bug in your code',
        'body' : 'Sends you a Pull Request'
    },
    {
        'username' : 'ScumbagSteve',
        'title' : 'Borrows something',
        'body' : 'Sells it'
    },
    {
        'username' : 'ScumbagSteve',
        'title' : 'Borrows everything',
        'body' : 'The end'
    },
    {
        'username' : 'ScumbagSteve',
        'title' : 'Forks your repo on github',
        'body' : 'Sets to private'
    }
]

posts_collection.insert_many(posts)

comments = [
    {
        'username' : 'GoodGuyGreg',
        'comment' : 'Hope you got a good deal!',
        'post' : ObjectId("5fb2441c6be213e2b7b4ee9f")
    },
    {
        'username' : 'GoodGuyGreg',
        'comment' : "What's mine is yours!",
        'post' : ObjectId("5fb2441c6be213e2b7b4eea0")
    },
    {
        'username' : 'GoodGuyGreg',
        'comment' : "Don't violate the licensing agreement!",
        'post' : ObjectId("5fb2441c6be213e2b7b4eea1")
    },
    {
        'username' : 'ScumbagSteve',
        'comment' : "It still isn't clean",
        'post' : ObjectId("5fb2441c6be213e2b7b4ee9c")
    },
    {
        'username' : 'ScumbagSteve',
        'comment' : 'Denied your PR cause I found a hack',
        'post' : ObjectId("5fb2441c6be213e2b7b4ee9e")    
    }
]

comments_collection.insert_many(comments)