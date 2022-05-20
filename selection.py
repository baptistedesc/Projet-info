#Fonctions pour pouvoir sélectionner une variable avec son nom (comme avec un dictionnaire) 
# plutôt qu'avec son indice, je sais pas encore dans quelle classe mettre ça

from transformation import Transformation

class Selection(Transformation):
#On créé la liste des variables
    def __init__(self,dataframe):
        '''Sélectionne certaines variables d'une base de données
        
        Renvoie une nouvelle basse de données contenant seulement ces variables

        Parameters
        ----------
        dataframe : table
            La base de données
        '''
        self.dataframe=dataframe

    def execute(self,variable):
        nom_variables=[]
        for i in range(len(self.dataframe)):
            nom_variables.append(self.dataframe[i][0])
        assert variable in nom_variables
        for i in range(len(self.dataframe))
            if self.dataframe[i][0]==variable:
                return self.dataframe[i]

        
