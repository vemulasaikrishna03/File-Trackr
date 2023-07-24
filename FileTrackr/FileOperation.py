from abc import ABC, abstractmethod
import os

class FileOperation(ABC):
    @abstractmethod
    def execute(self):
        pass