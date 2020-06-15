from trees import ProximityForest
from core import AppContext as app
import time
import statistics as st
import os
import json
import numpy as np
from core import AppContext


class PFResult:

    def __init__(self, forest: ProximityForest):
        self.forest_id = forest.forest_id
        self.forest = forest
        self.results_collated = False
        self.forest_id = -1
        self.majority_vote_match_count = 0

        self.start_time_train = 0
        self.end_time_train = 0
        self.elapsed_time_train = 0

        self.start_time_test = 0
        self.end_time_test = 0
        self.elapsed_time_test = 0

        self.errors = 0
        self.correct = 0
        self.accuracy = 0
        self.error_rate = 0

        self.total_num_trees = -1

        self.mean_num_nodes_per_tree = -1
        self.sd_num_nodes_per_tree = -1

        self.mean_depth_per_tree = -1
        self.sd_depth_per_tree = -1

        self.mean_weighted_depth_per_tree = -1
        self.sd_weighted_depth_per_tree = -1

        self.num_train_series = AppContext.AppContext.num_train_series
        self.num_test_series = AppContext.AppContext.num_test_series

    def collate_results(self):
        nodes = list()
        depths = list()
        weighted_depth = list()
        if self.results_collated:
            return
        trees = self.forest.get_trees()

        for tree in trees:
            tree_stats = tree.get_treestat_collection()
            nodes.append(tree_stats.num_nodes)
            depths.append(tree_stats.depth)
            weighted_depth.append(tree_stats.weighted_depth)

        self.mean_num_nodes_per_tree = st.mean(np.asarray(nodes))
        self.sd_num_nodes_per_tree = st.pstdev(np.asarray(nodes))

        self.mean_depth_per_tree = st.mean(np.asarray(depths))
        self.sd_depth_per_tree = st.pstdev(np.asarray(depths))

        self.mean_weighted_depth_per_tree = st.mean(np.asarray(weighted_depth))
        self.sd_weighted_depth_per_tree = st.pstdev(np.asarray(weighted_depth))

        self.results_collated = True

    def print_results(self, dataset_name: str, experiment_id: int, prefix: str):
        if app.AppContext.verbosity > 0:
            time_duration = time.localtime(self.elapsed_time_train)
            print("Training time:", self.elapsed_time_train, "(", time_duration, ")")
            print("Correct(TP+TN):", self.correct, "incorrect(FP+FN)", self.errors)
            print("Accuracy:", self.accuracy)

        self.collate_results()

        pre = "REPEAT: " + str((experiment_id + 1)) + " ,"
        print(pre, dataset_name)
        print(", accuracy", self.accuracy)
        print(", elapsed time train", self.elapsed_time_train / 1e6)
        print(", elapsed time test", self.elapsed_time_test / 1e6)
        print(", mean depth tree", self.mean_depth_per_tree)
        print()

    def result_statistics(self, dataset_name):
        time_duration = time.localtime(self.elapsed_time_train)
        resultados = list()
        self.collate_results()
        result = "Train series number: " + str(AppContext.AppContext.num_train_series)
        resultados.append(result)
        result = "Test series number: " + str(AppContext.AppContext.num_test_series)
        resultados.append(result)
        result = "Correct (TP+TN): " + str(self.correct)
        resultados.append(result)
        result = "Incorrect (FP+FN): " + str(self.errors)
        resultados.append(result)
        result = 'Accuracy: ' + str(self.accuracy)
        resultados.append(result)
        result = "elapsed time train: " + str(self.elapsed_time_train)
        resultados.append(result)
        result = "elapsed time test: " + str(self.elapsed_time_test)
        resultados.append(result)

        return resultados

    def exportJSON(self, dataset_name, experiment_id):
        file = ""
        timestamp = time.asctime().split()
        hora = time.asctime().split()[3].split(":")
        timestamp = timestamp[1] + "_" + timestamp[2] + "_" + hora[0] + "-" + hora[1] + "-" + hora[2]

        file_path = app.AppContext.output_dir + os.path.sep + self.forest_id + timestamp + ".json"
        file = None
        json_string = json.dumps(self)
        try:
            file = open(file_path, "w+")
            file.write(json_string)
            file.close()
        except:
            print("Error: Could create file ")
            return

        return file_path

    @staticmethod
    def get_list_from_dict(query: dict):
        lista = list()
        for entry in query.values():
            lista.append(entry)
        return lista

    pass
