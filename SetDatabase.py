import pymongo
from pymongo import MongoClient



client = MongoClient('mongodb+srv://kmj4789:Alinani95!@Cluster0.a9jy9oq.mongodb.net/?retryWrites=true&w=majority')

#setting cluster test
db = client["Class_Roles"]


collection = db["Class_One"]

c1post = [
    {"First_Name": "Christian", "Last_Name": "Bale", "Student_ID": 14875771, "QR_Code": "https://www.imdb.com/name/nm0000288/", "Has_Attended": "No"},
    {"First_Name": "Sam", "Last_Name": "Jackson", "Student_ID": 12345869, "QR_Code": "https://www.imdb.com/name/nm0000168/?ref_=nv_sr_srsg_0", "Has_Attended": "No"},
    {"First_Name": "Matt", "Last_Name": "Damon", "Student_ID": 15995145, "QR_Code": "https://www.imdb.com/name/nm0000354/?ref_=nv_sr_srsg_0", "Has_Attended": "No"},
    {"First_Name": "Tom", "Last_Name": "Cruise", "Student_ID": 15824875, "QR_Code": "https://www.imdb.com/name/nm0000129/?ref_=nv_sr_srsg_0", "Has_Attended": "No"},
    {"First_Name": "Emma", "Last_Name": "Stone", "Student_ID": 12565656, "QR_Code": "https://www.imdb.com/name/nm1297015/?ref_=nv_sr_srsg_6", "Has_Attended": "No"},
    {"First_Name": "Danny", "Last_Name": "Devito", "Student_ID": 16253636, "QR_Code": "https://www.imdb.com/name/nm0000362/?ref_=nv_sr_srsg_4", "Has_Attended": "No"},
    {"First_Name": "Robert", "Last_Name": "De Niro", "Student_ID": 23659584, "QR_Code": "https://www.imdb.com/name/nm0000134/?ref_=nv_sr_srsg_3", "Has_Attended": "No"},
    {"First_Name": "Denzel", "Last_Name": "Washington", "Student_ID": 86955958, "QR_Code": "https://www.imdb.com/name/nm0000243/?ref_=nv_sr_srsg_0", "Has_Attended": "No"},
]
collection.insert_many(c1post)

collection = db["Class_Two"]

c2post = [
    {"First_Name": "Ryan", "Last_Name": "Gosling", "Student_ID": 51654844, "QR_Code": "https://www.imdb.com/name/nm0331516/?ref_=nv_sr_srsg_0", "Has_Attended": "No"},
    {"First_Name": "Zac", "Last_Name": "Efron", "Student_ID": 1374980, "QR_Code": "https://www.imdb.com/name/nm1374980/?ref_=nv_sr_srsg_0", "Has_Attended": "No"},
    {"First_Name": "Jennifer", "Last_Name": "Lawrence", "Student_ID": 2225369, "QR_Code": "https://www.imdb.com/name/nm2225369/?ref_=nv_sr_srsg_0", "Has_Attended": "No"},
    {"First_Name": "Rachel", "Last_Name": "McAdams", "Student_ID": 104097, "QR_Code": "https://www.imdb.com/name/nm1046097/?ref_=nv_sr_srsg_0", "Has_Attended": "No"},
    {"First_Name": "Eva", "Last_Name": "Longoria", "Student_ID": 40519456, "QR_Code": "https://www.imdb.com/name/nm0519456/?ref_=nv_sr_srsg_1", "Has_Attended": "No"},
    {"First_Name": "Tom", "Last_Name": "Hardy", "Student_ID": 362766, "QR_Code": "https://www.imdb.com/name/nm0362766/?ref_=nv_sr_srsg_0", "Has_Attended": "No"},
    {"First_Name": "Daniel", "Last_Name": "Radcliffe", "Student_ID": 70535600, "QR_Code": "https://www.imdb.com/name/nm0705356/?ref_=nv_sr_srsg_0", "Has_Attended": "No"},
    {"First_Name": "Emma", "Last_Name": "Watson", "Student_ID": 91461200, "QR_Code": "https://www.imdb.com/name/nm0914612/?ref_=nv_sr_srsg_0", "Has_Attended": "No"},
]

collection.insert_many(c2post)


db = client["Attendance_List"]
class_connect = db["Class"]

class_connect.insert_many(c1post)