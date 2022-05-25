from estimateur import Estimateur
import doctest


class Moyenne(Estimateur):
    def __init__(self,variable) -> None:
        
     
        #C'est bizarre, pourquoi ici tu prends une variable en entrée et pas le dataframe comme d'habitude pour après selectionner la variable (en fait pour tous les estimateurs)
   
        self.variable=variable
        self.valeur = self.execute()

    def execute(self):
        '''
        >>> var1 = [2,2,2,5,5,5]
        >>> m1 = Moyenne(var1)
        >>> print(m1.execute())
        3.05
        '''
   
        som=0
        for i in self.variable:
            som+=i
        moyenne = som/len(self.variable)
        return moyenne

    
    if __name__ == '__main__':
        import doctest
        doctest.testmod()