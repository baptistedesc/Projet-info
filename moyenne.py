from estimateur import Estimateur



class Moyenne(Estimateur):
    def __init__(self,variable) -> None:
        '''Calcule la moyenne d'une variable

        Parameters
        ----------
        variable : list
            La variable
        '''
        self.variable=variable
        self.valeur = self.execute()

    def execute(self):
        som=0
        for i in self.variable:
            som+=i
        moyenne = som/len(self.variable)
        return moyenne

    