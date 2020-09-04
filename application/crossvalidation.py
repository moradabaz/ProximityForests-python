import sys
import json
import time
import random
from scipy.io import arff
sys.path.append(sys.argv[1])
from core import AppContext
from core.ExperimentRunner import ExperimentRunner
from core.FileReader import FileReader

trainin_path = sys.argv[3]
name = sys.argv[2]


def save_json(folds):
    f_path = '../outputs/' + name + '_Folds.json'
    header = 'iterations,trees,candidates,accuracy'
    with open(f_path, 'w+') as file:
        file.writelines("%s\n" % header)
        file.writelines("%s\n" % linea for linea in folds)
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
lineas = list()
runner = ExperimentRunner()
AppContext.AppContext.num_repeats = 10
AppContext.AppContext.num_trees = 100
AppContext.AppContext.num_candidates_per_split = 5
for trees in [20, 35]:
    AppContext.AppContext.num_trees = trees
    for candidates in [2, 3, 4]:
        AppContext.AppContext.num_candidates_per_split = candidates
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
            linea = str(turn) + ',' + str(AppContext.AppContext.num_trees) + ',' + str(AppContext.AppContext.num_candidates_per_split) + ',' + str(fold_accuracies[turn])
            lineas.append(linea)
save_json(lineas)
