from operation import Operation
from abc import ABC, abstractmethod

class Graphique(Operation,ABC):
    @abstractmethod
    def execute():
        pass
