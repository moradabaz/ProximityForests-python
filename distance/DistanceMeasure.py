import dtw
import random
import numpy as np
from core import AppContext


class DistanceMeasure:

    @staticmethod
    def find_closest_nodes(query, exemplars):
        array_query = np.asarray(query)
        closest_nodes = list()
        dist = 100000
        bsf = 100000

        for i in range(0, len(exemplars)):
            exemplar = np.asarray(exemplars[i])

            if (exemplar == array_query).all():
                return i

            dist = dtw.accelerated_dtw(array_query, exemplar, 'euclidean')[0]
            if dist < bsf:
                bsf = dist
                closest_nodes.clear()
                closest_nodes.append(i)
            elif bsf == dist:
                closest_nodes.append(i)

        r = np.random.randint(len(closest_nodes), size=1)[0]
        return closest_nodes[r]
