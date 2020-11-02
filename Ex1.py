from EcoleIotMongodb import db
import json

db.students.insert(json.loads('{"name":"Guy Brossard","scores":[{"score":87.5,"type":"exam"},{"score":58.6,"type":"quiz"},{"score":60.8,"type":"homework"}]}'))
db.students.insert(json.loads('{"name":"Patrick Folrui","scores":[{"score":47.5,"type":"exam"},{"score":28.6,"type":"quiz"},{"score":80.8,"type":"homework"}]}'))
db.students.insert(json.loads('{"name":"Yann Dubois","scores":[{"score":57.5,"type":"exam"},{"score":88.6,"type":"quiz"},{"score":68.8,"type":"homework"}]}'))

print(db.students.find_one({"name": "Patrick Folrui"}))