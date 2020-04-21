import unittest
from core import CSVReader
from dataset import ListDataset


class MyTestCase(unittest.TestCase):
    file_name1 = "/Users/morad/PycharmProjects/PForests/util/tabla1.csv"
    file_name2 = "/Users/morad/PycharmProjects/PForests/util/tabla2.csv"
    file_name3 = "/Users/morad/PycharmProjects/PForests/util/tabla3.csv"
    file_name4 = "/Users/morad/PycharmProjects/PForests/util/tabla4.csv"
    tabla_1 = open(file_name1)
    tabla_2 = open(file_name2)
    tabla_3 = open(file_name3)
    tabla_4 = open(file_name4)

    def test_read_file1(self):
        line = self.tabla_1.readline()
        while len(line) > 0:
            print(line)
            line = self.tabla_1.readline()

    def test_read_file(self):
        file_info = CSVReader.CSVReader.getFileInformation(filename="this", separator=" ")



    def test_read_file2(self):
        line = self.tabla_2.readline()
        while len(line) > 0:
            print(line)
            line = self.tabla_2.readline()

    def test_read_file3(self):
        line = self.tabla_3.readline()
        while len(line) > 0:
            print(line)
            line = self.tabla_3.readline()

    def test_num_columns1(self):
        file_info = CSVReader.CSVReader.getFileInformation(filename=self.file_name1, separator=" ")
        self.assertEqual(file_info[1], 5)
        self.assertEqual(file_info[0], 10)

    def test_num_columns2(self):
        file_info = CSVReader.CSVReader.getFileInformation(filename=self.file_name2, has_header=True, separator=" ")
        self.assertEqual(file_info[1], 4)
        self.assertEqual(file_info[0], 10)

    def test_num_columns4(self):
        file_info = CSVReader.CSVReader.getFileInformation(filename=self.file_name4, has_header=True, separator=" ")
        self.assertEqual(file_info[1], 5)
        self.assertEqual(file_info[0], 10)

    # Comprobaciones con el dataset

    def test_dataset_labels(self):
        dataset = CSVReader.CSVReader.readCSVToListDataset(fileName=self.file_name1, has_header=False, targetColumnsIsFirst=True, separator=" ")
        print(len(dataset.labels))
        for i in dataset.series_data:
            print(i)
        for j in dataset.labels:
            print(j)

    def test_dataset_labels2(self):
        dataset = CSVReader.CSVReader.readCSVToListDataset(fileName=self.file_name2, has_header=True,targetColumnsIsFirst=False, separator=" ")
        print(len(dataset.labels))
        for i in dataset.series_data:
            print(i)
        for j in dataset.labels:
            print(j)

    def test_dataset_labels3(self):
        train_dataset = CSVReader.CSVReader.readCSVToListDataset(fileName="/Users/morad/Downloads/ItalyPowerDemand/ItalyPowerDemand_TRAIN.csv", has_header=False, targetColumnsIsFirst=False, separator=",")
        test_dataset = CSVReader.CSVReader.readCSVToListDataset(fileName="/Users/morad/Downloads/ItalyPowerDemand/ItalyPowerDemand_TEST.csv", has_header=False, targetColumnsIsFirst=False, separator=",")

        print(len(train_dataset.labels))
        for i in train_dataset.series_data:
            print(i)
        for j in test_dataset.labels:
            print(j)


if __name__ == '__main__':
    unittest.main()
