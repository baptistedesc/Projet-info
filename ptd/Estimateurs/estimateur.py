from ptd.operation import Operation
from abc import ABC, abstractmethod

class Estimateur(Operation,ABC):
    @abstractmethod
    def execute():
        pass
