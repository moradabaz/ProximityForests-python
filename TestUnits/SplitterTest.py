from dataset import ListDataset
from trees import Splitter
import unittest


class MyTestCase(unittest.TestCase):

    dataset1 = ListDataset.ListDataset()
    splitter = Splitter.Splitter()

    def test_something(self):
        self.assertEqual(True, False)

    def test_split_data(self):
        datos1 = [12.32, 0.45, 4.55, 9.55]
        datos2 = [3.44, 0.67, 9.22, 0.001]
        datos3 = [3.44, 0.67, 9.22, 0.001, 4.22, 1.22]
        self.dataset1.series_data.append(datos1)
        self.dataset1.series_data.append(datos2)
        self.dataset1.series_data.append(datos3)

if __name__ == '__main__':
    unittest.main()
