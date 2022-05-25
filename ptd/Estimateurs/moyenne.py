from ptd.estimateurs.estimateur import Estimateur

class Moyenne(Estimateur):
    '''
    >>> [1,2,3]
    2
    '''
    def __init__(self,variable) -> None:
        #C'est bizarre, pourquoi ici tu prends une variable en entrée et pas le dataframe comme d'habitude pour après selectionner la variable (en fait pour tous les estimateurs)
        '''Calcule la moyenne d'une variable

        Parameters
        ----------
        variable : list
            La variable
        '''
        self.variable=variable

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


if __name__ == '__main__':
    # Utilisation des tests unitaires doctest pour tester le module.
    # Usuellement, le code dans ce bloc if n'est exécuté que pour des tests, d'où
    # l'intérêt d'y mettre les doctests.
    import doctest
    doctest.testmod()

    