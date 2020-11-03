from EcoleIotMongodb import db
import json
import random

# add a note of type "terminal exam" to all students
print("add a note of type terminal exam to all students")
db.students.update_many({}, {"$push": {"scores": {"score": random.randrange(0, 100), "type": "terminal exam"}}})
all_students = db.students.find()
for student in all_students:
    print(student)

# add the mean of notes to all students
print("add the mean of notes to all students")
db.students.update_many({},
    [
        {"$set": {"mean": {"$avg": "$scores.score"}}} 
    ])
all_students = db.students.find()
for student in all_students:
    print(student)

