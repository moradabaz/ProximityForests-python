from trees import Splitter as sp
from trees import ProximityTree as ptree
from dataset import ListDataset as ltd
import time
class Node:

    def __init__(self, parent, label, node_id, tree):
        self.is_leaf = False
        self.node_depth = 0
        self.parent = parent
        self.label = label
        self.node_id = node_id
        self.tree = tree
        self.children = list()
        self.splitter = None
        if parent is not None:
            self.node_depth = parent.node_depth + 1

    def is_leaf(self):
        return self.is_leaf

    def get_label(self):
        return self.label

    def get_children(self):
        return self.children

    def train(self, dataset: ltd.ListDataset):
        start = time.clock()
        if dataset is None:
            print("[ERROR] Dataset is none or empty")
            return
        gini = dataset.gini()
        if gini == 0:
            self.label = dataset.labels[0]
            self.is_leaf = True
            return
        self.splitter = sp.Splitter(self)
        best_split = self.splitter.find_best_splits(dataset)
        for i in range(0, len(best_split.values())):
            self.children.append(Node(self, i, self.tree.node_counter + 1, self.tree))
            self.tree.node_counter = self.tree.node_counter + 1
        counter = 0
        for split in best_split.values():
            self.children[counter].train(split)
            counter = counter + 1
        stop = time.clock()
        print("[TIEMPO][NODE - TRAIN]: ", (stop - start))
