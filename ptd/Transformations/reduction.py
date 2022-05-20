from ptd.transformations.transformation import Transformation
from cmath import sqrt
from statistics import variance

class Reduction(Transformation):
    def __init__(self, dataframe) -> None:
        '''Reduit certaines variables d'une base de données 

        Parameters
        ----------
        dataframe : table
            La base de données
        '''
        self.dataframe = dataframe


    def execute(self, colonne) :
        for i in range(len(self.dataframe)) :
            if str(self.dataframe[i][0])==str(colonne) :
                moyenne = 0
                somme = 0
                ecart_moyenne_carre = 0
                somme_ecarts_carre = 0
                for k in range(1,len(self.dataframe[i])):
                    somme = somme + self.dataframe[i][k]
                    moyenne=somme/(len(self.dataframe[i])-1)
                for k in range(1,len(self.dataframe[i])):
                    ecart_moyenne_carre=(self.dataframe[i][k]-moyenne)**2
                    somme_ecarts_carre= somme_ecarts_carre + ecart_moyenne_carre
                    variance=somme_ecarts_carre/(len(self.dataframe[i])-1)
                    ecart_type=sqrt(variance)
                for k in range(1,len(self.dataframe[i])):
                    self.dataframe[i][k]=self.dataframe[i][k]/ecart_type
        return self.dataframe
