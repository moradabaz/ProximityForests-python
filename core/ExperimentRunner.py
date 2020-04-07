from numpy.distutils.fcompiler import none
import sys
from dataset import ListDataset
from core import CSVReader, AppContext


class ExperimentRunner:

    def __init__(self):
        self.train_data = ListDataset.ListDataset()
        self.test_data = ListDataset.ListDataset()
        self.def_separator = " "

    def run(self):
        train_data_original = CSVReader.CSVReader.readCSVToListDataset(AppContext.AppContext.training_file,
                                                                       AppContext.AppContext.csv_has_header,
                                                                       AppContext.AppContext.target_column_is_first,
                                                                       separator=self.def_separator)
        test_data_original = CSVReader.CSVReader.readCSVToListDataset(AppContext.AppContext.testing_file,
                                                                      AppContext.AppContext.csv_has_header,
                                                                      AppContext.AppContext.target_column_is_first,
                                                                      separator=self.def_separator)

        self.train_data = train_data_original.reorder_class_labels(none)
        self.test_data = test_data_original.reorder_class_labels(self.train_data._get_initial_class_labels())

        AppContext.AppContext.set_training_dataset(self.train_data)
        AppContext.AppContext.set_testing_dataset(self.test_data)

        train_data_original = none
        test_data_original = none

        try:
            training_file = open(AppContext.AppContext.training_file)

            for i in range(0, AppContext.AppContext.num_repeats):
                if (AppContext.AppContext.verbosity > 0):
                    print("Experimenting...")
                else:
                    print("This is ...")

            # Proximity Forest implementation



        except:
            return


        pass
