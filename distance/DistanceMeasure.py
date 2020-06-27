import dtaidistance.dtw as dtw
import random
import numpy as np
from core import AppContext
from distance.lcss import LCSS
from distance.TWE import TWE
import math


class DistanceMeasure:
    """
    This fonction finds the serie which is the most similar to the query serie
        :param temp_exemplar -> list of serie
        :param query -> Set of series
    """

    @staticmethod
    def find_closest_nodes(query, temp_exemplars: list):
        array_query = np.asarray(query)
        closest_nodes = list()
        bsf = np.inf
        for i in range(0, len(temp_exemplars)):
            exemplars = np.asarray(temp_exemplars.__getitem__(i))
            try:
                if np.array_equal(exemplars, array_query):
                    return i
            except RecursionError:
                return -1

            if AppContext.AppContext.elastic_distance == "dtw":
                dist = dtw.distance_fast(array_query, exemplars, window=AppContext.AppContext.window_length,
                                         max_dist=bsf)
            elif AppContext.AppContext.elastic_distance == "lcss":
                esilon = LCSS.get_random_epsilon()
                dist = LCSS.distance(array_query, exemplars, window_size=-np.inf, epsilon=esilon)
            elif AppContext.AppContext.elastic_distance == "twe":
                dist = TWE.distance(array_query, exemplars, TWE.get_random_nu(), TWE.get_random_lambda())
            else:
                dist = dtw.distance_fast(array_query, exemplars, window=2)

            if dist < bsf:
                bsf = dist
                closest_nodes.clear()
                closest_nodes.append(i)
            elif bsf == dist:
                closest_nodes.append(i)

        if len(closest_nodes) == 0:
            print("There are no closest Nodes")
            r = 0
        elif len(closest_nodes) == 1:
            return closest_nodes[0]
        else:
            r = random.randint(0, len(closest_nodes) - 1)
        return closest_nodes[r]

    @staticmethod
    def find_closes_branch_ar(array_query, temp_exemplars):
        closest_nodes = list()
        bsf = 100000
        for i in range(0, len(temp_exemplars)):
            exemplars = np.asarray(temp_exemplars.__getitem__(i))
            if DistanceMeasure.are_equal(exemplars, array_query):
                return i
            dist = dtw.distance_fast(array_query, exemplars)
            if dist < bsf:
                bsf = dist
                closest_nodes.clear()
                closest_nodes.append(i)
            elif bsf == dist:
                closest_nodes.append(i)
        r = random.randint(0, len(closest_nodes) - 1)
        return closest_nodes[r]

    @staticmethod
    def are_equal(first, second):
        if len(first) != len(second):
            return False
        for i in range(0, len(first)):
            if first[i] != second[i]:
                return False
        return True

    @staticmethod
    def stdv_p():
        sumx = 0
        sumx2 = 0
        for i in range(0, AppContext.AppContext.training_dataset.series_data.__len__()):
            insarray = np.asarray(AppContext.AppContext.training_dataset[i])
            for j in range(0, len(insarray)):
                sumx = sumx + insarray[j]
                sumx2 = sumx2 + insarray[j] * insarray[j]
        n = len(AppContext.AppContext.training_dataset.series_data)
        mean = sumx / n
        return math.sqrt((sumx2 / n) - mean * mean)
