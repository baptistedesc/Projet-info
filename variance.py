from estimateur import Estimateur


class Variance(Estimateur):
    def __init__(self,variable) -> None:
        '''Calcule la variance d'une variable

        Parameters
        ----------
        variable : list
            La variable
        '''
        self.variable = variable
    
    def execute(self):
        som=0
        for i in self.variable:
            som+=i
        moyenne = som/len(self.variable)
        sum=0
        for i in self.variable:
            sum+=(i-moyenne)**2
        variance = sum/len(self.variable)
        return variance
