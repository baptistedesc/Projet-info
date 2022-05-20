from estimateur import Estimateur



class Moyenne(Estimateur):
    def __init__(self,variable) -> None:
        #C'est bizarre, pourquoi ici tu prends une variable en entrée et pas le dataframe comme d'habitude pour après selectionner la variable (en fait pour tous les estimateurs)
        '''Calcule la moyenne d'une variable

        Parameters
        ----------
        variable : list
            La variable
        '''
        self.variable=variable
        self.valeur = self.execute()

    def execute(self):
        '''Calcule la moyenne 

        Returns
        -------
        float
            La moyenne demandée
        ''' 
        som=0
        for i in self.variable:
            som+=i
        moyenne = som/len(self.variable)
        return moyenne

    