from trees import Splitter as sp
from dataStructures import ListDataset as ltd
import timeit


class Node:

    def __init__(self, parent, label, node_id, depth, tree, train_cache=None):
        self.depth = depth
        self.is_leaf = False
        self.node_depth = 0
        self.parent = parent
        self.label = label
        self.node_id = node_id
        self.tree = tree
        self.children = list()
        self.splitter = None
        self.train_cache = train_cache
        if parent is not None:
            self.node_depth = parent.node_depth + 1

    def is_leaf(self):
        return self.is_leaf

    def get_label(self):
        return self.label

    def get_children(self):
        return self.children

    """
        1 - We initialize our splitter in the node.
        2 - We search our best splits
        3 - For each dataStructures of the splits:
            3.1 - We create a Node-Child 
            3.2 - We train the node-Child
        :param  dataStructures
    """

    def train(self, dataset: ltd.ListDataset):
        if dataset is None:
            print("[ERROR] Dataset is none or empty")
            exit(0)
        gini = dataset.gini()
        if gini == 0:
            self.label = dataset.classes[0]
            self.is_leaf = True
            return
        self.splitter = sp.Splitter(self)
        start = timeit.default_timer()
        best_split = self.splitter.find_best_splits(dataset)
        stop = timeit.default_timer()
        self.tree.time_best_splits = self.tree.time_best_splits + (stop - start)
        for i in range(0, len(best_split.values())):
            self.children.append(Node(self, i, self.tree.node_counter + 1, self.depth + 1, self.tree))
            self.tree.node_counter = self.tree.node_counter + 1
        counter = 0
        for split in best_split.values():
            try:
                self.children[counter].train(split)
            except OverflowError:
                return
            counter = counter + 1
