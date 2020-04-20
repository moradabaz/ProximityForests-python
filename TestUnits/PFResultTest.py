import unittest
from core import PFResult
from trees import ProximityForest
from dataset import ListDataset
from util import randomNumbers as rdnumbers
from core import AppContext as appcontext


class MyTestCase(unittest.TestCase):
    pforest = ProximityForest.ProximityForest(64)
    pfresult = PFResult.PFResult(pforest)

    def test_collate_results_1(self):
        dataset = rdnumbers.randomNumbers.generate_dataset_multiple_series(8, 6, 4)
        self.pforest.train(dataset)
        self.pfresult.collate_results()

    def test_collate_results_2(self):
        dataset = rdnumbers.randomNumbers.generate_dataset(10, 6)
        #test_datset = rdnumbers.randomNumbers.generate_dataset(10, 6)
        test_datset = rdnumbers.randomNumbers.generate_dataset_with_labels(dataset.labels, 10, 6)
        self.pforest.train(dataset)
        result = self.pforest.test(test_datset)
        result.print_results(dataset, 64, "str")


if __name__ == '__main__':
    unittest.main()
