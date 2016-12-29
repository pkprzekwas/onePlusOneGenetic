import click

from app.algorithm import Strategy1plus1


@click.option('--iter',
              type=int, prompt='Set number of iterations',
              help='Number of algorithm iterations')
@click.option('--limit',
              type=float, default=0.2,
              help='\"1/5\" ratio limit')
@click.option('--mutation',
              type=click.Choice(['reverse_cut', 'swap', 'shuffle']),
              default='reverse_cut',
              help='Mutation type: cut and reverse, swap, shuffle')
@click.option('--to_file',
              type=click.BOOL,
              default=False, help='Saves output to file')
@click.command()
def run(iter, mutation, to_file, limit):
    """

    1+1 genetic strategy.

    """
    strategy = Strategy1plus1(
        mutation_type=mutation,
        limit=limit,
        filename='att48_d.txt'
    )

    strategy.run(loops=iter)

    if to_file:
        strategy.results.save()
    strategy.results.plot(iter_num=iter)


### LEFT FOR LOCAL DEBUGGING ###

#  if __name__ == '__main__':
#     run(iter=1000, mutation='reverse_cut', to_file=False, limit=0.2)


