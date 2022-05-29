from transformations.transformation import Transformation
from transformations.selection import Selection

class Fenetrage(Transformation):
#On créé la liste des variables
    def __init__(self):
        pass

    def execute(self,table1,table2,date1,date2):
        '''Fenêtre la base de données

        Returns
        -------
        table
            La base de données initiale, mais réduite à la période demandée
        ''' 


