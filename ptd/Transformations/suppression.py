from matplotlib.pyplot import table
from ptd.table import Table
from ptd.transformations.transformation import Transformation

class Suppression(Transformation):
    def __init__(self):
        '''Supprime une variable

        Parameters
        ----------
        Table : table
            La base de données
        '''

    def execute(table,variable):
        assert variable in table.nom_colonnes
        i=table.nom_colonnes.index(variable)
        del table.nom_colonnes[i]
        for j in range(len(table.valeurs[i])):
            del table.valeurs[i][j]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    colonnes=['fruits','legumes','sante']
    valeurs=[['kiwi','poire','abricot'],['haricot','pois','mq'],['bien','pas bien','moyen']]
    table1=Table(nom_colonnes=colonnes,valeurs=valeurs)
    Suppression.execute(table1,'fruits')
    Table.afficher(table1)