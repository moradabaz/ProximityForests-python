import unittest
from trees import Node, ProximityTree
from util import randomNumbers as rd


class MyTestCase(unittest.TestCase):
    ptree = ProximityTree.ProximityTree(12, forest=None)
    node = Node.Node(parent=None, label="Best Node", node_id=23, tree=ptree)

    def test_training_1(self):
        dataset = rd.randomNumbers.generate_dataset(5, 4)
        self.node.train(dataset)


    def test_training_2(self):
        dataset = rd.randomNumbers.generate_dataset(555, 4)
        self.node.train(dataset)

    def test_training_3(self):
        dataset = rd.randomNumbers.generate_dataset(5555, 8)
        self.node.train(dataset)

if __name__ == '__main__':
    unittest.main()
