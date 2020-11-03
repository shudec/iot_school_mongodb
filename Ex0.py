from EcoleIotMongodb import db
from DataLoader import DataLoader

dataLoader = DataLoader('students.json')
data = dataLoader.load()
db.students.delete_many({})
db.students.insert_many(data)

print(db.students.find_one({"name": "Aurelia Menendez"}))