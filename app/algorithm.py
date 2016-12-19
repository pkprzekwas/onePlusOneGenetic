from random import shuffle, randint
import matplotlib.pyplot as plt
import click

from app.data import get_dataset


class OnePlusOne(object):
    """

    Implementation of (1+1) genetic strategy.

    """

    def __init__(self):
        self.results = {}
        self.load_data()

    def load_data(self, file_name='att48_d.txt'):
        self.dataset = get_dataset(file_name)

    def run(self, route, mutation, limit=0.2, mutations=25, max_iter_num=1000):
        distance = self.count_distance(route=route)
        iter_num = 0
        final_iter = 0
        success = 0
        m_size = self.get_matrix_size()

        while iter_num < max_iter_num:
            iter_num += 1

            # 1/5 rule
            ratio = self.count_ratio(success, iter_num)
            if ratio > limit:
                mutations = int(((0.81)**-1)*mutations) if mutations < m_size else m_size
            elif ratio < limit and mutations > 1:
                if mutations > 5:
                    mutations = int((0.81)*mutations) if mutations < m_size else m_size
            else:
                mutations = mutations

            # mutations
            if mutations > m_size:
                mutations = m_size
            if mutations < 5:
                mutations = 5
            new_route = mutation(route=route[:], mut_range=mutations)
            for i in range(0, 3):
                new_route = mutation(route=new_route[:], mut_range=mutations)
            new_distance = self.count_distance(route=new_route)

            if new_distance <= distance:
                distance = new_distance
                route = new_route
                final_iter = iter_num
                success += 1

            self.save(iter_num=iter_num, route=route, mutated=new_route,
                      distance=distance, final_iter=final_iter, mutations=mutations, success=success)

    def save(self, *, iter_num, route, mutated, distance, final_iter, mutations, success):
        self.results[iter_num] = {
            "route": route,
            "mutated": mutated,
            "distance": distance,
            "final_iter": final_iter,
            "mutations": mutations,
            "success": success,
            "repr": "\tIteration: {}\n\tRoute: {}\n\tMutated: {}\n\tDistance: {}\tFinal iteration: {}"
                    "\tMutations: {}\tSuccesses: {}\n"
                .format(iter_num, route, mutated, distance, final_iter, mutations, success),
            "repr_less": "\t\tIteration: {}\t\tDistance: {}\t\tFinal iteration: {}"
                    "\t\tMutations: {}\t\t\tSuccesses: {}"
                .format(iter_num, distance, final_iter, mutations, success)
        }

    def plot(self, iter_num):
        x = []
        y = []
        max_dist = self.results[1]["distance"]
        min_dist = self.results[iter_num]["distance"]

        for key, val in self.results.items():
            x.append(key)
            y.append(val["distance"])
        click.echo("\n\n{}\n\n".format(self.results[iter_num]["repr"]))
        plt.plot(x, y)
        plt.axis([1, iter_num, min_dist, max_dist])
        plt.show()

    def plot_data(self, iter_num):
        x = []
        y = []
        max_dist = self.results[1]["distance"]
        min_dist = self.results[iter_num]["distance"]

        for key, val in self.results.items():
            x.append(key)
            y.append(val["distance"])
        return x, y, max_dist, min_dist

    def print_results(self):
        for key, val in self.results.items():
            click.echo((val["repr_less"]))

    def save_results(self):
        file = open('out.txt', 'w')
        for key, val in self.results.items():
            file.write("{}\n".format(val["repr"]))
        file.close()

    def generate_route(self):
        route = [i for i in range(0, self.get_matrix_size())]
        shuffle(route)
        return route

    def count_distance(self, route):
        distance = 0
        for city in range(len(route) - 1):
            distance += self.dataset[route[city]][route[city + 1]]
        return distance

    def get_matrix_size(self):
        matrix_shape = self.dataset.shape
        return matrix_shape[0]

    @classmethod
    def count_ratio(cls, success, rounds):
        return float(success) / float(rounds)

    @classmethod
    def swap(cls, route, mut_range):
        a = randint(1, mut_range-1)
        b = randint(1, mut_range-1)
        while a == b:
            b = randint(1, mut_range-1)
        route[b], route[a] = route[a], route[b]
        return route

    @classmethod
    def rev_list(cls, route, mut_range):
        a = randint(0, mut_range)
        b = randint(0, mut_range)
        while a == b:
            b = randint(0, mut_range)
        return reverse_sublist(route, a, b)

    @classmethod
    def shuffle(cls, route, mut_range):
        shuffle(route)
        return route


def reverse_sublist(lst, start, end):
    lst[start:end] = lst[start:end][::-1]
    return lst

