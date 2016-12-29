import os

class Dataset(object):
    """
    The object exists to handle data import
    from a file. User is expected to put data
    file to 'data/' directory of this project.

    Format example show below:

      0 633 257  91 412 150  80
    633   0 390 661 227 488 572
    257 390   0 228 169 112 196
     91 661 228   0 383 120  77
    412 227 169 383   0 267 351
    150 488 112 120 267   0  63
     80 572 196  77 351  63   0

    By default object will use 'gr17_d.txt' file.
    """

    FILE_DIR = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, filename: str='gr17_d.txt'):
        self.name = filename
        self.path = self._get_path()
        self.data = self._get_data()

    def __len__(self):
        return len(self.data)

    def _get_data(self) -> list:
        with open(self.path, 'r') as data_file:
            matrix = []
            for line in data_file.readlines():
                line = self._parse_line(line)
                matrix.append(line)
            return matrix

    def _get_path(self) -> str:
        data_dir = os.path.join(self.FILE_DIR, '../data/')
        dataset_path = os.path.join(data_dir, self.name)
        return dataset_path

    @staticmethod
    def _parse_line(line: str) -> list:
        line = line.split(' ')
        line[-1] = line[-1].replace('\n', '')
        line = [int(val) for val in line if val != '']
        return line
