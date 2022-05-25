import gzip
import json

folder = "//filer-eleves.domensai.ecole/id1977/Projet-info/donnees_electricite/"
filename = "2022-03.json.gz"
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

#Tests
# print(donnees[0])
# print(data[0])
# print(nom_variables)

donnees.insert(0,nom_variables)
print(donnees[0])
print(donnees[4])
# print(base_donnees)


dataframe=[]
for k in range(len(nom_variables)):
    dataframe.append([])
for i in range(len(nom_variables)):
    for j in range(len(donnees)):
        dataframe[i].append(donnees[j][i])

# print(dataframe[0][0:10])

# Summary
# resume=[]
# n=len(dataframe)
# for i in range(n):
#     resume.append([])
# for i in range(n):
#     resume[i].append(dataframe[i][0])
#     resume[i].append(type(dataframe[i][1]))
# print(resume)


