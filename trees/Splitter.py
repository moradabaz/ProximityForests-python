import dtw
from dataset import ListDataset
from core import AppContext
import random


class Splitter:

    def __init__(self, node):
        self.node = node

    def split_data(self, sample, data_per_class):
        splits = ListDataset.ListDataset(sample.get_num_classes())
        temp_exemplars = sample.get_num_classes()
        branch = 0
        for entry in data_per_class.keys():
            r = random.randint(data_per_class[entry])
            splits[branch] = ListDataset.ListDataset(sample.expected_size, 0)
            temp_exemplars[branch] = data_per_class[entry].get_series(r)
            branch = branch + 1
        sample_size = sample.expected_size
        closest_branch = -1
        for j in range(0, sample_size):
            closest_branch = self.find_closest_branch(sample.get_series(r), self.temp_distance_measure, temp_exemplars)
            if closest_branch == -1:
                assert False
            splits[closest_branch].add_series(sample.get_class(j), sample.get_series(j))
        return splits

    def find_closest_branch(self, query, dm, e):
        return