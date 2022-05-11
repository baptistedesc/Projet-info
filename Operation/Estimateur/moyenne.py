from estimateur import Estimateur
class Moyenne(Estimateur):
    def __init__(self,variable) -> None:
        self.variable=variable

    def calcul_moy(self,variable):
        som=0
        for i in variable:
            som+=i
        moyenne = som/len(variable)
        return moyenne