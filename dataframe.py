import gzip
import csv
import json

class dataframe:
    def __init__(self,folder,filename):
        self.folder=folder
        self.filename=filename
    def chargement(self):
        if 'csv.gz' in self.filename:
            data = []
            with gzip.open(self.folder + self.filename, mode='rt') as gzfile :
                synopreader = csv.reader(gzfile, delimiter=';')
                for row in synopreader :
                    data.append(row)
        #Transformer ça en listes de listes
        elif 'json.gz' in self.filename:
            with gzip.open(self.folder + self.filename, mode='rt') as gzfile :
                data = json.load(gzfile)
        return data













