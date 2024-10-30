from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class MixinInfo:

    def __init__(self, *args, **kwargs):
        super().__repr__()
        print(repr(self))


    def __repr__(self):
        return f"{self.__class__.__name__}, ({self.name}, {self.description}, {self.price}, {self.quantity})"
