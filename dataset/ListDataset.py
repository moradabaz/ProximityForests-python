import random


class ListDataset:

    def __init__(self, expected_size=0, length=0):
        self.series_data = list()
        self.labels = list()
        self.class_map = dict()
        self.initial_class_labels = dict()
        self.lenght = length
        self.is_ordered = False
        self.expected_size = expected_size

    def set_lenght(self, length):
        self.lenght = length

    def set_expected_size(self, size):
        self.expected_size = size

    def get_series_size(self):
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
        return self.series_data.__len__()

    def add_series(self, label, series):
        #self.expected_size = self.expected_size + 1
        self.series_data.append(series)
        self.labels.append(label)
        exists = False
        for lab in self.class_map.keys():
            if lab == label:
                exists = True
                self.class_map[label] = self.class_map[label] + 1
        if not exists:
            self.class_map[label] = 1

    def remove_item(self, i):
        label = self.labels[i]
        if self.class_map[label] is not None:
            count = self.class_map[label]
            if count > 0:
                self.class_map[label] = count - 1
            else:
                self.class_map.pop(label)
        self.series_data.pop(i)
        self.labels.pop(i)
        self.expected_size = self.expected_size - 1

    def get_series(self, i):
        return self.series_data[i]

    def get_class(self, i):
        return self.labels[i]

    def get_num_classes(self):
        return len(self.class_map)

    def get_class_size(self, label):
        return self.class_map[label]

    def get_class_map(self):
        return self.class_map

    def get_unique_classes(self):
        keys = self.class_map.keys()
        unique_classes = [None] * len(keys)
        i = 0
        for key in keys:
            unique_classes[i] = key
            i = i + 1

        return unique_classes

    def get_unique_classes_as_set(self):
        return self.class_map.keys()

    def split_classes(self):
        split = dict()
        size = self.get_expected_size()
        contador = 0
        # for label in self.labels:
        for i in range(0, self.labels.__len__()):
            label = self.labels.__getitem__(i)

            if not split.keys().__contains__(label):
                class_set = ListDataset()
                split[label] = class_set
            split[label].add_series(label, self.series_data[i])
        return split

    def gini(self):
        total_sum = 0
        total_size = len(self.series_data)
        for item in self.class_map.keys():
            p = (self.class_map[item] / total_size)
            total_sum = total_sum + p * p
        return 1 - total_sum

    def _internal_data_list(self):
        return self.series_data

    def _internal_class_list(self):
        return self.labels

    def reorder_class_labels(self, new_order):
        new_dataset = ListDataset()
        if new_order is None:
            new_order = dict()

        size = self.expected_size
        new_label = 0
        old_label = 0
        counter = 0
        for old_label in self.labels:
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
