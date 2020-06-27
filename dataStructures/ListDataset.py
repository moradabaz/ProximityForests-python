import random
import math


class ListDataset:
    """
        :param: series_data: List of series in the dataStructures
        :param: classes: List of classes in the datasets.
        :param: class_map: map which indicates the number of series per label -> <label, nº series>
        :param
    """

    def __init__(self, expected_size=0, length=0):
        self.series_data = list()
        self.classes = list()
        self.class_counter = dict()
        self.series_map = dict()
        self.initial_class_labels = dict()
        self.length = length
        self.is_ordered = False
        self.expected_size = expected_size

    def set_lenght(self, length):
        self.length = length

    def set_expected_size(self, size):
        self.expected_size = size

    def get_series_size(self):
        return len(self.series_data)

    def get_data(self):
        return self.series_data

    def get_labels(self):
        return self.classes

    def get_new_class_map(self):
        return self.initial_class_labels

    def get_lenght(self):
        return self.length

    def set_order(self, order):
        self.is_ordered = order

    def is_ordered(self):
        return self.is_ordered

    def get_series_data_length(self):
        return self.series_data.__len__()

    def add_series(self, label, series):
        self.series_data.append(series)
        self.classes.append(label)
        exists = False
        for lab in self.class_counter.keys():
            if lab == label:
                exists = True
                self.class_counter[lab] = self.class_counter[lab] + 1
                series_list = self.series_map[lab]
                series_list.append(series)
                self.series_map[lab] = series_list
        if not exists:
            series_list = list()
            series_list.append(series)
            self.series_map[label] = series_list
            self.class_counter[label] = 1

    def get_series_from_label(self, label):
        if not self.series_map.keys().__contains__(label):
            return list()
        return self.series_map[label]

    def remove_item(self, i):
        label = self.classes[i]
        if self.class_counter[label] is not None:
            count = self.class_counter[label]
            if count > 0:
                self.class_counter[label] = count - 1
            else:
                self.class_counter.pop(label)
        self.series_data.pop(i)
        self.classes.pop(i)
        self.expected_size = self.expected_size - 1

    def get_series(self, i):
        return self.series_data[i]

    def get_class(self, i):
        return self.classes[i]

    def get_num_classes(self):
        return len(self.class_counter)

    def get_class_size(self, label):
        return self.class_counter[label]

    def get_class_map(self):
        return self.class_counter

    def get_unique_classes(self):
        keys = self.class_counter.keys()
        unique_classes = [None] * len(keys)
        i = 0
        for key in keys:
            unique_classes[i] = key
            i = i + 1

        return unique_classes

    def get_unique_classes_as_set(self):
        return self.class_counter.keys()

    def split_classes(self):
        split = dict()
        for i in range(0, self.classes.__len__()):
            label = self.classes[i]
            if not split.keys().__contains__(label):
                class_set = ListDataset()
                split[label] = class_set
            split[label].add_series(label, self.series_data[i])
        return split

    def gini(self):
        total_sum = 0
        total_size = len(self.series_data)
        for item in self.class_counter.keys():
            p = (self.class_counter[item] / total_size)
            total_sum = total_sum + p * p
        return 1 - total_sum

    def _internal_data_list(self):
        return self.series_data

    def _internal_class_list(self):
        return self.classes

    def reorder_class_labels(self, new_order):
        new_dataset = ListDataset()
        if new_order is None:
            new_order = dict()
        new_label = 0
        counter = 0
        for old_label in self.classes:
            if new_order.keys().__contains__(old_label):
                temp_label = new_order[old_label]
            else:
                new_order[old_label] = new_label
                temp_label = new_label
                new_label = new_label + 1
            new_dataset.add_series(temp_label, self.series_data[counter])
            counter = counter + 1

        new_dataset.set_initial_class_order(new_order)
        new_dataset.set_reordered(True)
        return new_dataset

    def set_reordered(self, status):
        self.is_ordered = status

    def set_initial_class_order(self, initial_order):
        self.initial_class_labels = initial_order

    def _get_initial_class_labels(self):
        return self.initial_class_labels

    def sample_n(self, n_items):
        n = n_items
        if n > self.expected_size:
            n = self.expected_size
        sample = ListDataset(expected_size=n, length=self.length)
        for i in range(0, n - 1):
            sample.add_series(self.classes[i], self.series_data[i])

        return sample

    def swap(self, init, final):
        tmp_series = self.series_data[final]
        tmp_label = self.classes[final]

        self.series_data[final] = self.series_data[init]
        self.classes[final] = self.classes[init]

        self.series_data[init] = tmp_series
        self.classes[init] = tmp_label

    def shuffle(self):
        random.shuffle(self.series_data)
        random.shuffle(self.classes)

    @staticmethod
    def stdv(dataset):
        suma = 0
        suma2 = 0
        for serie in dataset.series_data:
            for i in range(0, len(serie)):
                suma = suma + serie[i]
                suma2 = suma2 + serie[i] * serie[i]
        n = len(dataset.series_data) * len(dataset.series_data[0])
        mean = suma / n
        return math.sqrt(abs(suma2 / (n - (mean * mean))))
