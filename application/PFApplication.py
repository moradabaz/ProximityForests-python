import json
import sys
import time

sys.path.append(sys.argv[1])
from trees.ProximityForest import ProximityForest

sys.setrecursionlimit(31000)
from core import AppContext, ExperimentRunner
import timeit


class PFApplication:
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
                elif arg == "-output":
                    AppContext.AppContext.output_dir = value
                elif arg == "-targetlast":
                    AppContext.AppContext.target_column_is_first = value
                elif arg == "-ignoreFirst":
                    AppContext.AppContext.ignore_first_col = value
                elif arg == "-edistance":
                    AppContext.AppContext.elastic_distance = value
                elif arg == '-dtw_window':
                    AppContext.AppContext.window_length = int(value)
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
    def save_json():
        name = AppContext.AppContext.dataset_name
        f_path = AppContext.AppContext.output_dir + name + '_' + AppContext.AppContext.elastic_distance + '_' + str(
            time.localtime().tm_hour) + str(time.localtime().tm_min) + str(
            time.localtime().tm_sec) + ".json"
        data = {}
        data_stats = result.exportJSONstats()
        data['dataset'] = []
        data['dataset'].append({
            'name': AppContext.AppContext.dataset_name,
            'n_trees': AppContext.AppContext.num_trees,
            'n_candidates': AppContext.AppContext.num_candidates_per_split,
            'n_repeats': AppContext.AppContext.num_repeats,
            'execution_time': str(stop - start),
            'stats': data_stats
        })
        with open(f_path, 'w+') as file:
            file.write(json.dumps(data))
        file.close()
        return

    @staticmethod
    def save_training():
        name = AppContext.AppContext.dataset_name
        f_path = AppContext.AppContext.output_dir + name + '_' + AppContext.AppContext.elastic_distance + "_" + \
                 str(time.localtime().tm_hour) + str(time.localtime().tm_min) + \
                 str(time.localtime().tm_sec) + ".txt"

        with open(f_path, 'w+') as file:
            stats = result.result_statistics(AppContext.AppContext.dataset_name)
            file.writelines("Dataset: %s\n" % AppContext.AppContext.dataset_name)
            file.writelines("Number of Trees: %s\n" % AppContext.AppContext.num_trees)
            file.writelines("Number of Candidates per tree: %s\n" % AppContext.AppContext.num_candidates_per_split)
            file.writelines("Number of repeats: %s\n" % AppContext.AppContext.num_repeats)
            file.writelines("Elastic distance chosen: %s\n" % AppContext.AppContext.elastic_distance)
            file.writelines("Window lenght: %s\n" % AppContext.AppContext.window_length)
            file.writelines("% s\n" % str(linea) for linea in stats)
            file.writelines("Time: %s\n" % str(stop - start))
            ## file.writelines(stats)
        file.close()

    @staticmethod
    def save_all(pforest: ProximityForest):
        name = AppContext.AppContext.dataset_name

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

    pass


# sys.path.append("/Users/morad/PycharmProjects/PForests/")  # TODO: CHANGE
scenario = PFApplication()
scenario.get_args()

experimentrunner = ExperimentRunner.ExperimentRunner()

# start = timeit.default_timer()
# aqui entrena
# stop = timeit.default_timer()
print("Calculating accuracy using the test....")
print("")
result_lines = list()
AppContext.AppContext.num_repeats = 1
for trees in [20, 35, 50, 75, 100, 120]:
    AppContext.AppContext.num_trees = trees
    for candidates in [2, 3, 4, 5, 6, 7]:
        AppContext.AppContext.num_candidates_per_split = candidates
        start = timeit.default_timer()
        pforest = experimentrunner.run()
        result = pforest.result
        stop = timeit.default_timer()
        linea = str(trees) + ',' + str(candidates) + ',' + str(round(result.accuracy, 5)) + ',' + str(
            round((stop - start), 5))
        result_lines.append(linea)

name = AppContext.AppContext.dataset_name
f_path = AppContext.AppContext.output_dir + name + '_compare_results.csv'
with open(f_path, 'w+') as file:
    stats = result.result_statistics(AppContext.AppContext.dataset_name)
    file.writelines("n_trees,n_candidates,accuracy,exec_time\n")
    file.writelines("%s\n" % str(linea) for linea in result_lines)
    ## file.writelines(stats)
file.close()
