import dtw
import unittest
import numpy as np
from distance import DistanceMeasure


class MyTestCase(unittest.TestCase):
    exemplars = [[1.07, 4.85, 1.68, 3.91, 3.09], [1.07, 4.95, 0.68, 4.91, 3.09],
                [4.07, 2.25, 2.98, 3.24, 1.17], [1.2, 4.39, 1.16, 2.77, 1.12],
                [2.89, 1.26, 3.66, 4.38, 4.4], [1.07, 4.85, 1.68, 3.91, 3.09]]

    query = [1.07, 4.85, 1.68, 3.91, 3.19]

    def test_something(self):
        self.assertEqual(True, False)

    def test_dis(self):
        array_query = np.asarray(self.query)
        closest_nodes = list()
        dist = float('inf')
        bsf = float('-inf')

        for i in range(0, len(self.exemplars)):
            exemplar = np.asarray(self.exemplars[i])

            if (exemplar == array_query).all():
                return i
            dist = dtw.accelerated_dtw(array_query, exemplar, 'euclidean')
            for d in dist:
                print("Imprimo:", d)
            print("--------CAMBIO-------")

    def test_find_closest_nodes(self):
        closest_nodes = DistanceMeasure.DistanceMeasure.find_closest_nodes(self.query, self.exemplars)
        self.assertIsNotNone(closest_nodes)
        print(closest_nodes)



if __name__ == '__main__':
    unittest.main()
