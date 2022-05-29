from matplotlib.pyplot import table
from ptd.table import Table
from ptd.transformations.transformation import Transformation

class Suppression(Transformation):
    def __init__(self):
        pass

    def execute(table,variable):
        assert variable in table.nom_colonnes
        i=table.nom_colonnes.index(variable)
        del table.nom_colonnes[i]
        del table.valeurs[i]
        return table


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    colonnes=['fruits','legumes','sante']
    valeurs=[['kiwi','poire','abricot'],['haricot','pois','mq'],['bien','pas bien','moyen']]
    table=Table(colonnes,valeurs)
    Suppression.execute(table,'fruits')
    Table.afficher(table)