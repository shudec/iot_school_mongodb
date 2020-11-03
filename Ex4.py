from EcoleIotMongodb import db
import json
import random

# Delete documents with an empty name
print("Delete documents with an empty name")
all_students_with_empty_name = db.students.find({"name": ""})
for student in all_students_with_empty_name:
    print(student)
db.students.delete_many({"name": ""})

all_students_with_empty_name = db.students.find({"name": ""})
for student in all_students_with_empty_name:
    print(student)
