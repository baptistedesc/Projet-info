from ptd.estimateurs.estimateur import Estimateur

class Sd(Estimateur):
#C'est bizarre, pourquoi ici tu prends une variable en entrée et pas le dataframe comme d'habitude pour après selectionner la variable (en fait pour tous les estimateurs)    
    def __init__(self) -> None:
        '''Calcul l'écart-type d'une variable

        Parameters
        ----------
      
        '''
    
    def execute(self,colonne, table):
        '''Calcule l'écart-type

        -------
        float
            L'écart-type demandé
        ''' 
        
        indice = table.nom_colonnes.index(colonne)
        moyenne = 0
        somme = 0
        for k in range(0,len(table.valeurs[indice])):
            somme = table.valeurs[indice][k] + somme
        moyenne=somme/(len(table.valeurs[indice]))
        

        sum=0
        for h in range(0,len(table.valeurs[indice])):
            sum+=(table.valeurs[indice][h]-moyenne)**2
        variance = sum/len(table.valeurs[indice])
        return variance**(0.5)
