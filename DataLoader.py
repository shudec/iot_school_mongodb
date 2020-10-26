import json

class DataLoader(object):

    filename=''

    def __init__ (self, filename):
        self.filename = filename

    def load (self):
        data = []
        try:
            dataFile = open(self.filename, mode='r', encoding='utf-8')
            data = json.load(dataFile)
        finally:
            dataFile.close
        return data