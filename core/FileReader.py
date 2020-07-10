import time
from numpy import double
from scipy.io import arff
from dataStructures import ListDataset


class FileReader:

    @staticmethod
    def read_file(fileName, has_header=True, labelLastColumn=True, separator=","):
        file = fileName.split(".")[1]
        if file == "arff" or file == "ts":
            return FileReader.load_arff_data(fileName)
        return FileReader.readCSVToListDataset(fileName, has_header, labelLastColumn, False, separator)

    @staticmethod
    def readCSVToListDataset(fileName, has_header=True, labelLastColumn=True, ignore_first_column=False, separator=","):
        try:
            file = open(fileName, "r")
            print("Reading File: [", fileName, "]")
        except:
            print("File Not Found: [", fileName, "]")
            return
        start = time.time()
        dataset = ListDataset.ListDataset()
        line = file.readline()
        line.strip()
        line.rstrip()
        line.lstrip()
        num_line = 0
        if has_header:
            line = file.readline()
        while len(line) > 0:
            label = 0
            line_array = line.split(separator)
            series = list()
            if ignore_first_column:
                index = 1
            else:
                index = 0
            if labelLastColumn:
                serie_length = len(line_array) - 1
            else:
                serie_length = len(line_array)

            for j in range(index, serie_length):
                try:
                    series.append(double(line_array[j]))
                except:
                    print("Problem with", line_array[j])
                    continue
            if labelLastColumn:
                try:
                    label = int(line_array[serie_length].split("\n")[0])
                except:
                    label = line_array[serie_length].split("\n")[0]
            if label is not None:
                dataset.add_series(label, series)
            num_line = num_line + 1
            line = file.readline()
        end = time.time()

        elapsed = end - start
        print("parsing process finished in", elapsed, "seconds")
        file.close()
        return dataset

    @staticmethod
    def load_data(full_data_path):
        f = open(full_data_path)
        print("FICHERO:", f)
        data, meta = arff.loadarff(f)
        f.close()
        return data

    @staticmethod
    def load_arff_data(fullpath):
        try:
            file = FileReader.load_data(fullpath)
            print("Reading File: [", fullpath, "]")
        except:
            print("File Not Found: [", fullpath, "]")
            return
        start = time.time()
        dataset = ListDataset.ListDataset()
        tam_series = len(file)
        for i in range(0, tam_series):
            serie_lenth = len(file[i])
            if serie_lenth <= 0:
                continue
            try:
                class_label = int(file[i][serie_lenth - 1])
            except:
                class_label = file[i][serie_lenth - 1]
            serie = list()
            for j in range(0, serie_lenth - 1):
                try:
                    serie.append(double(file[i][j]))
                except:
                    continue
            dataset.add_series(class_label, serie)
        end = time.time()
        elapsed = end - start
        print("finished in", elapsed, "seconds")
        return dataset


    @staticmethod
    def parse_arff_data(file):
        start = time.time()
        dataset = ListDataset.ListDataset()
        tam_series = len(file)
        for i in range(0, tam_series):
            serie_lenth = len(file[i])
            if serie_lenth <= 0:
                continue
            try:
                class_label = int(file[i][serie_lenth - 1])
            except:
                class_label = file[i][serie_lenth - 1]
            serie = list()
            for j in range(0, serie_lenth - 1):
                try:
                    serie.append(double(file[i][j]))
                except:
                    continue
            dataset.add_series(class_label, serie)
        end = time.time()
        elapsed = end - start
        print("finished in", elapsed, "seconds")
        return dataset