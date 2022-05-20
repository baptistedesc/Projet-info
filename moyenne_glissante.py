from transformation import Transformation
from selection import Selection

class Moyenne_Glissante (Transformation) :
    def __init__ (self, dataframe) :
        '''Calcule la série des moyennes glissantes

        Parameters
        ----------
        dataframe : table
            La base de données
        '''
        self.dataframe=dataframe

    def execute(self,colonne,taille_intervalle):
        '''Calcule la série des moyennes glissantes

    Parameters
    ----------
    colonne : list
    taille_intervalle : int

    Returns
    -------
    list

    Examples
    --------
    >>> liste=Moyenne_Glissante([2, 3, 5, 7, 11, 13, 17])
    >>> liste.execute(liste,3)
    [3.3333333333333335, 5.0, 7.666666666666666, 10.333333333333332, 13.666666666666664]
    '''
        data=Selection.execute(colonne)
        moyenne_glissante=[]
        for i in range(len(data)-taille_intervalle):
            for j in range(i,i+taille_intervalle)
                moyenne_glissante[i]=(moyenne_glissante[i]+data[i+j])/taille_intervalle
        self.dataframe.append(moyenne_glissante)
        return self.dataframe

if __name__ == "__main__":
    import doctest
    doctest.testmod()
#A vérifier que ça marche
                
        
