from random import shuffle

from app.mutations import Swap, ReverseSlice, Shuffle


class Chromosome(object):

    MUTATION_TYPES = {
        'swap': Swap,
        'reverse_cut': ReverseSlice,
        'shuffle': Shuffle,
    }

    def __init__(self, length, mutatuion_type):
        self.seq = self._random_chromosome(length)
        print(self.seq)
        self.mutation = self._set_mutation_type(mutatuion_type)

    def __len__(self):
        return len(self.seq)

    def __repr__(self):
        return str(self.seq)

    def __str__(self):
        self.__repr__()

    def mutate(self, range):
        self.seq = self.mutation.mutate(range)

    def _set_mutation_type(self, mutation):
        mut = self.MUTATION_TYPES[mutation]
        return mut(elements=self.seq[:])

    @property
    def length(self):
        return len(self.seq)

    @staticmethod
    def _random_chromosome(size):
        chromosome = [i for i in range(0, size)]
        shuffle(chromosome)
        return chromosome
