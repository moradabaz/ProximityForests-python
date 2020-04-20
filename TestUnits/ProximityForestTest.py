import unittest
from util import randomNumbers as rdnumbers
from trees import ProximityForest


class MyTestCase(unittest.TestCase):
    pforest = ProximityForest.ProximityForest(64)

    def test_something(self):
        self.assertEqual(len(self.pforest.trees), 50)

    def test_train(self):
        dt = rdnumbers.randomNumbers.generate_dataset(5, 6)
        self.pforest.train(dt)

    def test_testing(self):
        dt = rdnumbers.randomNumbers.generate_dataset(5, 6)
        self.pforest.test(dt)


if __name__ == '__main__':
    unittest.main()
