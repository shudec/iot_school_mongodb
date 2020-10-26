from pymongo import MongoClient

client = MongoClient('mongodb://localhost:3000/', username='root', password='iot')

db = client.ecoleiot_db
