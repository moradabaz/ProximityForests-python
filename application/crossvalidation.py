import sys
import json
import time
import random
from scipy.io import arff

sys.path.append(sys.argv[1])
from core.ExperimentRunner import ExperimentRunner
from core.FileReader import FileReader

trainin_path = sys.argv[3]
name = sys.argv[2]


def save_json(accuracies):
    f_path = '../outputs/' + name + '_Folds_' + str(time.localtime().tm_hour) + str(time.localtime().tm_min) + str(
        time.localtime().tm_sec) + ".json"
    data = {'folds_accuracies': []}
    for fold in accuracies:
        data['folds_accuracies'].append({
            'Fold_' + str(fold): str(accuracies[fold])
        })
    with open(f_path, 'w+') as file:
        file.write(json.dumps(data))
    file.close()
    return


pass

random.seed(1234)
arff_data, training_classes = arff.loadarff(trainin_path)
num_series = len(arff_data)
num_series_per_fold = round(num_series / 10)
counter = 0
folds = dict()
key = 0
series = list()
for i in range(0, num_series):
    if i % num_series_per_fold is 0:
        if key < 10:
            key = key + 1
            folds[key] = list()
            folds[key].append(arff_data[i])
        else:
            folds[key].append(arff_data[i])
    else:
        folds[key].append(arff_data[i])
train_data = list()
fold_accuracies = dict()
runner = ExperimentRunner()
for turn in folds.keys():
    test_dataset = FileReader.parse_arff_data(folds[turn])
    for fold in folds.keys():
        if fold != turn:
            for line in folds[fold]:
                train_data.append(line)
    print("FOLD ", turn, " ->")
    train_dataset = FileReader.parse_arff_data(train_data)
    pforest = runner.run_data(train_dataset, test_dataset, name)
    fold_accuracies[turn] = pforest.result.accuracy
save_json(fold_accuracies)
