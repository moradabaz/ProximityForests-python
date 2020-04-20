import dtw
import random
import numpy as np
from core import AppContext


class DistanceMeasure:

    @staticmethod
    def find_closest_nodes(query, temp_exemplars: list):
        array_query = np.asarray(query)
        closest_nodes = list()
        dist = 100000
        bsf = 100000

        for i in range(0, len(temp_exemplars)):
            exemplars = np.asarray(temp_exemplars.__getitem__(i))

            if DistanceMeasure.are_equal(exemplars, array_query):
                return i

            dist = dtw.accelerated_dtw(array_query, exemplars, 'euclidean')[0]
            if dist < bsf:
                bsf = dist
                closest_nodes.clear()
                closest_nodes.append(i)
            elif bsf == dist:
                closest_nodes.append(i)

        r = np.random.randint(len(closest_nodes), size=1)[0]
        return closest_nodes[r]

    @staticmethod
    def are_equal(first, second):
        if len(first) != len(second):
            return False
        for i in range(0, len(first)):
            if first[i] != second[i]:
                return False
        return True
