from estimateur import Estimateur

class Sd(Estimateur):
    def __init__(self,variable) -> None:
        self.variable = variable
        self.valeur = self.execute()
    
    def execute(self):
        som=0
        for i in self.variable:
            som+=i
        moyenne = som/len(self.variable)
        sum=0
        for i in self.variable:
            sum+=(i-moyenne)**2
        variance = sum/len(self.variable)
        return variance**(0.5)
