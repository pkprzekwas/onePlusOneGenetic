from random import shuffle, randint

from app.bases import Mutation


class Swap(Mutation):
    """
    Swaps two elements from beginning of the list.
    User must specify the range of elements exposed
    for mutation.
    
    Example:
        -> elem = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        -> s = Swap(elements=elem, range=4)
        -> elem = s.mutate()
        -> print(elem)
            [1, 4, 3, 2, 5, 6, 7, 8, 9]

    """
    def __init__(self, elements: list):
        super().__init__(elements)

    def mutate(self, range):
        a = randint(1, range - 1)
        b = randint(1, range - 1)
        while a == b:
            b = randint(1, range - 1)
        self.elements[b], self.elements[a] = \
            self.elements[a], self.elements[b]
        return self.elements


class ReverseSlice(Mutation):
    """
    Reverse a slice of a list.
    User must specify the range of elements exposed
    for mutation.

    Example:
        -> elem = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        -> rs = ReverseSlice(elements=elem, range=8)
        -> elem = rs.mutate()
        -> print(elem)
            [1, 2, 7, 6, 5, 4, 3, 8, 9]

    """
    def __init__(self, elements: list):
        super().__init__(elements)

    def mutate(self, range):
        a = randint(0, range)
        b = randint(0, range)
        while a == b:
            b = randint(0, range)
        return self._reverse_sublist(min(a, b), max(a, b))

    def _reverse_sublist(self, start, end):
        self.elements[start:end] = self.elements[start:end][::-1]
        return self.elements


class Shuffle(Mutation):
    """
    Shuffle all elements from provided list.
    """
    def __init__(self, elements: list):
        super().__init__(elements)

    def mutate(self, range=None):
        shuffle(self.elements)
        return self.elements
