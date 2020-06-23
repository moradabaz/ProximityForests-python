import dtaidistance.dtw as dtw
import random
import numpy as np
from core import AppContext
from distance import *
from distance.ERP import ERP
from distance.LCSS import LCSS
from distance.MSM import MSM
from distance.TWE import TWE


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

            #dist = dtw.distance_fast(array_query, exemplars, window=2)
            #  windowsize = ERP.ERP.get_random_window(AppContext.AppContext.series_length)
            #  g_value = ERP.ERP.get_random_g(AppContext.AppContext.training_dataset)
            # dist = ERP.ERP.erp_distance(array_query, exemplars, windowsize, g_value)
            #msm_cost = MSM.get_random_cost()
            #dist = MSM.distance(array_query, exemplars, msm_cost)
            if AppContext.AppContext.elastic_distance == "dtw":
                dist = dtw.distance(array_query, exemplars, window=2)
            elif AppContext.AppContext.elastic_distance == "lcss":
                dist = LCSS.distance(array_query, exemplars, window_size=)
            dist = TWE.distance(array_query, exemplars, TWE.get_random_nu(), TWE.get_random_lambda())
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
            r = 0
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
