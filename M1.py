import pymongo
from pymongo import MongoClient



def change_database(collection):
    
    new_class = collection

    client = MongoClient('mongodb+srv://kmj4789:Alinani95!@Cluster0.a9jy9oq.mongodb.net/?retryWrites=true&w=majority')
    #setting cluster test
    db = client["Attendance_List"]
    class_connect = db["Class"]
    class_connect.delete_many({})
    class_connect.insert_many(new_class)
    print("hit update")
    return
    
def mark_scan(qr):
    #Connecting to database for M1
    client = MongoClient('mongodb+srv://kmj4789:Alinani95!@Cluster0.a9jy9oq.mongodb.net/?retryWrites=true&w=majority')
    db = client["Attendance_List"]
    class_connect = db["Class"]

    #setting the query to search for QR code and to mark attendance
    myquery = {"QR_Code": qr}
    attended = {"$set": {"Has_Attended": "Yes"}}
    if class_connect.find_one(myquery):
        class_connect.update_one(myquery, attended)
    else:
        new_student = {"First_Name": 'Sam', "Last_Name": 'Gilchrist', "Student_ID": 1255252, "QR_Code": qr, "Has_Attended": 'Yes', "Action_Needed": 'Yes'}
        class_connect.insert_one(new_student)

    for x in class_connect.find():
        print(x)
    return

def send_list():
    client = MongoClient('mongodb+srv://kmj4789:Alinani95!@Cluster0.a9jy9oq.mongodb.net/?retryWrites=true&w=majority')
    db = client["Attendance_List"]
    class_connect = db["Class"]
    completed_list = class_connect.find({})

    return completed_list