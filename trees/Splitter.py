from distance import DistanceMeasure as dm
from dataset import ListDataset
from core import AppContext
import numpy as np
import random
import time


class Splitter:

    def __init__(self, node):
        self.num_children = None
        self.temp_exemplars = dict()
        self.node = node
        self.best_splits = dict()
        self.exemplars = None

    """
    
    This function splits the data collected and structured from the dataset 
    For each class, we get their respective dataset and get a random exemplar serie from it.
    Then, for each set of series of the sample dataset:
    - we find the closest branch (class) which series are similiar to the exemplar serie
      previously extracted randomly.
    - We insert the closest branch, which is a class, into a list
    After the search, we pick a random class from the list.
    :param sample_dataset List of classified series
    :param dataset_per_class A map of <class, series>. Each class represent a branch
    :return A random class from a list of classes which series are similar to the exemplar serie
    """
    def split_data(self, sample_dataset: ListDataset, dataset_per_class: dict):
        splits = dict()
        class_branch = 0
        for class_key in dataset_per_class.keys():
            dataset = dataset_per_class[class_key]
            length = dataset.get_series_size() - 1
            if length < 0:
                continue
            else:
                r = random.randint(0, length)
                splits[class_branch] = ListDataset.ListDataset()
                self.temp_exemplars[class_branch] = np.asarray(dataset.get_series(r))
                class_branch = class_branch + 1
        sample_size = sample_dataset.get_series_data_length()

        for j in range(0, sample_size):
            exemplar_series = self.get_list_from_dict(self.temp_exemplars)
            closest_branch = Splitter.find_closest_branch(sample_dataset.get_series(j), exemplar_series)
            if closest_branch == -1:
                return splits
            splits[closest_branch].add_series(sample_dataset.get_class(j), sample_dataset.get_series(j))
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
        for spt in splits.values():
            wgini = wgini + (spt.get_series_data_length() / parent_size) * spt.gini()
        return wgini

    """
    This function finds the best splits of a dataset
    splitting the data n_candidate times and returning
    the less weighted gini split
    """
    def find_best_splits(self, sample_dataset):
        series_per_class = sample_dataset.split_classes()
        best_weighted_gini = 1000000
        num_series = sample_dataset.get_series_data_length()
        for i in range(0, AppContext.AppContext.num_candidates_per_split):
            splits = self.split_data(sample_dataset, series_per_class)
            weighted_gini = self.weighted_gini(num_series, splits)
            if weighted_gini < best_weighted_gini:
                best_weighted_gini = weighted_gini
                self.best_splits = splits
                self.exemplars = self.temp_exemplars
        self.num_children = self.best_splits.__len__()
        return self.best_splits

    @staticmethod
    def get_list_from_dict(query: dict):
        lista = list()
        for entry in query.values():
            lista.append(entry)
        return lista
