import unittest
from core import ExperimentRunner


class MyTestCase(unittest.TestCase):

    experiment = ExperimentRunner.ExperimentRunner()

    def time_splitter_find_closest_branch(self):
        self.experiment.run()

    # def time_splitter_split_data(self):
    #    self.experiment.run()


if __name__ == '__main__':
    unittest.main()
