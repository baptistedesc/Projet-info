from matplotlib.pyplot import table
from ptd.table import Table
from ptd.transformations.transformation import Transformation

class Renommer(Transformation):
    def __init__(self):
        '''Renomme une variable

        Parameters
        ----------
        Table : table
            La base de données
        '''

    def execute(table,variable_avant,variable_apres):
        i=table.nom_colonnes.index(variable_avant)
        table.nom_colonnes[i]=variable_apres
        return table

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    colonnes=['fruits','legumes','sante']
    valeurs=[['kiwi','poire','abricot'],['haricot','pois','mq'],['bien','pas bien','moyen']]
    alpha=Table(colonnes,valeurs)
    beta=Renommer.execute(alpha,'fruits','construction')
    Table.afficher(beta)