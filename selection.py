#Fonctions pour pouvoir sélectionner une variable avec son nom (comme avec un dictionnaire) 
# plutôt qu'avec son indice, je sais pas encore dans quelle classe mettre ça

from transformation import Transformation

class Selection(Transformation):
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
        '''Sélectionne la variable demandée 

        Parameters
        ----------
        variable : str
            Le nom de la variable à selectionner

        Returns
        -------
        list
            La variable demandée
        ''' 
        #Pas sûr d'avoir complètement capté comment ça marche donc à vérifier. En fait comme c'est codé selection ça sert juste à prendre une variable à part pour après faire 
        # des opérations dessus, mais je pense qu'il faudrait qu'on ait aussi un truc pour selectionner plusieurs variables et réduire la base de données à ça (un peu comme fenêtrage fait
        # une sélection sur les lignes, faire une sélection sur les colonnes mais qui modifie le dataframe)
        #On créé la liste des variables
        nom_variables=[]
        for i in range(len(self.dataframe)):
            nom_variables.append(self.dataframe[i][0]) #mais du coup on est d'accord que comme en entrée on va prendre une seule variable c'est un peu bizarre de coder comme ça non ?
        assert variable in nom_variables
        for i in range(len(self.dataframe))
            if self.dataframe[i][0]==variable:
                return self.dataframe[i]

        
