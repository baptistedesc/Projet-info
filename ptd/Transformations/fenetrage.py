from ptd.transformations.transformation import Transformation
from ptd.transformations.selection import Selection

class Fenetrage(Transformation):
#On créé la liste des variables
    def __init__(self,table,date1,date2):
        '''Fenêtre la base de données

        Conserve uniquement les données comprises entre deux dates 

        Parameters
        ----------
        table : table
            La base de données
        date1 : ???????????????????????
            La date de début pour le fenêtrage
        date2 : ????????????????????????????
            La date de fin du fenêtrage
        '''
        self.table=table
        self.date1=date1
        self.date2=date2
    def execute(self):
        '''Fenêtre la base de données

        Returns
        -------
        table
            La base de données initiale, mais réduite à la période demandée
        ''' 
# Il y a un problème à régler avec les dates


