import gzip
import json

folder = "//filer-eleves.domensai.ecole/id1977/traitement_donnees/"
filename = "2013-01.json.gz"
with gzip.open(folder + filename, mode='rt') as gzfile :
    data = json.load(gzfile)

print(data[3]['fields'])