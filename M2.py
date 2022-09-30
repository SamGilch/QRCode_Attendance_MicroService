import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb+srv://kmj4789:Alinani95!@Cluster0.a9jy9oq.mongodb.net/?retryWrites=true&w=majority')

#setting cluster test
db = client["Class_Roles"]
test_time = 1


def update_class():

    if test_time == 0:
        collection = db["Class_One"]
        students = collection.find({})
        test_time + 1
        return students
    elif test_time == 1:
        collection = db["Class_Two"]
        students = collection.find({})
        test_time + 1
        return students
    else:
        return

