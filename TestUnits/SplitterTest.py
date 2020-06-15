from dataStructures import ListDataset
from trees import Splitter
import unittest
import numpy as np
from trees import Node
from util import randomNumbers as rnumbers

class MyTestCase(unittest.TestCase):
    dataset1 = ListDataset.ListDataset()
    splitter = Splitter.Splitter(None)

    datos1 = [12.32, 0.45, 4.55, 9.55]
    datos2 = [3.44, 0.67, 9.22, 0.001]
    datos3 = [9.22, 0.001, 4.22, 1.22]
    datos4 = [3.23, 8.23, 6.44, 1.34]
    datos5 = [2.64, 8.34, 1.11, 1.24]

    datos6 = [0.8, 0.9, 0.22, 0.35]
    datos7 = [0.79, 0.58, 0.24, 0.4]
    datos8 = [0.29, 0.59, 0.41, 0.88]
    datos9 = [3.44, 0.67, 9.22, 0.001]
    datos10 = [0.15, 0.45, 0.93, 0.72]

    dataset1.add_series("Hola", datos1)
    dataset1.add_series("Mundo", datos2)
    dataset1.add_series("Como", datos3)
    dataset1.add_series("Estas", datos4)

    def test_split_data(self):
        listdataset = ListDataset.ListDataset()
        listdataset.add_series(0, self.datos1)
        listdataset.add_series(1, self.datos2)
        listdataset.add_series(2, self.datos3)
        listdataset.add_series(3, self.datos4)
        listdataset.add_series(4, self.datos5)

        listdataset2 = ListDataset.ListDataset()
        listdataset2.add_series(0, self.datos6)
        listdataset2.add_series(1, self.datos7)
        listdataset2.add_series(2, self.datos8)
        listdataset2.add_series(3, self.datos9)
        listdataset2.add_series(4, self.datos10)

        data_per_class = list()
        data_per_class.append(listdataset)
        data_per_class.append(listdataset2)

        splits = self.splitter.split_data(self.dataset1, data_per_class)
        for spt in splits:
            print("Vamos")
            print(spt.series_data)


    def test_find_closest_branch(self):
        datos1 = [12.32, 0.45, 4.55, 9.55]
        datos2 = [3.44, 0.67, 9.22, 0.001]
        datos3 = [9.22, 0.001, 4.22, 1.22]
        datos4 = [3.23, 8.23, 6.44, 1.34]
        datos = list()
        datos.append(datos1)
        datos.append(datos2)
        datos.append(datos3)
        datos.append(datos4)
        temp_exemplar = np.asarray(datos)
        serie = [2.64, 8.34, 1.11, 1.24]
        splitters = self.splitter.find_closest_branch(serie, temp_exemplar)
        print(splitters)

    def test_find_closest_branch2(self):
        dt_list = rnumbers.randomNumbers.create_multiple_datasets(6, 5)
        serie = rnumbers.randomNumbers.generate_random_array(5)
        temp_exemplar = np.asarray(dt_list[0].series_data)
        splitters = self.splitter.find_closest_branch(serie, temp_exemplar.__array__())
        print(splitters)

    def test_split_classes(self):
        dt_list = rnumbers.randomNumbers.create_multiple_datasets(6, 5)
        serie = rnumbers.randomNumbers.generate_random_array(5)
        for dt in dt_list:
            print("> best splits")
            best_splits = self.splitter.find_best_splits(dt)
            for split in best_splits:
                print(split.series_data)

    def test_gini(self):
        listdataset = ListDataset.ListDataset()
        listdataset.add_series(0, self.datos1)
        listdataset.add_series(1, self.datos2)
        listdataset.add_series(2, self.datos3)
        listdataset.add_series(3, self.datos4)
        listdataset.add_series(4, self.datos5)

        listdataset2 = ListDataset.ListDataset()
        listdataset2.add_series(0, self.datos6)
        listdataset2.add_series(1, self.datos7)
        listdataset2.add_series(2, self.datos8)
        listdataset2.add_series(3, self.datos9)
        listdataset2.add_series(4, self.datos10)

        data_per_class = list()
        data_per_class.append(listdataset)
        data_per_class.append(listdataset2)

        splits = self.splitter.split_data(self.dataset1, data_per_class)
        self.assertLessEqual(self.splitter.weighted_gini(10, splits), 0.5)

    def test_find_best_splits(self):
        listdataset = ListDataset.ListDataset()
        listdataset.add_series(0, self.datos1)
        listdataset.add_series(1, self.datos2)
        listdataset.add_series(2, self.datos3)

        best_splits = self.splitter.find_best_splits(listdataset)
        self.assertIsNotNone(best_splits)
        for split in best_splits:
            print("Split")
            for serie in split.series_data:
                print(serie)


if __name__ == '__main__':
    unittest.main()
