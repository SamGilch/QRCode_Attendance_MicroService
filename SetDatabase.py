import pymongo
from pymongo import MongoClient



client = MongoClient('mongodb+srv://kmj4789:Alinani95!@Cluster0.a9jy9oq.mongodb.net/?retryWrites=true&w=majority')

#setting cluster test
db = client["test"]

collection = db["test"]

post = {"First_Name": "John", "Last_Name": "Smith", "Student_ID": 14875771, "QR_Code": "Google.com", "Has_Attended": "No"}

collection.insert_one(post)
