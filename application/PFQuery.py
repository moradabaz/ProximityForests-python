import sys
from math import inf

from core import AppContext, ExperimentRunner
from distance.DistanceMeasure import DistanceMeasure
import timeit
from dtaidistance import dtw
import numpy as np
class PFQuery:

    def __init__(self):
        self.appcontext = AppContext.AppContext(train_dataset="/Users/morad/PycharmProjects/PForests/util/tabla1.csv",
                                                test_dataset="/Users/morad/PycharmProjects/PForests/util/tabla1.csv")
        return

    def get_app_context(self):
        return self.appcontext

    def parse_args(self):
        argc = "-out=output -repeats=1 -trees=1 -r=1 -on_tree=true -export=1 -verbosity=2"
        argv = argc.split(" ")
        if len(argv) > 1:
            for i in range(1, len(argv)):
                options = argv[i].split("=")
                arg = options[0]
                value = options[1]
                self.appcontext.set_value(arg, value)


pq = PFQuery()
experimentrunner = ExperimentRunner.ExperimentRunner()
pforest = experimentrunner.load_traindata()
for query in experimentrunner.test_data.series_data:
    query_serie = np.asarray(query)

    label = pforest.predict(query)

    lista = experimentrunner.train_data.get_series_from_label(label)
    num_series = len(lista)
    best_dist = inf
    best_serie_id = -1
    for i in range(0, num_series):
        serie = lista[i]
        dist = dtw.distance_fast(np.asarray(query), np.asarray(serie))
        if dist < best_dist:
            best_dist = dist
            best_serie_id = i

    print("QUERY")
    print(query)
    print("Series aproximate:", best_serie_id)
    print(lista[best_serie_id])
    print("Dist: ", best_dist)

    print("DISTANCIAS")
    resultado = pforest.calculate_diffs(np.asarray(lista[best_serie_id]), np.asarray(query))
    print(resultado)
    print(np.max(resultado))

