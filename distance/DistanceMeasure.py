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
            exemplars = np.asarray(temp_exemplars[i])

            if (exemplars == array_query).all():
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
