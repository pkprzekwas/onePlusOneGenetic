import abc


class Mutation(metaclass=abc.ABCMeta):

    def __init__(self, elements: list):
        self.elements = elements

    @abc.abstractmethod
    def mutate(self, range):
        pass


class Algorithm(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def run(self, loops):
        pass

    @abc.abstractmethod
    def criterion_function(self, sequence):
        pass