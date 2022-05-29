from operation import Operation
from abc import ABC, abstractmethod

class Transformation(ABC):
    @abstractmethod
    def execute():
        pass

