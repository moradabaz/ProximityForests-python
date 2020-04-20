from numpy import double

from trees import ProximityTree as pt
from core import AppContext as app
from core import PFResult as pfr
from dataset import ListDataset
import random
import time


class ProximityForest:

    def __init__(self, forest_id):
        self.max_voted_classes = list()
        self.num_votes = dict()
        self.forest_id = forest_id
        self.result = pfr.PFResult(self)
        self.trees = list()
        counter = 0
        for i in range(0, app.AppContext.num_trees):
            self.trees.append(pt.ProximityTree(i, self))

    def train(self, dataset):
        # result.startTimeTrain
        self.result.start_time_train = time.time()

        for i in range(0, app.AppContext.num_trees):
            self.trees[i].train(dataset)
            if app.AppContext.verbosity > 0:
                print(i, ".")
                if app.AppContext.verbosity > 1:
                    if ((i + 1) % 20) == 0:
                        print("")

        # fala implementar ProximityResult
        self.result.end_time_train = time.time()
        self.result.elapsed_time_train = self.result.end_time_train - self.result.start_time_train

        # print memory usages

    def test(self, test_data: ListDataset):
        self.result.start_time_train = time.time()
#        self.num_votes = [int] * len(test_data.initial_class_labels)
        for label in test_data.labels:
            self.num_votes[label] = 0

        self.max_voted_classes = list()
        predicted_class = -1
        actual_class = -1
        size = test_data.get_series_size()

        for i in range(0, size):
            actual_class = test_data.get_class(i)
            predicted_class = self.predict(test_data.series_data.__getitem__(i))
            if actual_class != predicted_class:
                self.result.errors = self.result.errors + 1
            else:
                self.result.correct = self.result.correct + 1

            if app.AppContext.verbosity > 0:
                if (i % app.AppContext.print_test_progress_for_each_instances) == 0:
                    print("*")
        self.result.end_time_test = time.time()
        self.result.elapsed_time_test = self.result.end_time_test - self.result.start_time_test

        if app.AppContext.verbosity > 0:
            print()
        assert test_data.get_series_size() == self.result.errors + self.result.correct
        self.result.accuracy = double(self.result.correct) / test_data.get_series_size()
        self.result.error_rate = 1 - self.result.accuracy
        return self.result

    def get_trees(self):
        return self.trees

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

    pass

    def _predict(self, query):
        label = 0
        counter = 0
        max_vote_count = -1
        temp_count = 0
        for label in self.num_votes.keys():
            self.num_votes[label] = 0

        self.max_voted_classes.clear()
        for tree in self.trees:
            label = tree.predict(query)
            if label == -1:
                continue
            if not self.num_votes.keys().__contains__(label):
                self.num_votes[label] = 0
            else:
                self.num_votes[label] = self.num_votes[label] + 1

        for label in self.num_votes:
            if self.num_votes[label] > 0:
                temp_count = self.num_votes[label]
                if temp_count > max_vote_count:
                    max_vote_count = temp_count
                    self.max_voted_classes.clear()
                    self.max_voted_classes.append(label)
                elif temp_count == max_vote_count:
                    self.max_voted_classes.append(label)

        r = random.randint(0, self.max_voted_classes.__len__() - 1)

        if len(self.max_voted_classes) > 1:
            self.result.majority_vote_match_count = self.result.majority_vote_match_count + 1

        return self.max_voted_classes[r]

    def predict(self, query):
        label = -1
        max_vote_count = -1
        temp_count = 0
        for label in self.num_votes.keys():
            self.num_votes[label] = 0
        self.max_voted_classes.clear()

        for tree in self.trees:
            label = tree.predict(query)
            if not self.num_votes.keys().__contains__(label):
                self.num_votes[label] = 0
            else:
                self.num_votes[label] = self.num_votes[label] + 1

        for label in self.num_votes.keys():
            temp_count = self.num_votes[label]
            if temp_count > max_vote_count:
                max_vote_count = temp_count
                self.max_voted_classes.clear()
                self.max_voted_classes.append(label)
            elif temp_count == max_vote_count:
                self.max_voted_classes.append(label)

        r = random.randrange(self.max_voted_classes.__len__())
        if self.max_voted_classes.__len__() > 1:
            self.result.majority_vote_match_count = self.result.majority_vote_match_count + 1
        return self.max_voted_classes.__getitem__(r)

        pass
