import sys
import json


class JsonToCsv:
    file_name = sys.argv[1]
    file = open(file_name, "r")
    print("Reading File: [", file_name, "]")
    data = json.load(file)
    file.close()

    for (k, v) in data.items():
        print("Key: " + k)
        print("Value: " + str(v))
