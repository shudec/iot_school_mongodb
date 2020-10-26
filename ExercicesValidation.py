from EcoleIotMongodb import client, db
import unittest

class TestMongodbExercices(unittest.TestCase):

    def test_db_connection(self):
        self.assertTrue(client != None, "le client MongoDB est initialisé")
        self.assertTrue(db != None, "la base de données existe")
        print("Collections: " + str(db.list_collection_names()))

if __name__ == '__main__':
    unittest.main()