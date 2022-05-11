from variance import Variance
class Sd:
    def __init__(self,variable) -> None:
        self.variable = variable
    
    def calcul_sd(self,variable):
        variance = Variance.calcul_var(variable)
        return variance^(1/2)