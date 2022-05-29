from ptd.estimateurs.estimateur import Estimateur
from ptd.table import Table
import doctest


class Somme(Estimateur):
    '''
    >>> [1,2,3]
    6
    '''
    def __init__(self) -> None:
        pass
        
     
    def execute(self,colonne, table):
        '''
        >>> var1 = [2,2,2,5,5,5]
        >>> nom=["var1"]
        >>> m1 = Somme()
        >>> Ex=Table(nom,var1)
        >>> print(Ex)
        >>> 
        21
        '''       
        indice = table.nom_colonnes.index(colonne)
        somme = 0
        for k in range(0,len(table.valeurs[indice])):
            somme = table.valeurs[indice][k] +somme
        return somme 


if __name__ == '__main__':
    var1 = [2,2,2,5,5,5]
    nom=["var1"]
    m1 = Somme()
    Ex=Table(nom,var1)
    print(Ex)
    
    import doctest
    doctest.testmod()

    
