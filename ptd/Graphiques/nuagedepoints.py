from ptd.graphiques.graphique import Graphique
import matplotlib.pyplot as plt 

class Nuagedepoints(Graphique): 
    def __init__(self,dataframe) -> None:
        '''Construit un nuage de points à partir d'une base de données

        Parameters
        ----------
        dataframe : table
            La base de données
        '''     
        self.dataframe = dataframe

    def execute(self):
