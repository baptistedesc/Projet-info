from distutils.log import error
import gzip
import csv
import json

from ptd.table import Table

def isfloat(valeur):
    """Renvoie True si value est un flottant, False sinon
    Parameters
    ----------
    value : 
        Valeur dont on cherche à déterminer le type
    Returns
    -------
    bool
        True si value est un flottant, False sinon

    Examples
    --------
    >>> isfloat(9.0)
    True
    >>> fonction('test')
    False
    """
    try:
        float(valeur)
        return True
    except ValueError:
        return False

class Importer:
    def __init__(self,filename,folder):
        self.filename=filename
        self.folder=folder
    def lire(self):
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
            with gzip.open(self.folder + self.filename, mode='rt', encoding='utf-8') as gzfile :
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
        nom_colonnes=[]
        for i in range(len(dataframe)):
            nom_colonnes.append(dataframe[i][0])
            del dataframe[i][0]
        return Table(nom_colonnes,dataframe)


if __name__ == '__main__':
    folder = '//filer-eleves.domensai.ecole/id1977/Projet-info/donnees_electricite/'
    filename = '2013-01.json.gz' 
    beta=Importer(filename,folder)
    alpha=Importer.lire(beta)
    Table.afficher(alpha)
    print(alpha.nom_colonnes)


