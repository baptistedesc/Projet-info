from ptd.transformations.transformation import Transformation

class Centrage (Transformation) :
    def __init__ (self, dataframe) :
        '''Centre une variable

        Parameters
        ----------
        dataframe : table
            La base de données
        '''
        
        self.dataframe=dataframe

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
        
        for i in range(len(self.dataframe)) :
            if str(self.dataframe[i][0])==colonne :
                somme=0
                moyenne=0
                for k in range(1,len(self.dataframe[i])):
                    somme = somme + self.dataframe[i][k]
                moyenne=somme/(len(self.dataframe[i])-1)
                for j in range(1,len(self.dataframe[i])):
                    self.dataframe[i][j]=self.dataframe[i][j] - moyenne
        return self.dataframe
