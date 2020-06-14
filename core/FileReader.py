import time
from numpy import double
from scipy.io import arff
from dataset import ListDataset

from numpy.distutils.fcompiler import none


class FileReader:


    @staticmethod
    def read_file(fileName, has_header=False, labelLastColumn=False, separator=" "):
        file = fileName.split(".")[1]
        if file == "arff" or file == "ts":
            return FileReader.load_arff_data(fileName)
        return FileReader.readCSVToListDataset(fileName, has_header, labelLastColumn, separator)

    @staticmethod
    def readCSVToListDataset(fileName, has_header, labelLastColumn=False, separator=","):
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
            if labelLastColumn:
                line_array = line.split(":")
                try:
                    label = int(line_array[1].split("\n")[0])
                except:
                    label = line_array[1]
                line_array = line_array[0].split(separator)
            else:
                line_array = line.split(separator)

            series = list()
            for j in range(0, len(line_array)):
                try:
                    series.append(double(line_array[j]))
                except:
                    continue
            if not labelLastColumn:
                label = abs(int(double(line_array[len(series) - 1])))
            if label != none:
                dataset.add_series(label, series)
            num_line = num_line + 1
            line = file.readline()
        end = time.time()
        elapsed = end - start
        print("finished in", elapsed, "seconds")
        file.close()
        print("Dataset Series:", dataset.get_series_size())
        print("Dataset Labels:", dataset.get_labels())
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
