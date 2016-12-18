import os
import numpy as np

file_dir = os.path.dirname(os.path.abspath(__file__))


def get_dataset(name: str='att48_d.txt') -> np.array:
    data_dir = os.path.join(file_dir, '../data/')
    dataset_path = os.path.join(data_dir, name)
    with open(dataset_path, 'r') as data_file:
        matrix = []
        for line in data_file.readlines():
            line = _parse_line(line)
            matrix.append(line)
        return np.array(matrix, np.int32)


def _parse_line(line: str) -> list:
    line = line.split(' ')
    line[-1] = line[-1].replace('\n', '')
    line = [int(val) for val in line if val != '']
    return line

default_data_matrix = np.array([
        [0, 6, 7, 3, 4, 5, 6, 5],
        [5, 0, 4, 8, 2, 2, 7, 9],
        [6, 3, 0, 1, 4, 3, 2, 1],
        [2, 3, 5, 0, 1, 4, 2, 2],
        [3, 8, 1, 4, 0, 2, 4, 6],
        [5, 8, 4, 9, 4, 0, 4, 3],
        [3, 6, 7, 4, 7, 2, 0, 6],
        [9, 2, 1, 8, 9, 9, 4, 0],
        ], )


if __name__ == '__main__':
    m = get_dataset()
    print(m)