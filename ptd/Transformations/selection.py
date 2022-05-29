#Fonctions pour pouvoir sélectionner une variable avec son nom (comme avec un dictionnaire) 
# plutôt qu'avec son indice, je sais pas encore dans quelle classe mettre ça

from ptd.table import Table
from ptd.transformations.transformation import Transformation

class Selection(Transformation):

    def __init__(self):
        pass
    

    def execute(table,variables):
        '''Sélectionne la variable demandée 

        Parameters
        ----------
        variables : liste
            Liste des variables sélectionnées
        table : Table
            La base de données

        Returns
        -------
        liste_index
            liste des indices des variables recherchées
        ''' 
        for i in range(len(variables)):
            assert variables[i] in table.nom_colonnes
        for j in range(len(table.nom_colonnes)):
            if table.nom_colonnes[j] not in variables:
                del table.nom_colonnes[j]
                del table.valeurs[j]
        return table

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    colonnes=['fruits','legumes','sante']
    valeurs=[['kiwi','poire','abricot'],['haricot','pois','mq'],['bien','pas bien','moyen']]
    table1=Table(nom_colonnes=colonnes,valeurs=valeurs)
    variables1=['fruits','legumes']
    variables2=['fruits']
    alpha=Selection.execute(table1,variables1)
    Table.afficher(alpha)
    beta=Selection.execute(table1,variables2)
    Table.afficher(beta)




