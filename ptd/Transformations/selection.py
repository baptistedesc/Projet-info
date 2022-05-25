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

    def execute(self,table,variable):
        
        '''Sélectionne la variable demandée 

        Parameters
        ----------
        variable : str
            Le nom de la variable à selectionner
        dataframe : table
            La base de données

        Returns
        -------
        table
            La variable demandée
        ''' 
        #Pas sûr d'avoir complètement capté comment ça marche donc à vérifier. En fait comme c'est codé selection ça sert juste à prendre une variable à part pour après faire 
        # des opérations dessus, mais je pense qu'il faudrait qu'on ait aussi un truc pour selectionner plusieurs variables et réduire la base de données à ça (un peu comme fenêtrage fait
        # une sélection sur les lignes, faire une sélection sur les colonnes mais qui modifie le dataframe)
        #On créé la liste des variables
        for i in range(len(table.nom_colonnes)):
            assert variable in table.nom_colonnes
        for i in range(len(table.nom_colonnes)) :
            if table.nom_colonnes[i]==variable:
                return Table(table.nom_colonnes[i],table.valeurs[i])

#tu penses ca marche ca ?
        indice=table.nom_colonnes.index(variable)
        return Table(table.nom_colonnes[indice],table.valeurs[indice])
