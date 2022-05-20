from estimateur import Estimateur
import matplotlib.pyplot as plt 

class Boxplot(Estimateur): 
    def __init__(self,dataframe) -> None:
        '''Construit une boxplot à partir d'une base de données

        Parameters
        ----------
        dataframe : table
            La base de données
        '''     
        self.dataframe = dataframe
    

    def execute(self, tableau):
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
        for i in range(0,len(tableau)):
            row = row+1
            for j in range(1,len(tableau[i])):
                nouveau_tableau.append(tableau[i][j])
                col = col+1
        
        print(col,row)
        row = int(row)
        col = int(col/row)
        NewList = [nouveau_tableau[col*i : col*(i+1)] for i in range(row)]
        print(NewList)
        plt.boxplot(NewList)
        plt.show()

        