import timeit
import sys
import json
import time
from sktime.classification.distance_based import _proximity_forest as pf
from sktime.utils.load_data import load_from_tsfile_to_dataframe as ts_loader
from sktime.utils.load_data import load_from_arff_to_dataframe as arff_loader
from sktime.distances.elastic import dtw_distance
import random
sys.path.append(sys.argv[1])


class PFSktime:
    name = ''
    training_path = None
    testing_path = None

    def save_json(self, total_time, time_train, time_test, accuracy):
        f_path = '../outputs/sktime_' + self.name + '_results_' + str(
            time.localtime().tm_hour) + str(time.localtime().tm_min) + str(
            time.localtime().tm_sec) + ".json"
        data = {'dataset': []}
        data['dataset'].append({
            'name': self.name,
            'exec_time': total_time,
            'training_time': time_train,
            'testing_time': time_test,
            'accuracy': accuracy
        })
        with open(f_path, 'w+') as file:
            file.write(json.dumps(data))
        file.close()
        return

    def get_args(self):
        if len(sys.argv) > 1:
            for i in range(2, len(sys.argv)):
                options = sys.argv[i].split("=")
                arg = options[0]
                value = options[1]
                if arg == "-name":
                    self.name = value
                elif arg == "-train":
                    self.training_path = value
                elif arg == "-test":
                    self.testing_path = value


pass

data_train = None
data_test = None

pfsktime = PFSktime()
pfsktime.get_args()
random.seed(1234)
if pfsktime.testing_path.split(".")[1] == "arff":
    data_train = arff_loader(pfsktime.training_path)
    data_test = arff_loader(pfsktime.testing_path)
elif sys.argv[1].split(".")[1] == "ts":
    data_train = ts_loader(pfsktime.training_path)
    data_test = ts_loader(pfsktime.training_path)

pforest = pf.ProximityForest(distance_measure=dtw_distance, n_jobs=1)
start = timeit.default_timer()
train_time_start = timeit.default_timer()
print("Training... ")
pforest.fit(data_train[0], data_train[1])
train_time_stop = timeit.default_timer()

test_time_start = timeit.default_timer()
print("Testing....")
predictions = pforest.score(data_test[0], data_test[1])
test_time_stop = timeit.default_timer()

stop = timeit.default_timer()
pfsktime.save_json((stop - start), (train_time_stop - train_time_start), (test_time_stop - test_time_start),
                   predictions)
print(predictions)

# pforest.predict_proba()
