from estimateur import Estimateur
import doctest


class Moyenne(Estimateur):
    '''
    >>> [1,2,3]
    2
    '''
    def __init__(self,variable) -> None:
        
     
        #C'est bizarre, pourquoi ici tu prends une variable en entrée et pas le dataframe comme d'habitude pour après selectionner la variable (en fait pour tous les estimateurs)
   
        self.variable=variable

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
    # Utilisation des tests unitaires doctest pour tester le module.
    # Usuellement, le code dans ce bloc if n'est exécuté que pour des tests, d'où
    # l'intérêt d'y mettre les doctests.
    import doctest
    doctest.testmod()

    
