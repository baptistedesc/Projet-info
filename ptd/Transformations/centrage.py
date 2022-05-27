from ptd.transformations.transformation import Transformation

class Centrage (Transformation) :
    def __init__ (self, table) :
        '''Centre une variable

        Parameters
        ----------
        table : table
            La base de données
        '''
        
        self.table=table

    def execute(self,colonne) :
        '''Centre la variable demandée 

        Parameters
        ----------
        colonne : str
            Le nom de la variable à centrer

        Returns
        -------
        table
            La base de données initiale, avec la variable en question centrée
        ''' 
        
        for i in range(len(self.table)) :
            if str(self.table[i][0])==colonne :
                somme=0
                moyenne=0
                for k in range(1,len(self.table[i])):
                    somme = somme + self.table[i][k]
                moyenne=somme/(len(self.table[i])-1)
                for j in range(1,len(self.table[i])):
                    self.table[i][j]=self.table[i][j] - moyenne
        return self.table
