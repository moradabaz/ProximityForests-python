from numpy.distutils.fcompiler import none

import util.Constants
from dtw import *


class AppContext:
    config_majority_vote_tie_break_randomly = True
    config_skip_distance_when_exemplar_matches_query = True
    config_use_random_choice_when_min_distance_is_equal = True

    training_file = "/Users/morad/git/ProximityForest/paper/ItalyPowerDemand_TRAIN.csv"
    testing_file = "/Users/morad/git/ProximityForest/paper/ItalyPowerDemand_TRAIN.csv"
    output_dir = "output/"
    csv_has_header = False
    target_column_is_first = True

    num_repeats = 10
    num_trees = 50
    num_candidates_per_split = 100
    random_dm_per_node = True
    shuffle_dataset = True

    def __init__(self, train_dataset, test_dataset):
        self.training_file = train_dataset
        self.testing_file = test_dataset

    @staticmethod
    def get_training_dataset(self):
        return self.training_file

    @staticmethod
    def set_training_dataset(self, data_set):
        self.training_file = data_set

    @staticmethod
    def get_testing_dataset(self):
        return self.testing_file

    @staticmethod
    def set_testing_dataset(self, data_set):
        self.testing_file = data_set

    @staticmethod
    def get_dataset_name(self):
        return self.dataset_name

    @staticmethod
    def set_dataset_name(self, dataset_name):
        self.dataset_name = dataset_name

    @staticmethod
    def set_num_repeats(self, num_repeats):
        self.num_repeats = num_repeats

    @staticmethod
    def get_num_repeats(self):
        return self.num_repeats

    @staticmethod
    def set_num_candidates_per_split(self, candidates_per_split):
        self.num_candidates_per_split = candidates_per_split

    @staticmethod
    def set_random_dm_per_node(self, is_rand):
        self.random_dm_per_node = is_rand

    @staticmethod
    def get_random_dm_per_node(self):
        return self.random_dm_per_node

    @staticmethod
    def set_export_level(self, export_level):
        self.export_level = export_level

    @staticmethod
    def get_export_level(self):
        return self.export_level

    @staticmethod
    def set_shuffle_dataset(self, shuffle_dataset):
        self.shuffle_dataset = shuffle_dataset

    @staticmethod
    def get_shuffle_dataset(self):
        return self.shuffle_dataset

    @staticmethod
    def set_verbosity(self, verbosity):
        self.verbosity = verbosity

    @staticmethod
    def get_verbosity(self):
        return self.verbosity


def __init__():
    return None