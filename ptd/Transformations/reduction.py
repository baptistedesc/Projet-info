from ptd.transformations.transformation import Transformation
from cmath import sqrt
from statistics import variance

class Reduction(Transformation):
    def __init__(self, table) -> None:
        '''Reduit certaines variables d'une base de données 

        Parameters
        ----------
        table : table
            La base de données
        '''
        self.table = table


    def execute(self, colonne) :
        for i in range(len(self.table)) :
            if str(self.table[i][0])==str(colonne) :
                moyenne = 0
                somme = 0
                ecart_moyenne_carre = 0
                somme_ecarts_carre = 0
                for k in range(1,len(self.table[i])):
                    somme = somme + self.table[i][k]
                    moyenne=somme/(len(self.table[i])-1)
                for k in range(1,len(self.table[i])):
                    ecart_moyenne_carre=(self.table[i][k]-moyenne)**2
                    somme_ecarts_carre= somme_ecarts_carre + ecart_moyenne_carre
                    variance=somme_ecarts_carre/(len(self.table[i])-1)
                    ecart_type=sqrt(variance)
                for k in range(1,len(self.table[i])):
                    self.table[i][k]=self.table[i][k]/ecart_type
        return self.table
