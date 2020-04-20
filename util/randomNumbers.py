# import the random module
import random
import sys
import numpy as np
from dataset import ListDataset as ldt


# define the main function

class randomNumbers:

    @staticmethod
    def generate_label():
        return "Label" + str(random.randint(0, 10))

    @staticmethod
    def generate_random_array(N):
        counter = 0
        lista = list()
        for i in range(0, N):
            numero = np.double("%.2f" % random.uniform(0, 5))
            lista.append(numero)
        return np.asarray(lista)

    @staticmethod
    def generate_several_arrays(num_arrays, array_length):
        array_list = list()
        for i in range(0, num_arrays):
            array_list.append(randomNumbers.generate_random_array(array_length))
        return array_list

    @staticmethod
    def generate_n_arrays_different_len(num_arrays):
        array_list = list()
        for i in range(0, num_arrays):
            array_length = random.randint(4, 7)
            array_list.append(randomNumbers.generate_random_array(array_length))
        return array_list

    @staticmethod
    def generate_empty_dataset():
        return ldt.ListDataset()

    pass

    @staticmethod
    def insert_array_in_dataset(array, dt: ldt):
        if dt is None:
            return
        if len(array) == 0 or array is None:
            return
        label = randomNumbers.generate_label()
        dt.add_series(label, array)

    @staticmethod
    def insert_arraylist_in_dataset(lista: list, dt: ldt):
        for l in lista:
            randomNumbers.insert_array_in_dataset(l, dt)

    @staticmethod
    def create_multiple_datasets(num_datasets, num_arrays):
        datasets_list = list()

        for i in range(0, num_datasets):
            # n_array = random.randint(num_arrays, num_arrays + 2)
            dt = randomNumbers.generate_empty_dataset()
            arays = randomNumbers.generate_n_arrays_different_len(num_arrays)
            randomNumbers.insert_arraylist_in_dataset(arays, dt)
            datasets_list.append(dt)
        return datasets_list

    @staticmethod
    def generate_dataset(num_series, len_serie):
        dt = randomNumbers.generate_empty_dataset()
        arrays_ = randomNumbers.generate_several_arrays(num_series, len_serie)
        randomNumbers.insert_arraylist_in_dataset(arrays_, dt)
        return dt

    @staticmethod
    def generate_dataset_with_labels(labels: list, num_series, len_serie):
        dt = randomNumbers.generate_empty_dataset()
        arrays_ = randomNumbers.generate_several_arrays(num_series, len_serie)
        counter = 0
        for array in arrays_:
            if dt is None:
                return
            if len(array) == 0 or array is None:
                continue
            else:
                label = labels.__getitem__(counter)
                dt.add_series(label, np.asarray(array))
                counter = counter + 1
        return dt

    @staticmethod
    def generate_dataset_multiple_series(series_per_array, num_series, len_serie):
        contador = 0
        dt = randomNumbers.generate_empty_dataset()
        while contador < num_series:
            arrays_ = randomNumbers.generate_several_arrays(series_per_array, len_serie)
            label = randomNumbers.generate_label()
            dt.add_series(label, np.asarray(arrays_))
            contador = contador + 1
        return dt


if __name__ == '__main__':
    lista = randomNumbers.create_multiple_datasets(4, 5)
    counter = 0
    for l in lista:
        print("lista", counter)
        for serie in l.series_data:
            print(serie)
        counter = counter + 1
