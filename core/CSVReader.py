import io
import time

from numpy.distutils.fcompiler import none


class CSVReader:

    @staticmethod
    def getFileInformation(filename, separator=" "):
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
        while len(line) != 0:
            num_lines = num_lines + 1
            if num_columns < len(line.split(separator)):
                num_columns = len(line.split(separator))
            line = file.readline()
        return num_lines, num_columns

    @staticmethod
    def readCSVToListDataset(fileName, targetColumnsIsFirst, separator):
        file = open(fileName, "r")
        print("Reading File:[", fileName, "]")

        return
