from dataStructures import ListDataset


class AppContext:
    elastic_distance = "dtw"
    window_length = 1.5
    series_length = 0
    num_test_series = 0
    num_train_series = 0
    print_test_progress_for_each_instances = 100
    config_majority_vote_tie_break_randomly = True
    config_skip_distance_when_exemplar_matches_query = True
    config_use_random_choice_when_min_distance_is_equal = True
    training_file = "/Users/morad/PycharmProjects/PForests/datasets/Chinatown/Chinatown_TRAIN.csv"
    testing_file = "/Users/morad/PycharmProjects/PForests/datasets/Chinatown/Chinatown_TEST.csv"
    output_dir = "../output/"
    csv_has_header = True
    ignore_first_col = True
    target_column_is_first = False
    dataset_name = ""
    verbosity = 2
    num_repeats = 10
    num_trees = 100
    num_candidates_per_split = 5
    random_dm_per_node = True
    shuffle_dataset = False
    export_level = 0
    separator = ","
    training_dataset = ListDataset.ListDataset()
    testing_dataset = ListDataset.ListDataset()
    sequence_stats = None

    def __init__(self, train_dataset: ListDataset, test_dataset: ListDataset):
        self.training_file = train_dataset
        self.testing_file = test_dataset

    def print_parameters(self):
        print("dataStructures name", self.dataset_name)
        print("train dataStructures", self.training_file)
        print("test dataStructures", self.testing_file)
        print("number of trees", self.num_trees)
        print("number of repeats", self.num_repeats)
        print("number of candidates", self.num_candidates_per_split)

    def get_training_dataset(self):
        return self.training_file

    # -train
    def set_training_dataset(self, data_set):
        self.training_dataset = data_set

    def get_testing_dataset(self):
        return self.testing_file

    # test
    def set_testing_dataset(self, data_set):
        self.testing_dataset = data_set

    # -out
    def set_output_dir(self, output_dir):
        self.output_dir = output_dir

    def get_output_dir(self):
        return self.output_dir

    def get_dataset_name(self):
        return self.dataset_name

    # dataStructures name
    def set_dataset_name(self, dataset_name):
        self.dataset_name = dataset_name

    # num repeats
    def set_num_repeats(self, num_repeats):
        self.num_repeats = num_repeats

    def get_num_repeats(self):
        return self.num_repeats

    # num candidates per split
    def set_num_candidates_per_split(self, candidates_per_split):
        self.num_candidates_per_split = candidates_per_split

    def get_num_candidates_per_split(self):
        return self.num_candidates_per_split

    # num_trees
    def set_num_trees(self, num_trees):
        self.num_trees = num_trees

    def get_num_trees(self):
        return self.num_trees

    # random dm per node
    def set_random_dm_per_node(self, is_rand):
        self.random_dm_per_node = is_rand

    def get_random_dm_per_node(self):
        return self.random_dm_per_node

    # export level
    def set_export_level(self, export_level):
        self.export_level = export_level

    def get_export_level(self):
        return self.export_level

    # shuffle dataStructures
    def set_shuffle_dataset(self, shuffle_dataset):
        self.shuffle_dataset = shuffle_dataset

    def get_shuffle_dataset(self):
        return self.shuffle_dataset

    # verbosity
    def set_verbosity(self, verbosity):
        self.verbosity = verbosity

    def get_verbosity(self):
        return self.verbosity

    def set_value(self, arg, value):
        if arg is None:
            return
        if value is None:
            return
        if arg == "-train":
            self.set_training_dataset(value)
        elif arg == "-test":
            self.set_testing_dataset(value)
        elif arg == "-out":
            self.set_output_dir(value)
        elif arg == "-repeats":
            self.set_num_repeats(int(value))
        elif arg == "-trees":
            self.set_num_trees(int(value))
        elif arg == "-r":
            self.set_num_candidates_per_split(int(value))
        elif arg == "-trees":
            self.set_random_dm_per_node(value)
        elif arg == "-export":
            self.set_export_level(int(value))
        elif arg == "-verbosity":
            self.set_verbosity(int(value))
        elif arg == "-shuffle":
            self.set_shuffle_dataset(value)

    def print_content(self):
        print("Name:", self.get_dataset_name())
        print("Output dir:", self.get_output_dir())
        print("Num trees:", self.get_num_trees())
        print("Num repeats:", self.get_num_repeats())
        print("Training set:", self.get_training_dataset())
        print("Testing set:", self.get_testing_dataset())
        print("Candidates per split:", self.get_num_candidates_per_split())
