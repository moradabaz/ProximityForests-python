import unittest
from core.FileReader import CSVReader as reader
from dataset.ListDataset import ListDataset
import numpy as np

class MyTestCase(unittest.TestCase):

    data_standard_italy = reader.readCSVToListDataset(
        "/Users/morad/Desktop/resultados/ItalyPowerDemandAlt/ItalyPowerDemand_TRAIN.ts", has_header=False, labelLastColumn=True, separator=",")
    data_arff_italy = reader.read_file("/Users/morad/Desktop/resultados/ItalyPowerDemand/ItalyPowerDemand_TRAIN.arff")

    data_standard_plane = reader.readCSVToListDataset("/Users/morad/Desktop/resultados/PlaneAlt/Plane_TEST.ts", has_header=False, labelLastColumn=True)
    data_arff_plane = reader.read_file("/Users/morad/Desktop/resultados/PlaneAlt/Plane_TEST.arff")

    def test_something(self):
        self.assertEqual(True, False)

    def test_number_series_italy(self):
        series_data_std = self.data_standard_italy.series_data
        series_data_arff = self.data_arff_italy.series_data
        self.assertEqual(len(series_data_std), len(series_data_arff))

    def test_series_last_italy(self):
        series_data_std = self.data_standard_italy.series_data
        series_data_arff = self.data_arff_italy.series_data
        print("Series standard", series_data_std[len(series_data_std) - 1])
        print("Series arff", series_data_arff[len(series_data_arff) - 1])

    def test_check_series_italy(self):
        series_data_std = self.data_standard_italy.series_data
        series_data_arff = self.data_arff_italy.series_data
        for i in range(0, 66):
            if not np.array_equal(series_data_std[i], series_data_arff[i]):
                print("serie standard: ", series_data_std[i])
                print("serie arff: ", series_data_arff[i])
                print("Posicion: ", i)

        print("Series standard", series_data_std[len(series_data_std) - 1])
        print("Series arff", series_data_arff[len(series_data_arff) - 1])

    def test_find_serie_in_other_italy(self):
        series_data_std = self.data_standard_italy.series_data
        series_data_arff = self.data_arff_italy.series_data
        for serie in series_data_std:
            for i in range(0, len(series_data_arff)):
                if serie == series_data_arff[i]:
                    print("Serie found in posicion", i)

    def test_series_map_italy(self):
        series_data_std = self.data_standard_italy.series_map
        series_data_arff = self.data_arff_italy.series_map
        self.assertEqual(series_data_std.keys(), series_data_arff.keys())

    def test_series_map_italy_vals(self):
        series_data_std = self.data_standard_italy.series_map
        series_data_arff = self.data_arff_italy.series_map
        for key in series_data_std.keys():
            self.assertEqual(len(series_data_std[key]), len(series_data_arff[key]))

    def test_series_map_italy_vals_2(self):
        series_data_std = self.data_standard_italy.series_map
        series_data_arff = self.data_arff_italy.series_map
        for key in series_data_std.keys():
            print("CLAVE: ", key)
            for i in range(0, len(series_data_std[key])):
                print("Serie standard:", series_data_std[key][i])
                print("Serie     arff:", series_data_arff[key][i])

    def test_number_plane(self):
        series_data_std = self.data_standard_plane.series_data
        series_data_arff = self.data_arff_plane.series_data
        self.assertEqual(len(series_data_std), len(series_data_arff))

    def test_number_series_plane(self):
        series_data_std = self.data_standard_plane.series_map
        series_data_arff = self.data_arff_plane.series_map
        for key in series_data_std.keys():
            print("CLAVE: ", key)
            for i in range(0, len(series_data_std[key])):
                print("Serie standard:", series_data_std[key][i])
                print("Serie     arff:", series_data_arff[key][i])






if __name__ == '__main__':
    unittest.main()
