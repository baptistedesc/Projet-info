#Fonctions pour pouvoir sélectionner une variable avec son nom (comme avec un dictionnaire) 
# plutôt qu'avec son indice, je sais pas encore dans quelle classe mettre ça

from ptd.table import Table
from ptd.importer import Importer
from ptd.transformations.transformation import Transformation

class Selection(Transformation):

    def __init__(self):
        pass
    

    def execute(colonnes,table):
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
        nom_colonnes=[]
        valeurs=[]
        for i in range(len(table.nom_colonnes)):
            if table.nom_colonnes[i] in colonnes:
                nom_colonnes.append(table.nom_colonnes[i])
                valeurs.append(table.valeurs[i])
        return Table(nom_colonnes,valeurs)
     

if __name__ == '__main__':
    folder = '//filer-eleves.domensai.ecole/id1977/Projet-info/donnees_electricite/'
    filename = '2013-01.json.gz' 
    beta=Importer(filename,folder)
    alpha=Importer.lire(beta)
    print(alpha.nom_colonnes)
    gamma=Selection.execute(['date','date_heure'],alpha)

