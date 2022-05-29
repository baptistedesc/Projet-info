from Estimateurs.estimateur import Estimateur
import doctest


class Moyenne(Estimateur):
    '''
    >>> [1,2,3]
    2
    '''
    def __init__(self) -> None:
        pass
        
     
    def execute(self,colonne, table):
        '''
        >>> var1 = [2,2,2,5,5,5]
        >>> m1 = Moyenne(var1)
        >>> print(m1.execute())
        3.05
        '''       
        indice = table.nom_colonnes.index(colonne)
        moyenne = 0
        somme = 0
        for k in range(0,len(table.valeurs[indice])):
            somme = table.valeurs[indice][k] +somme
        moyenne=somme/(len(table.valeurs[indice]))
        return moyenne


if __name__ == '__main__':
    # Utilisation des tests unitaires doctest pour tester le module.
    # Usuellement, le code dans ce bloc if n'est exécuté que pour des tests, d'où
    # l'intérêt d'y mettre les doctests.
    import doctest
    doctest.testmod()

    
