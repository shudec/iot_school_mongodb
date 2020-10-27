from EcoleIotMongodb import client, db
from DataLoader import DataLoader
import unittest

class TestMongodbExercices(unittest.TestCase):

    def test_db_connection(self):
        self.assertTrue(client != None, "MongoDB client is initialized")
        self.assertTrue(db != None, "database exists")
        print("Collections: " + str(db.list_collection_names()))

    def test_dataloader(self):
        dataLoader = DataLoader('students.json')
        data = dataLoader.load()
        self.assertTrue(data != None, "data exist")

if __name__ == '__main__':
    unittest.main()