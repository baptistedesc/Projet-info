from Graphiques.graphique import Graphique
import matplotlib.pyplot as plt 

class Nuagedepoints(Graphique): 
    def __init__(self) -> None:
        '''Construit un nuage de points à partir d'une base de données

        Parameters
        ----------
       
        '''     
       

    def execute(self, col1, col2, table):
        indice1 = table.nom_colonnes.index(col1)
        indice2 = table.nom_colonnes.index(col2)

        plt.scatter(table.valeurs[indice1],table.valeurs[indice2])
        plt.show()

