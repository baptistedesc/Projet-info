from matplotlib.pyplot import table
from ptd.table import Table
from ptd.transformations.transformation import Transformation

class Renommer(Transformation):
    def __init__(self,table):
        '''Renomme une variable

        Parameters
        ----------
        Table : table
            La base de données
        '''
        self.table=table

    def execute(self,variable_avant,variable_apres):
        i=self.table.nom_colonnes.index(variable_avant)
        self.table.nom_colonnes[i]=variable_apres
        return self.table