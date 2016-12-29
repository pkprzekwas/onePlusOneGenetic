from copy import deepcopy
from math import floor, ceil

from app.data import Dataset
from app.chromosome import Chromosome
from app.result import Results
from app.bases import Algorithm


class Strategy1plus1(Algorithm):

    def __init__(self, mutation_type='reverse_cut', filename='gr17_d.txt', limit=0.2):
        self.results = Results()
        self.limit = limit
        self.data_set = Dataset(filename)
        self.initial_mutation_range = floor(len(self.data_set) / 2)
        self.chromosome = self._create_chromosome(mutation_type)

    def run(self, loops=1000):
        iter_num = 0
        final_iter = 0
        success = 0
        score = self.criterion_function(self.chromosome.seq)
        m_range = self.initial_mutation_range

        while iter_num < loops:
            iter_num += 1

            # 1/5 rule
            ratio = success/iter_num
            m_range = self.get_range(ratio, m_range)

            new_chromosome = deepcopy(self.chromosome)
            new_chromosome.mutate(m_range)
            new_score = self.criterion_function(new_chromosome.seq)

            if new_score <= score:
                score = new_score
                self.chromosome = new_chromosome
                final_iter = iter_num
                success += 1

            self.results.update(iter_num=iter_num, chromosome=self.chromosome.seq, mutated=new_chromosome.seq,
                                score=score, final_iter=final_iter, ratio=ratio, success=success)

    def criterion_function(self, sequence):
        score = 0
        for fenotype in range(len(sequence) - 2):
            score += self.data_set.data[sequence[fenotype]][sequence[fenotype + 1]]
        return score

    def _create_chromosome(self, mutation_type):
        chromosome = Chromosome(length=len(self.data_set), mutatuion_type=mutation_type)
        return chromosome

    def get_range(self, ratio, range):
        if ratio > self.limit:
            range = ceil((0.81 ** (- 1)) * range)
        elif ratio < self.limit:
            if range > ceil(self.chromosome.length / 3):
                range = ceil(0.81 * range)
        else:
            range = range

        if range > self.chromosome.length:
            range = self.chromosome.length
        if range < ceil(self.chromosome.length / 3):
            range = ceil(self.chromosome.length / 3)
        return range

    @staticmethod
    def _count_ratio(success, rounds):
        return float(success) / float(rounds)
