import gzip
import csv
import json

class dataframe:
    def __init__(self,folder,filename):
        self.folder=folder
        self.filename=filename
    def chargement(self):
        if '.csv.gz' in self.filename:
            donnees = []
            with gzip.open(self.folder + self.filename, mode='rt') as gzfile :
                synopreader = csv.reader(gzfile, delimiter=';')
                for row in synopreader :
                    donnees.append(row)

        elif '.json.gz' in self.filename:
            with gzip.open(folder + filename, mode='rt', encoding='utf-8') as gzfile :
                data0 = json.load(gzfile)
            data1=[obs['fields'] for obs in data0]

            nom_variables=[]
            donnees=[]
            n=len(data1)

            #Création de la liste des variables
            for i in range(n):
                donnees.append([])
                for cle in data1[i].keys():
                    if not cle in nom_variables:
                        nom_variables.append(cle)

            #Assignation des valeurs manquantes
            for i in range(n):
                for j in range(len(nom_variables)):
                    if not nom_variables[j] in data1[i].keys():
                        data1[i][nom_variables[j]]='mq'

            #Remplissage de la liste de liste données
            for i in range(n):
                for j in range(len(nom_variables)):
                    donnees[i].append(data1[i][nom_variables[j]])

            #Insertion de la liste des variables au début des données
            donnees.insert(0,nom_variables)
    
        #On fait la transposée de la matrice des données en quelque sorte

        dataframe=[]
        for k in range(len(donnees[0])):
            dataframe.append([])
        for i in range(len(donnees[0])):
            for j in range(len(donnees)):
                dataframe[i].append(donnees[j][i])
        return dataframe


folder = '//filer-eleves.domensai.ecole/id1977/Projet-info/donnees_meteo/'
filename = 'synop.201301.csv.gz'

Frac=dataframe(folder,filename)
print(dataframe.chargement(Frac)[0][0])


















