from estimateur import Estimateur
import matplotlib.pyplot as plt 

class Boxplot(Estimateur): 
    def __init__(self,dataframe) -> None:
        self.dataframe = dataframe
    

    def execute(self, tableau):
        #Il faut créé un tableau adapté à la création d'un boxplot
        #On prend en compte que le première élément de chaque liste est le nom de la colonne
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

        