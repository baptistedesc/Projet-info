from transformation import Transformation
from selection import Selection

class Moyenne_Glissante (Transformation) :
    def __init__ (self, dataframe) :
        self.dataframe=dataframe

    def execute(self,colonne,taille_intervalle):
        data=Selection.execute(colonne)
        moyenne_glissante=[]
        for i in range(len(data)-taille_intervalle):
            for j in range(i,i+taille_intervalle)
                moyenne_glissante[i]=(moyenne_glissante[i]+data[i+j])/taille_intervalle
        self.dataframe.append(moyenne_glissante)
        return self.dataframe
                
        
