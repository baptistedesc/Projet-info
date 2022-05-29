from Transformations.transformation import Transformation
from cmath import sqrt
from statistics import variance
from table import Table

class Reduction(Transformation):
    def __init__(self) -> None:
        pass

    def execute(self, colonne, table) :
        
        indice = table.nom_colonnes.index(colonne)
        moyenne = 0
        somme = 0
        ecart_moyenne_carre = 0
        somme_ecarts_carre = 0
        for k in range(0,len(table.valeurs[indice])):
            somme = table.valeurs[indice][k]
        moyenne=somme/(len(table.valeurs[indice]))
        for k in range(0,len(table.valeurs[indice])):
                ecart_moyenne_carre=(k - moyenne)**2
                somme_ecarts_carre= somme_ecarts_carre + ecart_moyenne_carre
                variance=somme_ecarts_carre/(len(table.valeurs[indice])-1)
                ecart_type=sqrt(variance) 
        for k in range(0,len(table.valeurs[indice])):

            table.valeurs[indice][k] = table.valeurs[indice][k]/ecart_type
        return table


