from random import random
from trees import Node
from core.TreeStatCollector import TreeStatCollector


class ProximityTree:

    def __init__(self, id, forest):
        self.root = None
        self.id = id
        if forest is not None:
            self.proximity_forest_id = forest.get_forest_ID()
            self.stats = TreeStatCollector(id, self.proximity_forest_id)
        self.random = random()
        self.node_counter = 0

    def get_root_node(self):
        return self.root

    def train(self, data):
        self.root = Node.Node(parent=None, label=None, node_id=self.node_counter + 1, tree=self)
        self.root.train(data)

    # query []
    def predict(self, query):
        node = self.root
        if node is None:
            return -1
        while not node.is_leaf:
            node = node.children[node.splitter.find_closest_branch_(query)]
        return node.label

    def get_treestat_collection(self):
        self.stats.collate_results(self)
        return self.stats

    def get_num_nodes(self):
        nodes = self._get_num_nodes(self.root) - 1
        if self.node_counter != nodes:
            print("Error: error in node counter!")
            return -1
        else:
            return self.node_counter

    def _get_num_nodes(self, node):
        count = 0
        if node.children is None:
            return 1
        for i in range(0, len(node.children)):
            count = count + self._get_num_nodes(node.children[i])
        return count + 1

    def get_num_leaves(self):
        return self._get_num_leaves(self.root)

    def _get_num_leaves(self, n):
        count = 0
        if n.children is None:
            return 1
        for i in range(0, len(n.children)):
            count = count + self._get_num_leaves(n.children[i])
        return count

    def get_num_internal_node(self):
        return self._get_num_internal_node(self.root)

    def _get_num_internal_node(self, n):
        count = 0
        if n.children is None:
            return 0
        for i in range(0, len(n.children)):
            count = count + self._get_num_internal_node(n.childen[i])

        return count + 1

    def get_height(self):
        return self._get_height(self.root)

    def _get_height(self, n):
        max_depth = 0
        if n.children is None:
            return 0
        for i in range(0, len(n.children)):
            max_depth = max(max_depth, self._get_height(n.children[i]))
        return max_depth + 1

    def get_min_depth(self, node):
        max_depth = 0
        if node.children is not None:
            return 0

        for i in range(0, len(node.children)):
            max_depth = min(max_depth, self._get_height(node.children[i]))
        return max_depth + 1

    pass
