from EcoleIotMongodb import db
import json

#all documents
print("all documents")
all_students = db.students.find()
for student in all_students:
    print(student)

# all documents with name set to "Jessika Dagenais"
print("\nall documents with name set to Jessika Dagenais")
jess = db.students.find({"name": "Jessika Dagenais"})
for j in jess:
    print(j)

# all documents which score of exam is greater than 50
print("\nall documents which score of exam is greater than 50")
good_scores = db.students.find({"scores": {"$elemMatch": {"score": {"$gt": 50}, "type": "exam"}}})
for s in good_scores:
    print(s)

# all documents which score of homework is between 50 and 70
print("\nall documents which score of homework is between 50 and 70")
good_scores = db.students.find({"scores": {"$elemMatch": {"score": {"$gt": 50, "$lt": 70}, "type": "homework"}}})
for s in good_scores:
    print(s)

