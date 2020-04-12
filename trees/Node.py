from numpy.distutils.fcompiler import none
from trees import Splitter as sp
from trees import ProximityTree as ptree


class Node:

    def __init__(self, parent, label, node_id, tree: ptree.ProximityTree):
        self.is_leaf = False
        self.node_depth = 0
        self.parent = parent
        self.label = label
        self.node_id = node_id
        self.tree = tree
        self.children = list()
        self.splitter = None
        if parent != none:
            self.node_depth = parent.node_depth + 1

    def is_leaf(self):
        return self.is_leaf

    def get_label(self):
        return self.label

    def get_children(self):
        return self.children

    def train(self, dataset):
        if dataset is none:
            print("[ERROR] Dataset is none or empty")
            return

        if dataset.gini() == 0:
            self.label = dataset.class_size_map[0]
            self.is_leaf = True
            return

        self.splitter = sp.Splitter(self)
        best_split = self.splitter.find_best_splits(dataset)
        for i in range(0, best_split.get_lenght()):
            self.children[i] = Node(self, i, self.tree.node_counter + 1, self.tree)

        for i in range(0, best_split.get_lenght()):
            self.children[i].train(best_split[i])
