import io
import time

from numpy import double

from dataset import ListDataset

from numpy.distutils.fcompiler import none


class CSVReader:

    @staticmethod
    def getFileInformation(filename, has_header=False, separator=" "):
        line_array = []
        file = none
        length_check = True
        num_lines = 0
        num_columns = 0
        try:
            file = open(filename, "r")
        except:
            print("[ERROR]", "File", filename, "Not Found")
            return
        line = file.readline()
        length_check = True
        while len(line) != 0:
            num_lines = num_lines + 1
            if length_check:
                length_check = False
                line_array = line.split(separator)
            line = file.readline()

        if has_header:
            if num_lines > 0:
                num_lines = num_lines - 1
        num_columns = len(line_array)
        file.close()
        return num_lines, num_columns

    @staticmethod
    def readCSVToListDataset(fileName, has_header, targetColumnsIsFirst=True, separator=" "):
        file = none
        try:
            file = open(fileName, "r")
            print("Reading File:[", fileName, "]")
        except:
            print("File Not Found:[", fileName, "]")
            return
        start = time.time()
        file_info = CSVReader.getFileInformation(fileName, has_header, separator)
        expected_size = file_info[0]
        data_length = file_info[1] - 1
        dataset = ListDataset.ListDataset(expected_size, 0)

        line = file.readline()
        num_line = 0
        while len(line) > 0:
            line_array = line.split(separator)
            series = list()
            if targetColumnsIsFirst:
                init_index = 1
            else:
                init_index = 0
            for j in range(init_index, len(line_array)):
                series.append(double(line_array[j]))
            try:
                if init_index == 1:
                    label = line_array[0]
                else:
                    label = num_line
            except:
                label = none

            if label != none:
                dataset.add_series(label, series)
            num_line = num_line + 1
            line = file.readline()

            # TODO: IMPLEMENT MEMORY STATS

        end = time.time()
        elapsed = end - start
        print("finished in", elapsed, "seconds")
        file.close()
        return dataset
