from sklearn.metrics import jaccard_similarity_score
from ptd.table import Table

class Agregation_temp():
    '''
    Examples
    -----------------
    >>> nom_colonnes=['fruits','légumes']
    >>> valeurs1=[['pomme','poire'],['haricot','pois']]
    >>> valeurs2=[['fraise','framboise'],['poireau','tomate']]
    >>> valeurs3=[['pomme','poire','fraise','framboise'],['haricot','pois','poireau','tomate']]
    >>> table1=table(nom_colonnes,valeurs1)
    >>> table2=table(nom_colonnes,valeurs2)
    >>> Agregation_temp.execute(table1,table2)
    table(nom_colonnes,valeurs3)
    '''
    def __init__(self, table1) :
        """Concatène des bases de données contenant les mêmes colonnes
        Utile notamment pour constituer une seule base de données à partir de plusieurs fichiers concernant le même sujet, mais découpés dans le temps (ex : les relevés météo par mois)
        Parameters
        ----------
        table1 : Dataframe
            Base de données 1
        table2 : Dataframe
            Base de données 2

        Returns
        -------
        Dataframe
        """
        self.table1=table1

    def execute(self,table2):
        self.nv_donnees=[]
        assert (self.table1.nom_colonnes==table2.nom_colonnes)
        for i in range(len(self.table1.valeurs)):
            for j in range(len(table2.valeurs[i])):
                self.table1.valeurs[i].append(table2.valeurs[i][j])
        self.nv_donnees= self.table1.valeurs + table2.valeurs
        nv_table=Table(self.table1.nom_colonnes,self.nv_donnees)
        return nv_table


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)


