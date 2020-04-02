from random import random
from core.TreeStatCollector import TreeStatCollector


class ProximityTree:

    def __init__(self, id, forest):
        self.id = id
        self.proximity_forest_id = forest.getId()
        self.random = random()
        self.stats = TreeStatCollector(id, self.proximity_forest_id)

    def get_root_node(self):
        return self.root

    def train(self, data):
        return

    pass
