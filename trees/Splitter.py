import dtw
from distance import DistanceMeasure as dm
from dataset import ListDataset
from core import AppContext
import random


class Splitter:

    def __init__(self, node):
        self.num_children = None
        self.temp_exemplars = None
        self.node = node
        self.best_splits = None
        self.exemplars = None

    def split_data(self, sample, data_per_class):
        splits = ListDataset.ListDataset(sample.get_num_classes())
        temp_exemplars = sample.get_num_classes()
        branch = 0
        r = None
        for entry in data_per_class.keys():
            r = random.randint(data_per_class[entry])
            splits[branch] = ListDataset.ListDataset(sample.expected_size, 0)
            self.temp_exemplars[branch] = data_per_class[entry].get_series(r)
            branch = branch + 1

        # this
        sample_size = sample.expected_size
        for j in range(0, sample_size):
            closest_branch = Splitter.find_closest_branch_(sample.get_series[j], temp_exemplars)
            if closest_branch == -1:
                assert False
            splits[closest_branch].add_series(sample.get_class(j), sample.get_series(j))
        return splits

    @staticmethod
    def find_closest_branch(query, e):
        return dm.DistanceMeasure.find_closest_nodes(query, e)

    def find_closest_branch_(self, query):
        return dm.DistanceMeasure.find_closest_nodes(query, self.exemplars)

    def get_best_splits(self):
        return self.best_splits

    def weighted_gini(self, parent_size, splits):
        wgini = 0.0
        for i in range(0, len(splits)):
            wgini = wgini + (splits[i].get_expected_size() / parent_size) * splits[i].gini()
        return wgini

    def find_best_splits(self, data):
        data_per_class = data.split_classes()
        best_weighted_gini = 1000000
        parent_size = len(data)
        splits = self.split_data(data, data_per_class)
        weighted_gini = self.weighted_gini(parent_size, splits)
        if weighted_gini < best_weighted_gini:
            best_weighted_gini = weighted_gini
            self.best_splits = splits
            self.exemplars = self.temp_exemplars

        self.num_children = best_weighted_gini
        return self.best_splits
