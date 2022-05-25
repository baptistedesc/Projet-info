from ptd.table import Table
class Agregation_temp():
    def __init__(self, table1, table2) :
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

    def execute(self):
        self.nv_donnees=[]
        assert (self.table1.nom_colonnes==self.table2.nom_colonnes)
        self.nom_colonnes=self.table1.nom_colonnes
        self.nv_donnees=self.table1.variables + self.table2.variables
        nv_table=Table(self.nom_colonnes,self.nv_donnees)
        return nv_table

    nom_colonnes1=['fruits','légumes']
    valeurs1=[[1,2],[3,4]]
    Ex1=Table(nom_colonnes1,valeurs1)
    nom_colonnes2=['fruits','légumes']
    valeurs2=[[18,54],[45,36]]
    Ex2=Table(nom_colonnes2,valeurs2)
    print(Ex1)
    print(Ex2)
    result=Agregation_temp(Ex1,Ex2)
    result.execute()
    print(result)