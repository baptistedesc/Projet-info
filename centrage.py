from transformation import Transformation

class Centrage (Transformation) :
    def __init__ (self, dataframe) :
        self.dataframe=dataframe

    def execute(self,colonne) :
        
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
