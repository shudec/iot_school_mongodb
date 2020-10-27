import json

class DataLoader(object):

    filename=''

    def __init__ (self, filename):
        self.filename = filename

    def load (self):
        data = []
        try:
            dataFile = open(self.filename, mode='r', encoding='utf-8')
            for line in dataFile:
                data.append(json.loads(line))
        finally:
            dataFile.close()
        return data