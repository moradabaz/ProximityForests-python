class TreeStatCollector:

    def __init__(self, forest_id, tree_id):
        self.forest_id = forest_id
        self.tree_id = tree_id

    def collate_results(self, ptree):
        self.tree = ptree
        self.num_nodes = ptree.get_num_nodes()
        self.num_leaves = ptree.get_num_leaves()
        self.depth = ptree.get_height()



    pass