from moyenne import Moyenne

class Variance(Moyenne):
    def __init__(self,variable) -> None:
        self.variable = variable
    
    def calcul_var(self,variable):
        mean = Moyenne.calcul_moy(variable)
        sum=0
        for i in variable:
            sum+=(i-mean)^2
        variance = sum/len(variable)
        return variance
            