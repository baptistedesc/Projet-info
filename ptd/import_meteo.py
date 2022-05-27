import gzip
import csv

# Dossier où se trouve le fichier :
folder = '//filer-eleves.domensai.ecole/id1953/Projet-info/donnees_meteo/'
filename = 'synop.201301.csv.gz'
data = []
with gzip.open(folder + filename, mode='rt') as gzfile :
    synopreader = csv.reader(gzfile, delimiter=';')
    for row in synopreader :
        data.append(row)
for i in range(len(data)):
    del data[i][-1]

print(data.nom_colonnes())