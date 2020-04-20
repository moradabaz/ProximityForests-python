import unittest
from trees import Node, ProximityTree, ProximityForest
from util import randomNumbers as rdnumbers
class MyTestCase(unittest.TestCase):

    pforest = ProximityForest.ProximityForest(61)
    ptree1 = ProximityTree.ProximityTree(42, pforest)
    ptree2 = ProximityTree.ProximityTree(47, forest=None)
    node = Node.Node(parent=None, label="NodeOne", node_id=26, tree=ptree1)

    def test_train_1(self):
        dt = rdnumbers.randomNumbers.generate_dataset(5, 6)
        self.ptree1.train(dt)

    def test_predict_1(self):
        dt1 = rdnumbers.randomNumbers.generate_dataset(5, 6)
        dt2 = rdnumbers.randomNumbers.generate_dataset(5, 6)
        self.ptree1.train(dt1)
        serie = rdnumbers.randomNumbers.generate_random_array(6)
        self.ptree1.predict(serie)

    def test_get_min_depth(self):
        dt1 = rdnumbers.randomNumbers.generate_dataset(5, 6)
        dt2 = rdnumbers.randomNumbers.generate_dataset(5, 6)
        self.ptree1.train(dt1)
        serie = rdnumbers.randomNumbers.generate_random_array(6)
        self.ptree1.predict(serie)
        print(self.ptree1.get_min_depth(self.node))


    def test_something(self):
        self.assertEqual(True, False)




if __name__ == '__main__':
    unittest.main()
