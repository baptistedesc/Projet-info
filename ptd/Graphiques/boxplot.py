from venv import create
from ptd.graphiques.graphique import Graphique
import matplotlib.pyplot as plt 

class Boxplot(Graphique): 
    def __init__(self) -> None:
        '''Construit une boxplot à partir d'une base de données

    
        '''     


    def execute(self, colonnes, table):
        '''Affiche le boxplot

        Parameters
        ----------
        tableau : table
            Le tableau qu'on veut représenter sous forme de boxplot, il doit être adapté à cette opération (seulement des variables quantitatives) 

        Returns
        -------
        ????????????????????????????????????
        
        '''
        #Ajouter un test pour vérifier que le tableau est adapté aux boxplots ?
        #On peut pas mettre des return à la fin pour qu'on puisse faire direct boxplot.execute(data) au lieu de print(boxplot.execute(data))
        #On ne prend en compte que le premier élément de chaque liste et le nom de la colonne
        nouveau_tableau = []
        row = 0
        col = 0
        def createList(name):#Permet d'avoir le nom des colonnes comme nom des clés d'un dictionnaire
            result = {}
            for i in range(len(name)):
               nameList = name[i]
               result[nameList] = []
            return result
        dico = createList(colonnes)

        for i in range(0,len(colonnes)):#Permet de remplir le dictionnaire avec les valeurs de chaques colonnes
            indice = table.nom_colonnes.index(colonnes[i])
            dico[colonnes [i]] = table.valeurs[indice]

        
        plt.boxplot([dico[x] for x in dico.keys()], labels = dico.keys())
        plt.show()

        