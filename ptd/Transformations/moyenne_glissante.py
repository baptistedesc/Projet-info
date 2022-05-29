from ptd.transformations.transformation import Transformation
from ptd.transformations.selection import Selection
from ptd.table import Table

class Moyenne_Glissante (Transformation) :
    def __init__ (self) :
        pass

    def execute(table,variable,taille_intervalle):
        '''Calcule la série des moyennes glissantes d'une variable

    Parameters
    ----------
    variable : le nom de la variable
    taille_intervalle : int

    Returns
    -------
    list
        La série des moyennes glissantes

    Examples
    --------
    >>> liste=Moyenne_Glissante([2, 3, 5, 7, 11, 13, 17])
    >>> Moyenne_Glissante.execute(liste,3)
    [3.3333333333333335, 5.0, 7.666666666666666, 10.333333333333332, 13.666666666666664]
    '''
        k=table.nom_colonnes.index(variable)
        data=table.valeurs[k]
        assert type(table.valeurs[0])!=str
        moyenne_glissante=[]
        for i in range(len(data)-taille_intervalle):
            for j in range(i,i+taille_intervalle):
                moyenne_glissante[i]=(moyenne_glissante[i]+data[i+j])/taille_intervalle
        table.append(moyenne_glissante)
        return table

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    colonnes=['fruits','legumes','age']
    valeurs=[['kiwi','poire','abricot'],['haricot','pois','mq'],[1,2,3]]
    table=Table(colonnes,valeurs)
    table.afficher(Moyenne_Glissante.execute(table,'age',2))

                
        
