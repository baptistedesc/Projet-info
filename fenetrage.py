from transformation import Transformation
from selection import Selection

class Fenetrage(Transformation):
#On créé la liste des variables
    def __init__(self,dataframe,date1,date2):
        '''Fenêtre la base de données

        Conserve uniquement les données comprises entre deux dates 

        Parameters
        ----------
        dataframe : table
            La base de données
        date1 : ???????????????????????
            La date de début pour le fenêtrage
        date2 : ????????????????????????????
            La date de fin du fenêtrage
        '''
        self.dataframe=dataframe
        self.date1=date1
        self.date2=date2
    def execute(self):
# Il y a un problème à régler avec les dates
        date=Selection.execute(date)
        for i in range (1,len(date)):
            if date1>date[i] or date2<date[i]:
                for j in range len(self.dataframe):
                    del self.dataframe[j][i]
        return self.dataframe


