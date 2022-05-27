from Estimateurs.estimateur import Estimateur


class Variance(Estimateur):
#C'est bizarre, pourquoi ici tu prends une variable en entrée et pas le dataframe comme d'habitude pour après selectionner la variable (en fait pour tous les estimateurs)    
    def __init__(self) -> None:
        '''Calcule la variance d'une variable

        Parameters
        ----------
        
        '''
    
    def execute(self,colonne,table):
        '''Calcule la variance

        -------
        float
            La variance demandée
        ''' 
        

        indice = table.nom_colonnes.index(colonne)
        moyenne = 0
        somme = 0
        for k in range(0,len(table.valeurs[indice])):
            somme = table.valeurs[indice][k] + somme
        moyenne=somme/(len(table.valeurs[indice]))
        

        sum=0
        for h in range(0,table.valeurs[indice]):
            sum+=(table.valeurs[indice][h]-moyenne)**2
        variance = sum/len(table.valeurs[indice])
        return variance
