from table import Table
class Agregation_temp():
    def __init__(self, table1, table2) :
    '''
    '''
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

    Examples
    --------
    >>> 
    """
    self.table1=table1
    self.table2=table2
    self.nv_donnees=[]
    assert (table1.nom_colonnes==table2.nom_colonnes)
    self.nom_colonnes=table1.nom_colonnes
    self.nv_donnees= table1.variables + table2.variables
    nv_table=Table(self.nom_colonnes,self.nv_donnees)
    return nv_table
