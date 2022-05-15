from distutils.log import error
import gzip
import csv
import json

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

class dataframe:
    def __init__(self,folder,filename):
        self.folder=folder
        self.filename=filename
    def chargement(self):

        #Si le fichier est de type CSV
        if '.csv.gz' in self.filename:
            donnees = []
            with gzip.open(self.folder + self.filename, mode='rt') as gzfile :
                synopreader = csv.reader(gzfile, delimiter=';')
                for row in synopreader :
                    donnees.append(row)
            #On récupére une case vide [] en trop dans chaque liste qu'on doit supprimer
            for i in range(len(donnees)):
                del donnees[i][-1]

        #Si le fichier est de type json
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
    
        #On passe d'un système donnees=[[var1,var2],[donnee1,donnee2]] à dataframe=[[var1,donnee1],[var2,donnee2]]
        dataframe=[]
        for k in range(len(donnees[0])):
            dataframe.append([])
        for i in range(len(donnees[0])):
            for j in range(len(donnees)):
                dataframe[i].append(donnees[j][i])

        #Conversion des nombres en float
        for i in range(len(dataframe)):
            for j in range(len(dataframe[0])):
                 if isfloat(dataframe[i][j])==True:
                     dataframe[i][j]=float(dataframe[i][j])        
        return dataframe

    def resume(self):
        donnees=dataframe.chargement(self)
        resume=[]
        n=len(donnees)
        for i in range(n):
            resume.append([])
        for i in range(n):
            resume[i].append(donnees[i][0])
            resume[i].append(type(donnees[i][1]))
        return resume

# Pour tester la fonction chargement (je sais pas comment faire avec le __main__)
folder = '//filer-eleves.domensai.ecole/id1977/Projet-info/donnees_meteo/'
filename = 'synop.201301.csv.gz'

Frac=dataframe(folder,filename)
# print(dataframe.chargement(Frac))
print(dataframe.resume(Frac))


















