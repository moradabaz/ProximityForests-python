import sys
#sys.path.append("/Users/morad/PycharmProjects/PForests/")  # TODO: CHANGE
sys.path.append(sys.argv[1])
import time
import timeit
from datetime import date
from math import inf
from dtaidistance import dtw
from numpy import double
from trees.ProximityForest import ProximityForest
from core import AppContext, ExperimentRunner
import numpy as np


class ScenarioOne:
    query_file = ""
    type = 1
    time_start = 0
    time_stop = 0
    AppContext.AppContext.output_dir = "../outputs/"

    def __init__(self):
        self.appcontext = AppContext.AppContext(train_dataset="/Users/morad/PycharmProjects/PForests/util/tabla1.csv",
                                                test_dataset="/Users/morad/PycharmProjects/PForests/util/tabla1.csv")

    def get_app_context(self):
        return self.appcontext

    def get_args(self):
        if len(sys.argv) > 1:
            for i in range(2, len(sys.argv)):
                options = sys.argv[i].split("=")
                arg = options[0]
                value = options[1]
                if arg == "-name":
                    AppContext.AppContext.dataset_name = value
                elif arg == "-syspath":
                    sys.path.append(value)
                elif arg == "-train":
                    AppContext.AppContext.training_file = value
                elif arg == "-test":
                    AppContext.AppContext.testing_file = value
                elif arg == "-repeat":
                    AppContext.AppContext.num_repeats = int(value)
                elif arg == "-trees":
                    AppContext.AppContext.num_trees = int(value)
                elif arg == "-candidates":
                    AppContext.AppContext.num_candidates_per_split = int(value)
                elif arg == "-output":
                    AppContext.AppContext.output_dir = value
                elif arg == "-targetlast":
                    AppContext.AppContext.target_column_is_first = value
                elif arg == "-calculate":
                    value = value.upper().lower()
                    if value == "accuracy":
                        self.type = 0
                    elif value == "all":
                        self.type = 2
                    else:
                        self.type = 1
                elif arg == "-query_file":
                    if self.type == 1:
                        self.query_file = value

    @staticmethod
    def read_query_path(query):
        with open(query, 'r') as f:
            x = f.readlines()
        f.close()
        return x

    @staticmethod
    def save_training():
        f_path = ""
        name = AppContext.AppContext.dataset_name
        if type == 1:
            f_path = AppContext.AppContext.output_dir + name + '_' + 'query' + str(date.today()) + "_" + str(
                time.localtime().tm_hour) + "-" + str(time.localtime().tm_min) + "-" + str(
                time.localtime().tm_sec) + ".txt"
        else:
            f_path = AppContext.AppContext.output_dir + name + '_' + 'accuracy' + str(date.today()) + "_" + \
                     str(time.localtime().tm_hour) + "-" + str(time.localtime().tm_min) + "-" + \
                     str(time.localtime().tm_sec) + ".txt"

        with open(f_path, 'w+') as file:
            stats = result.result_statistics(AppContext.AppContext.dataset_name)
            file.writelines("Dataset: %s\n" % AppContext.AppContext.dataset_name)
            file.writelines("Number of Trees: %s\n" % AppContext.AppContext.num_trees)
            file.writelines("Number of Candidates per tree: %s\n" % AppContext.AppContext.num_candidates_per_split)
            file.writelines("Number of repeats: %s\n" % AppContext.AppContext.num_repeats)
            file.writelines("% s\n" % str(linea) for linea in stats)
            file.writelines("Time: %s\n" % str(stop - start))
            ## file.writelines(stats)
        file.close()

    @staticmethod
    def save_all(pforest: ProximityForest):
        name = AppContext.AppContext.dataset_name
        f_path = AppContext.AppContext.output_dir + name + '_' + 'results' + str(date.today()) + "_" + \
                 str(time.localtime().tm_hour) + "-" + str(time.localtime().tm_min) + "-" + \
                 str(time.localtime().tm_sec) + ".txt"

        result = pforest.result
        with open(f_path, 'w+') as file:
            stats = result.result_statistics(AppContext.AppContext.dataset_name)
            file.writelines("Dataset: %s\n" % AppContext.AppContext.dataset_name)
            file.writelines("Number of Trees: %s\n" % AppContext.AppContext.num_trees)
            file.writelines("Number of Candidates per tree: %s\n" % AppContext.AppContext.num_candidates_per_split)
            file.writelines("Number of repeats: %s\n" % AppContext.AppContext.num_repeats)
            file.writelines("% s\n" % str(linea) for linea in stats)
            file.writelines("Time: %s\n" % str(stop - start))
            file.writelines("\n")
        file.close()

    @staticmethod
    def classify_best_serie(query: list, pforest: ProximityForest):
        lista = query[0]
        print(lista)
        lista = lista.split(" ")
        query = list()
        for q in lista:
            query.append(double(q))
        print(query)
        label = pforest.predict(query)
        print(label)
        lista = experimentrunner.train_data.get_series_from_label(label)
        num_series = len(lista)
        best_dist = inf
        best_serie_id = -1
        for i in range(0, num_series):
            serie = lista[i]
            dist = dtw.distance_fast(np.asarray(query), np.asarray(serie))
            if dist < best_dist:
                best_dist = dist
                best_serie_id = i
        print("QUERY")
        print(query)
        print("Series aproximate:", best_serie_id)
        print(lista[best_serie_id])
        print("Dist: ", best_dist)

        name = AppContext.AppContext.dataset_name
        f_path = name + '_' + 'query' + str(date.today()) + "_" + str(
            time.localtime().tm_hour) + "-" + str(time.localtime().tm_min) + "-" + str(
            time.localtime().tm_sec) + ".txt"

        with open(f_path, 'w+') as file:
            file.writelines("Dataset: %s\n" % AppContext.AppContext.dataset_name)
            file.writelines("Number of Trees: %s\n" % AppContext.AppContext.num_trees)
            file.writelines("Number of Candidates per tree: %s\n" % AppContext.AppContext.num_candidates_per_split)
            file.writelines("Number of repeats: %s\n" % AppContext.AppContext.num_repeats)
            file.writelines("Query: ")
            file.writelines("%s " % q for q in query)
            file.writelines("\n")
            file.writelines("Best serie id: %s \n" % best_serie_id)
            file.writelines("Most similar serie: [ ")
            file.writelines("%s " % q for q in lista[best_serie_id])
            file.writelines(" ] \n")
            file.writelines("DTW distance: %s\n" % best_dist)
        file.close()

    pass

sys.path.append("/Users/morad/PycharmProjects/PForests/")  # TODO: CHANGE
scenario = ScenarioOne()
scenario.get_args()

experimentrunner = ExperimentRunner.ExperimentRunner()

# start = timeit.default_timer()
# aqui entrena
# stop = timeit.default_timer()
if scenario.type == 0:
    print("Calculating accuracy using the test dataStructures....")
    start = timeit.default_timer()
    pforest = experimentrunner.run()
    result = pforest.result
    stop = timeit.default_timer()
    scenario.save_training()

elif scenario.type == 2:
    print("Calculating accuracy using the test dataStructures....")
    start = timeit.default_timer()
    result = experimentrunner.run()
    stop = timeit.default_timer()
    scenario.save_all(pforest=result)
elif scenario.type == 1:
    pforest = experimentrunner.load_traindata()
    print("Opening query file...")
    query = scenario.read_query_path(query=scenario.query_file)
    print("Query loaded...")
    scenario.classify_best_serie(query, pforest)
