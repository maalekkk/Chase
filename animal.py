from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        pass
