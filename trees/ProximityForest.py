import timeit

import numpy as np
from trees import ProximityTree as pt
from core import AppContext as app
from core import PFResult as pfr
from dataStructures import ListDataset
import random

import time


class ProximityForest:

    candidates = app.AppContext.num_candidates_per_split

    def __init__(self, forest_id, max_depth=100, n_trees=100, n_candidates=5):
        app.AppContext.num_candidates_per_split = n_trees
        app.AppContext.num_trees = n_candidates
        self.max_depth = max_depth
        self.max_voted_classes = list()
        self.num_classes_predicted = dict()
        self.forest_id = forest_id
        self.result = pfr.PFResult(self)
        self.trees = list()
        for i in range(0, app.AppContext.num_trees):
            self.trees.append(pt.ProximityTree(i, self))


    """
    In the training method, we train each tree
    """

    def train(self, dataset):
        self.result.start_time_train = timeit.default_timer()
        print("Training dataStructures ...")
        for i in range(0, app.AppContext.num_trees):
            # print("training tree number ", i)
            self.trees[i].train(dataset)
            # print("training tree number ", self.trees[i].time_best_splits)
        self.result.end_time_train = timeit.default_timer()
        self.result.elapsed_time_train = self.result.end_time_train - self.result.start_time_train

    """
    Testing function.
    Having a ListDataset:
    We get the serie list of each class, we try to predict the class
    and compare it with its actual class
    """

    def test(self, test_data: ListDataset):
        self.result.start_time_test = timeit.default_timer()
        for label in test_data.classes:
            self.num_classes_predicted[label] = 0
        self.max_voted_classes = list()
        size = test_data.get_series_size()
        for i in range(0, size):
            actual_class = test_data.get_class(i)
            predicted_class = self.predict(test_data.series_data[i])
            if actual_class != predicted_class:
                self.result.errors = self.result.errors + 1
            else:
                self.result.correct = self.result.correct + 1
        self.result.end_time_test = timeit.default_timer()
        self.result.elapsed_time_test = self.result.end_time_test - self.result.start_time_test
        if app.AppContext.verbosity > 0:
            print()
        assert test_data.get_series_size() == self.result.errors + self.result.correct
        self.result.accuracy = np.double(self.result.correct) / test_data.get_series_size()
        self.result.error_rate = 1 - self.result.accuracy
        return self.result

    def get_trees(self):
        return self.trees

    def set_trees(self, trees):
        self.trees = trees

    def get_tree(self, i):
        return self.trees[i]

    def get_result_set(self):
        return self.result

    def get_forest_stat_collection(self):
        self.result.collate_results()
        return self.result

    def get_forest_ID(self):
        return self.forest_id

    def set_forest_ID(self, forest_id):
        self.forest_id = forest_id

    def print_results(self, dataset_name: str, experiment_id: int, prefix: str):
        self.result.print_results(dataset_name, experiment_id, prefix)

    def calculate_simple_query(self, query_serie):
        print(np.array(query_serie).tolist())
        self.predict(np.array(query_serie).tolist())

    """
    Each tree is used to predict the class of the query.
    :returns Random most predicted class
    """

    def predict(self, query):
        max_predicted_class_count = -1
        for predicted_class in self.num_classes_predicted.keys():
            self.num_classes_predicted[predicted_class] = 0
        self.max_voted_classes.clear()

        for tree in self.trees:
            predicted_class = tree.predict(query)
            if not self.num_classes_predicted.keys().__contains__(predicted_class):
                self.num_classes_predicted[predicted_class] = 0
            else:
                self.num_classes_predicted[predicted_class] = self.num_classes_predicted[predicted_class] + 1

        for predicted_class in self.num_classes_predicted.keys():
            predict_class_count = self.num_classes_predicted[predicted_class]
            if predict_class_count > max_predicted_class_count:
                max_predicted_class_count = predict_class_count
                self.max_voted_classes.clear()
                self.max_voted_classes.append(predicted_class)
            elif predict_class_count == max_predicted_class_count:
                self.max_voted_classes.append(predicted_class)
        r = random.randrange(self.max_voted_classes.__len__())
        if self.max_voted_classes.__len__() > 1:
            self.result.majority_vote_match_count = self.result.majority_vote_match_count + 1
        return self.max_voted_classes.__getitem__(r)

    def run_data(self, train_data_original, test_data_original, name):
        self.train_data = train_data_original.reorder_class_labels(None)
        self.test_data = test_data_original.reorder_class_labels(self.train_data.initial_class_labels)
        self.series_length = len(self.train_data.series_data[0])
        app.AppContext.training_dataset = self.train_data
        app.AppContext.testing_dataset = self.test_data
        app.AppContext.series_length = self.series_length
        num_repeats = app.AppContext.num_repeats

        if app.AppContext.verbosity > 0:
            print("Number of repeats:", app.AppContext.num_repeats)
            print("Number of trees:")
            print("Experimenting...")
        else:
            print("This is ...")

        print("Creating Proximity Forest in repeat", self.forest_id)

        app.AppContext.num_train_series = self.train_data.get_series_size()

        self.train(self.train_data)

        print("Testing process...")
        app.AppContext.num_test_series = self.test_data.get_series_size()
        self.result = self.test(self.test_data)

        self.print_results(name, self.forest_id, "")
        if app.AppContext.export_level > 0:
            self.result.exportJSON(name, self.forest_id)
        return self

    pass
