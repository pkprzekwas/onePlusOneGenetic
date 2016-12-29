import click
import matplotlib.pyplot as plt


class Results(object):

    def __init__(self):
        self.data = {}

    def update(self, *, iter_num, chromosome, mutated, score, final_iter, ratio, success):
        self.data[iter_num] = {
            "chromosome": chromosome,
            "mutated": mutated,
            "score": score,
            "final_iter": final_iter,
            "ratio": ratio,
            "success": success,
            "repr": "\tIteration: {}"
                    "\n\tRoute: {}"
                    "\n\tMutated: {}"
                    "\n\tDistance: {}"
                    "\tFinal iteration: {}"
                    "\tRatio: {}"
                    "\tSuccesses: {}\n"
                    .format(iter_num, chromosome, mutated, score, final_iter, ratio, success),
            "repr_less": "\t\tIteration: {}"
                         "\t\tScore: {}"
                         "\t\tFinal iteration: {}"
                         "\t\tRatio: {}"
                         "\t\t\tSuccesses: {}"
                         .format(iter_num, score, final_iter, ratio, success)
        }

    def save(self):
        file = open('out.txt', 'w')
        for key, val in self.data.items():
            file.write("{}\n".format(val["repr"]))
        file.close()

    def print(self):
        for key, val in self.data.items():
            click.echo((val["repr_less"]))

    def plot(self, iter_num):
        x = []
        y = []
        max_dist = self.data[1]["score"]
        min_dist = self.data[iter_num]["score"]

        for key, val in self.data.items():
            x.append(key)
            y.append(val["score"])
        click.echo("\n\n{}\n\n".format(self.data[iter_num]["repr"]))
        plt.xlabel('Iterations')
        plt.ylabel('Distance')
        plt.title('Traveling Salesman Problem (projekt alg. genetyczne)')
        plt.plot(x, y)
        plt.axis([1, iter_num, min_dist, max_dist])
        plt.show()

    def get_plot_data(self, iter_num):
        x = []
        y = []
        max_dist = self.data[1]["distance"]
        min_dist = self.data[iter_num]["distance"]

        for key, val in self.data.items():
            x.append(key)
            y.append(val["distance"])
        return x, y, max_dist, min_dist
