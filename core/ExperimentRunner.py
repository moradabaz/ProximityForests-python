import sys
from dataset import ListDataset
from core import CSVReader, AppContext, PFResult
from trees import ProximityForest, ProximityTree, Splitter


class ExperimentRunner:

    def __init__(self):
        self.train_data = ListDataset.ListDataset()
        self.test_data = ListDataset.ListDataset()
        self.def_separator = ","

    def run(self):
        train_data_original = CSVReader.CSVReader.readCSVToListDataset(AppContext.AppContext.training_file,
                                                                       AppContext.AppContext.csv_has_header,
                                                                       AppContext.AppContext.target_column_is_first,
                                                                       separator=self.def_separator)
        test_data_original = CSVReader.CSVReader.readCSVToListDataset(AppContext.AppContext.testing_file,
                                                                      AppContext.AppContext.csv_has_header,
                                                                      AppContext.AppContext.target_column_is_first,
                                                                      separator=self.def_separator)

        self.train_data = train_data_original.reorder_class_labels(None)
        self.test_data = test_data_original.reorder_class_labels(self.train_data.initial_class_labels)

        print("Series: Length:", len(self.train_data.series_data[0]))

        # AppContext.AppContext.set_training_dataset(self.train_data)
        # AppContext.AppContext.set_testing_dataset(self.test_data)

        train_data_original = None
        test_data_original = None

        #  try:
        training_file = open(AppContext.AppContext.training_file)
        dataset_name = training_file.name
        # AppContext.AppContext.set_dataset_name(dataset_name)

        # PrintUtilities.printConfiguration()

        if AppContext.AppContext.shuffle_dataset:
            print("Shuffling in the training set...")
            self.train_data.shuffle()

        num_repeats = AppContext.AppContext.num_repeats
        for i in range(0, num_repeats):
            if AppContext.AppContext.verbosity > 0:
                print("Number of repeats:", AppContext.AppContext.num_repeats)
                print("Number of trees:")
                print("Experimenting...")
            else:
                print("This is ...")

            print("Creating Proximity Forest in repeat", i + 1)
            pforest = ProximityForest.ProximityForest(i)
            AppContext.AppContext.num_train_series = self.train_data.get_series_size()

            pforest.train(self.train_data)

            print("------------TIME----TO----TEST------")

            AppContext.AppContext.num_test_series = self.test_data.get_series_size()
            result = pforest.test(self.test_data)

            pforest.print_results(dataset_name, i, "")

            # result.print_results(dataset_name, i, "")

            if AppContext.AppContext.export_level > 0:
                result.exportJSON(dataset_name, i)

            return pforest.result
            # Proximity Forest implementation

    # except:
    #     return

    def load_traindata(self):
        train_data_original = CSVReader.CSVReader.readCSVToListDataset(AppContext.AppContext.training_file,
                                                                       AppContext.AppContext.csv_has_header,
                                                                       AppContext.AppContext.target_column_is_first,
                                                                       separator=self.def_separator)
        test_data_original = CSVReader.CSVReader.readCSVToListDataset(AppContext.AppContext.testing_file,
                                                                      AppContext.AppContext.csv_has_header,
                                                                      AppContext.AppContext.target_column_is_first,
                                                                      separator=self.def_separator)

        self.train_data = train_data_original.reorder_class_labels(None)
        self.test_data = test_data_original.reorder_class_labels(self.train_data.initial_class_labels)

        if AppContext.AppContext.shuffle_dataset:
            print("Shuffling in the training set...")
            self.train_data.shuffle()
        num_repeats = AppContext.AppContext.num_repeats
        for i in range(0, int(num_repeats)):
            if AppContext.AppContext.verbosity > 0:
                print("Experimenting...")
            else:
                print("This is ...")
            pforest = ProximityForest.ProximityForest(i)
            pforest.train(self.train_data)
            return pforest
