import pymongo
import api
from api import read_qr_code
from pymongo import MongoClient

scannedQR = api.read_qr_code('qrcode002.png')

def change_database(collection):
    """Changes the saved database for the current class

    Args:
        Collection (dictionary) - Python dictionary of students set to attend the next class
    Returns:
        Completed (dictionary) - Python dictionary of the completed attendance list of the last class
    """
    new_class = collection

    client = MongoClient('mongodb+srv://kmj4789:Alinani95!@Cluster0.a9jy9oq.mongodb.net/?retryWrites=true&w=majority')
    #setting cluster test
    db = client["Attendance_List"]
    class_connect = db["Class"]
    class_connect.drop
    class_connect.insert_many(new_class)
    
def mark_scan(qr):
    #Connecting to database for M1
    client = MongoClient('mongodb+srv://kmj4789:Alinani95!@Cluster0.a9jy9oq.mongodb.net/?retryWrites=true&w=majority')
    db = client["Attendance_List"]
    class_connect = db["Class"]

    #setting the query to search for QR code and to mark attendance
    myquery = {"QR_Code": qr}
    attended = {"$set": {"Has_Attended": "Yes"}}
    class_connect.update_one(myquery, attended)

    for x in class_connect.find():
        print(x)

mark_scan(scannedQR)