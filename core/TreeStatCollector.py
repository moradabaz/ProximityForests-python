class TreeStatCollector:

    def __init__(self, forest_id, tree_id):
        self.forest_id = forest_id
        self.tree_id = tree_id
        self.tree = None
        self.num_nodes = -1
        self.num_leaves = -1
        self.depth = -1
        self.weighted_depth = -1

    def collate_results(self, ptree):
        self.tree = ptree
        self.num_nodes = ptree.get_num_nodes()
        self.num_leaves = ptree.get_num_leaves()
        self.depth = ptree.get_height()
        self.weighted_depth = -1


    pass