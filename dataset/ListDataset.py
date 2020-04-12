from numpy.distutils.fcompiler import none
import random


class ListDataset:

    def __init__(self, expected_size=0, length=0):
        self.series_data = list()
        self.labels = list()
        self.class_size_map = dict()
        self.initial_class_labels = dict()
        self.lenght = length
        self.is_ordered = False
        self.expected_size = expected_size

    def set_lenght(self, length):
        self.lenght = length

    def set_expected_size(self, size):
        self.expected_size = size

    def get_data_size(self):
        return len(self.series_data)

    def get_data(self):
        return self.series_data

    def get_labels(self):
        return self.labels

    def get_new_class_map(self):
        return self.initial_class_labels

    def get_lenght(self):
        return self.lenght

    def set_order(self, order):
        self.is_ordered = order

    def is_ordered(self):
        return self.is_ordered

    def get_expected_size(self):
        return len(self.class_size_map.keys())

    def add_series(self, label, series):
        self.expected_size = self.expected_size + 1
        self.series_data.append(series)
        self.labels.append(label)
        exists = False
        for lab in self.class_size_map.keys():
            if lab == label:
                exists = True
                self.class_size_map[label] = self.class_size_map.get(label) + 1
        if not exists:
            self.class_size_map[label] = 1

    def remove_item(self, i):
        label = self.labels[i]
        if self.class_size_map[label] != none:
            count = self.class_size_map[label]
            if count > 0:
                self.class_size_map[label] = count - 1
            else:
                self.class_size_map.pop(label)
        self.series_data.pop(i)
        self.labels.pop(i)
        self.expected_size = self.expected_size - 1

    def get_series(self, i):
        return self.series_data[i]

    def get_class(self, i):
        return self.labels[i]

    def get_num_classes(self):
        return len(self.class_size_map)

    def get_class_size(self, label):
        return self.class_size_map[label]

    def get_class_map(self):
        return self.class_size_map

    def get_unique_classes(self):
        keys = self.class_size_map.keys()
        unique_classes = [None] * len(keys)
        i = 0
        for key in keys:
            unique_classes[i] = key
            i = i + 1

        return unique_classes

    def get_unique_classes_as_set(self):
        return self.class_size_map.keys()

    def split_classes(self):
        split = dict()
        size = self.get_expected_size()
        for i in range(0, size):
            label = self.labels[i]
            if label != none:
                class_set = ListDataset(expected_size=size)
                split[label] = class_set
                split[label].add_series(label, self.series_data[i])
        return split

    def gini(self):
        total_sum = 0
        total_size = len(self.series_data)
        for item in self.class_size_map.keys():
            p = (self.class_size_map[item] / total_size)
            total_sum = total_sum + p * p
        return 1 - total_sum

    def _internal_data_list(self):
        return self.series_data

    def _internal_class_list(self):
        return self.labels

    def reorder_class_labels(self, new_order):
        new_dataset = ListDataset(expected_size=self.expected_size, length=self.lenght)
        if new_order == none:
            new_order = dict()

        size = self.expected_size
        new_label = 0
        old_label = 0
        for i in range(0, size - 1):
            old_label = self.labels[i]

            if new_order[old_label] != none:
                temp_label = new_order[old_label]
            else:
                new_order[old_label] = new_label
                temp_label = new_label
                new_label = new_label + 1
            new_dataset.add_series(temp_label, self.series_data[i])

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
        sample = ListDataset(expected_size=n, length=self.lenght)

        # TODO: self.shuffle

        for i in range(0, n - 1):
            sample.add_series(self.labels[i], self.series_data[i])

        return sample

    def swap(self, init, final):
        tmp_series = self.series_data[final]
        tmp_label = self.labels[final]

        self.series_data[final] = self.series_data[init]
        self.labels[final] = self.labels[init]

        self.series_data[init] = tmp_series
        self.labels[init] = tmp_label

    def shuffle(self):
        random.shuffle(self.series_data)
        random.shuffle(self.labels)
