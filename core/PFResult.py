from trees import ProximityForest
from core import AppContext as app
import datetime, time
import statistics as st
import os
import json


class PFResult:
    results_collated = False
    forest_id = -1
    majority_vote_match_count = 0

    start_time_train = 0
    end_time_train = 0
    elapsed_time_train = 0

    start_time_test = 0
    end_time_test = 0
    elapsed_time_test = 0

    errors = 0
    correct = 0
    accuracy = 0
    error_rate = 0

    total_num_trees = -1

    mean_num_nodes_per_tree = -1
    sd_num_nodes_per_tree = -1

    mean_depth_per_tree = -1
    sd_depth_per_tree = -1

    mean_weighted_depth_per_tree = -1
    sd_weighted_depth_per_tree = -1

    def __init__(self, forest: ProximityForest):
        self.forest_id = forest.forest_id
        self.forest = forest

    def collate_results(self):
        nodes = [None] * self.total_num_trees
        depths = [None] * self.total_num_trees
        weighted_depth = [None] * self.total_num_trees
        if self.results_collated:
            return
        trees = self.forest.get_trees()
        total_num_trees = len(trees)

        for i in range(0, total_num_trees):
            tree = trees[i]
            tree_stats = tree.get_tree_stat_collection()
            nodes[i] = tree_stats.num_nodes
            depths[i] = tree_stats.depth
            weighted_depth[i] = tree_stats.weighted_path

        self.mean_num_nodes_per_tree = st.mean(nodes)
        self.sd_num_nodes_per_tree = st.pstdev(nodes)

        self.mean_depth_per_tree = st.mean(depths)
        self.sd_depth_per_tree = st.pstdev(depths)

        self.mean_weighted_depth_per_tree = st.mean(weighted_depth)
        self.sd_weighted_depth_per_tree = st.pstdev(weighted_depth)

        self.results_collated = True

    def print_results(self, dataset_name: str, experiment_id: int, prefix: str):
        if app.AppContext.verbosity > 0:
            time_duration = time.localtime(self.elapsed_time_train)
            print("Training time:", self.elapsed_time_train, "(", time_duration, ")")
            print("Correct(TP+TN):", self.correct, "incorrect(FP+FN)", self.errors)
            print("Accuracy:", self.accuracy)

        self.collate_results()

        pre = "REPEAT" + (experiment_id + 1) + " ,"
        print(pre, dataset_name)
        print(",", self.accuracy)
        print(",", self.elapsed_time_train / 1e6)
        print(",", self.elapsed_time_test / 1e6)
        print(",", self.mean_depth_per_tree)
        print()

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
    pass
