import dtw
import random
from core import AppContext


class DistanceMeasure:

    closest_nodes = list()

    def find_closest_nodes(self, query, exemplars, train):
        global exemplar
        dist = float('inf')
        bsf = float('-inf')

        for i in range(0, len(exemplars)):
            exemplar = exemplars[i]
            if exemplar == query:
                return i

            dist = dtw.accelerated_dtw(x=query, y=exemplar)
            if dist < bsf:
                bsf = dist
                self.closest_nodes.clear()
                self.closest_nodes.append(i)
            else:
                bsf = dist
                self.closest_nodes.append(i)
        r = random.randint(len(self.closest_nodes))
        return self.closest_nodes[r]
