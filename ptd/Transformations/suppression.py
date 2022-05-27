from matplotlib.pyplot import table
from ptd.table import Table
from ptd.transformations.transformation import Transformation

class Suppresion(Transformation):
    def __init__(self,table):
        '''Supprime une variable

        Parameters
        ----------
        Table : table
            La base de données
        '''
        self.table=table

    def execute(self,variable):
        i=self.table.nom_colonnes.index(variable)
        del self.table.nom_colonnes[i]
        for j in range(len(self.table.nom_colonnes[i])):
            del self.table.nom_colonnes.valeurs[i][j]


