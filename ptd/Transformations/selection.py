#Fonctions pour pouvoir sélectionner une variable avec son nom (comme avec un dictionnaire) 
# plutôt qu'avec son indice, je sais pas encore dans quelle classe mettre ça

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
    

    def execute(self,colonnes,table):
        '''Sélectionne la variable demandée 

        Parameters
        ----------
        colonnes : liste
            Les noms des variables à selectionner
        table : Table
            La table contenant les variables

        Returns
        -------
        list
            Les variables demandées.
     ''' 
        selection = []
        for i in range(0,len(colonnes)):
            indice = table.nom_colonnes.index(colonnes[i])
            selection.append(table.valeurs[indice])
        return selection
     