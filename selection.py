from transformation import Transformation
import numpy as np

class Selection(Transformation):
    def __init__(self, dataframe) -> None:
        self.dataframe = dataframe
  

    def execute(self,colonne):
        dataframe2 = np.array(self.dataframe)
        indice = (np.where(colonne==dataframe2)[0][0])
        return dataframe2[indice]