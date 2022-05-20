from ptd.estimateurs.estimateur import Estimateur


class Variance(Estimateur):
#C'est bizarre, pourquoi ici tu prends une variable en entrée et pas le dataframe comme d'habitude pour après selectionner la variable (en fait pour tous les estimateurs)    
    def __init__(self,variable) -> None:
        '''Calcule la variance d'une variable

        Parameters
        ----------
        variable : list
            La variable
        '''
        self.variable = variable
    
    def execute(self):
        '''Calcule la variance

        -------
        float
            La variance demandée
        ''' 
        som=0
        for i in self.variable:
            som+=i
        moyenne = som/len(self.variable)
        sum=0
        for i in self.variable:
            sum+=(i-moyenne)**2
        variance = sum/len(self.variable)
        return variance
