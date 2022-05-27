#Fonctions pour pouvoir sélectionner une variable avec son nom (comme avec un dictionnaire) 
# plutôt qu'avec son indice, je sais pas encore dans quelle classe mettre ça

from ptd.table import Table
from ptd.transformations.transformation import Transformation

class Selection(Transformation):
    def __init__(self):
        '''Sélectionne certaines variables d'une base de données
        
        Renvoie une nouvelle basse de données contenant seulement ces variables

        Parameters
        ----------
        dataframe : table
            La base de données
        '''
    

    def execute(self,variables,table):
        '''Sélectionne la variable demandée 

        Parameters
        ----------
        variables : liste
            Le nom de la variable à selectionner
        table : Table
            La base de données

        Returns
        -------
        liste_index
            liste des indices des variables recherchées
        ''' 
        #Pas sûr d'avoir complètement capté comment ça marche donc à vérifier. En fait comme c'est codé selection ça sert juste à prendre une variable à part pour après faire 
        # des opérations dessus, mais je pense qu'il faudrait qu'on ait aussi un truc pour selectionner plusieurs variables et réduire la base de données à ça (un peu comme fenêtrage fait
        # une sélection sur les lignes, faire une sélection sur les colonnes mais qui modifie le dataframe)
        #On créé la liste des variables
        liste_index=[]
        for i in range(len(variables)):
            assert variables[i] in table.nom_colonnes
        for j in range(len(variables)):
            liste_index.append(table.nom_colonnes.index(variables[i]))
        return liste_index


