import unittest
from core import AppContext


class MyTestCase(unittest.TestCase):
    app_context = AppContext.AppContext("/train", "/test")

    parameters1 = '-train=/data/ucr/ItalyPowerDemand_TRAIN.csv -test=/data/ucr/ItalyPowerDemand_TEST.csv -out=output ' \
                  '-repeats=1 -trees=100 -r=1 -on_tree=true -export=1 -verbosity=0 '

    parameters2 = '-test=/data/ucr/ItalyPowerDemand_TEST.csv -out=output ' \
                  '-repeats=1 -trees=100 -r=1 -on_tree=true -export=1 -verbosity=0 '

    parameters3 = '-train=/data/ucr/ItalyPowerDemand_TRAIN.csv -out=output ' \
                  '-repeats=1 -trees=100 -r=1 -on_tree=true -export=1 -verbosity=0 -shuffle=True'

    #    def test_something(self):
    #        self.assertEqual(True, False)

    def test_training_dataset(self):
        self.app_context.set_training_dataset("/ruta/training.csv")
        self.assertEqual(self.app_context.get_training_dataset(), "/ruta/training.csv")

    def test_testing_dataset(self):
        self.app_context.set_testing_dataset("/ruta/testing.csv")
        self.assertEqual(self.app_context.get_testing_dataset(), "/ruta/testing.csv")

    def test_output_dir(self):
        self.app_context.set_output_dir("/output/")
        self.assertEqual(self.app_context.get_output_dir(), "/output/")

    def test_num_repeats(self):
        self.app_context.set_num_repeats(10)
        self.assertEqual(self.app_context.get_num_repeats(), 10)

    def test_random_dm_per_node(self):
        self.app_context.set_random_dm_per_node(100)
        self.assertEqual(self.app_context.get_random_dm_per_node(), 100)

    def test_export_level(self):
        self.app_context.set_export_level(2)
        self.assertEqual(self.app_context.get_export_level(), 2)

    def test_set_value_1(self):
        argv = self.parameters1.strip().split(" ")
        if len(argv) > 1:
            for i in range(0, len(argv)-1):
                options = argv[i].split("=")
                arg = options[0]
                value = options[1]
                self.app_context.set_value(arg, value)
            self.app_context.set_dataset_name("holamundo")
            self.assertEqual(self.app_context.get_dataset_name(), "holamundo")
            self.assertEqual(self.app_context.get_output_dir(), "output")
            self.assertEqual(self.app_context.get_training_dataset(), "/data/ucr/ItalyPowerDemand_TRAIN.csv")
            self.assertEqual(self.app_context.get_testing_dataset(), "/data/ucr/ItalyPowerDemand_TEST.csv")
            self.assertEqual(self.app_context.get_num_trees(), 100)
            self.assertEqual(self.app_context.get_num_repeats(), 1)
            self.assertEqual(self.app_context.get_num_candidates_per_split(), 1)

    def test_set_value_2(self):
        argv = self.parameters2.strip().split(" ")
        if len(argv) > 1:
            for i in range(1, len(argv)):
                options = argv[i].split("=")
                arg = options[0]
                value = options[1]
                self.app_context.set_value(arg, value)
            self.assertEqual(self.app_context.get_export_level(), 1)
            self.assertEqual(self.app_context.get_shuffle_dataset(), True)
            self.assertEqual(self.app_context.get_verbosity(), 0)

if __name__ == '__main__':
    unittest.main()
