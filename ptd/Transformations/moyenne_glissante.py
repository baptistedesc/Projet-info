from ptd.transformations.transformation import Transformation
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
    '''
        k=table.nom_colonnes.index(variable)
        données=table.valeurs[k]
        assert type(table.valeurs[0])!=str
        moyenne_glissante=[0]*(len(table.valeurs[k])-taille_intervalle+1)
        for i in range(len(moyenne_glissante)):
            for j in range(taille_intervalle):
                moyenne_glissante[i]=moyenne_glissante[i]+données[i+j]/taille_intervalle
        table.valeurs.append(moyenne_glissante)
        return table

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    colonnes=['fruits','legumes','age']
    valeurs=[['kiwi','poire','abricot','abricot','abricot'],['haricot','pois','mq','abricot','abricot'],[2,4,6,8,10]]
    table=Table(colonnes,valeurs)
    alpha=Moyenne_Glissante.execute(table,'age',2)
    Table.afficher(alpha)

                
        
