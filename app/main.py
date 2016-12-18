import click
import matplotlib.pyplot as plt


from app.algorithm import OnePlusOne

mutations = {
    'swap': OnePlusOne.swap,
    'reverse_cut': OnePlusOne.rev_list,
    'shuffle': OnePlusOne.shuffle,
}

@click.command()
@click.option('--iter', type=int, prompt='Set number of iterations',
              help='Number of algorithm iterations')
@click.option('--limit', type=float, default=0.5,
              help='\"1/5\" ratio limit')
@click.option('--mutation',
              type=click.Choice(['reverse_cut', 'swap', 'shuffle', 'all']),
              default='reverse_cut',
              help='Mutation type: cut and reverse, swap, shuffle')
@click.option('--to_file', default=False,
              help='Saves output to file')
def run(iter, mutation, to_file, limit):
    if mutation != 'all':
        opo = OnePlusOne()
        mutation_type = mutations[mutation]
        init_route = opo.generate_route()
        opo.run(init_route, mutation=mutation_type, limit=limit, max_iter_num=iter)
        if to_file:
            opo.save_results()
        opo.plot(iter_num=iter)
    else:
        plots = []
        for mutation in mutations.values():
            opo = OnePlusOne()
            mutation_type = mutation
            init_route = opo.generate_route()
            opo.run(init_route, mutation=mutation_type, limit=limit, max_iter_num=iter)
            plots.append(opo)
        rev = plots[0].plot_data(iter_num=iter)
        swp = plots[1].plot_data(iter_num=iter)
        shuf = plots[2].plot_data(iter_num=iter)
        plt.xlabel('Iterations')
        plt.ylabel('Distance')
        plt.title('Traveling Salesman Problem (projekt alg. genetyczne)')
        plt.plot(rev[0], rev[1], 'r', label="cut & reverse")
        plt.plot(swp[0], swp[1], 'b', label="swap")
        plt.plot(shuf[0], shuf[1], 'g', label="shuffle")
        plt.legend(loc=1, borderaxespad=0.)
        plt.show()