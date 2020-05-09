import sys
import time
import timeit
from datetime import date

from numpy import double

sys.path.append("/Users/morad/PycharmProjects/PForests/")
from core import AppContext, ExperimentRunner
import numpy as np


class ScenarioOne:
    query_file = ""
    type = 1

    def __init__(self):
        self.appcontext = AppContext.AppContext(train_dataset="/Users/morad/PycharmProjects/PForests/util/tabla1.csv",
                                                test_dataset="/Users/morad/PycharmProjects/PForests/util/tabla1.csv")

    def get_app_context(self):
        return self.appcontext

    def get_args(self):
        if len(sys.argv) > 1:
            for i in range(1, len(sys.argv)):
                # print(sys.argv[i])
                options = sys.argv[i].split("=")
                arg = options[0]
                value = options[1]
                if arg == "-name":
                    self.appcontext.dataset_name = value
                elif arg == "-train":
                    self.appcontext.training_file = value
                elif arg == "-test":
                    self.appcontext.testing_file = value
                elif arg == "-repeat":
                    self.appcontext.num_repeats = value
                elif arg == "-trees":
                    self.appcontext.num_trees = value
                elif arg == "-candidates":
                    self.appcontext.num_candidates_per_split = value
                elif arg == "-output":
                    self.appcontext.output_dir = value
                elif arg == "-calculate":
                    value = value.upper().lower()
                    if value == "accuracy":
                        self.type = 0
                    else:
                        self.type = 1
                elif arg == "-query_file":
                    if self.type == 1:
                        self.query_file = value

    def save(self):
        f_path = ""
        name = self.appcontext.dataset_name
        if type == 1:
            f_path = name + '_' + 'query' + str(date.today()) + "_" + str(
                time.localtime().tm_hour) + "-" + str(time.localtime().tm_min) + "-" + str(
                time.localtime().tm_sec) + ".txt "
        else:
            f_path = name + '_' + 'accuracy' + str(date.today()) + "_" + \
                     str(time.localtime().tm_hour) + "-" + str(time.localtime().tm_min) + "-" + \
                     str(time.localtime().tm_sec) + ".txt "

        with open(f_path, 'w+') as file:
            stats = result.result_statistics(self.appcontext.dataset_name)
            file.writelines("Dataset: %s\n" % self.appcontext.dataset_name)
            file.writelines("Number of Trees: %s\n" % self.appcontext.num_trees)
            file.writelines("Number of Candidates per tree: %s\n" % self.appcontext.num_candidates_per_split)
            file.writelines("Number of repeats: %s\n" % self.appcontext.num_repeats)
            file.writelines("% s\n" % str(linea) for linea in stats)
            # file.writelines(stats)
        file.close()

    pass


scenario = ScenarioOne()
scenario.get_args()

experimentrunner = ExperimentRunner.ExperimentRunner()
pforest = experimentrunner.load_traindata()
# start = timeit.default_timer()
# aqui entrena
# stop = timeit.default_timer()
if scenario.type == 0:
    print("Calculating accuracy using the test dataset....")
    start = timeit.default_timer()
    result = experimentrunner.run()
    top = timeit.default_timer()
    scenario.save()
