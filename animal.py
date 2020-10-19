from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

    def move(self):
        pass
