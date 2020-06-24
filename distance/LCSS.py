import math
import random as rand
import numpy as np
import math


class LCSS:

    @staticmethod
    def distance(first, second, window_size=-1, epsilon=-1):
        if window_size == -1:
            window_size = len(first)

        length1 = len(first)
        length2 = len(second)

        min_length = min(length1, length2)

        matrix = np.zeros([length1, length1])

        matrix[0][0] = LCSS.sim(first[0], second[0], epsilon)
        for i in range(0, min(length1, 1 + window_size)):
            if LCSS.sim(first[i], second[i], epsilon) != 1:
                matrix[i][0] = matrix[i - 1][0]
            else:
                matrix[i][0] = LCSS.sim(first[i], second[0], epsilon)

        j = 1
        while j < min(length2, 1 + window_size):
            if LCSS.sim(first[0], second[j], epsilon) == 1:
                matrix[0][j] = LCSS.sim(first[0], second[0], epsilon)
            else:
                matrix[0][j] = matrix[0][j - 1]
            j = j + 1

        if j < length2:
            matrix[0][j] = -math.inf

        for i in range(0, length1):
            if (i - window_size) < 1:
                j_start = 1
            else:
                j_start = i - window_size
            if i + window_size + 1 > length2:
                j_stop = length2
            else:
                j_stop = i + window_size + 1

            if (i - window_size - 1) >= 0:
                matrix[i][i - window_size - 1] = -np.inf
            j = j_start
            while j < j_stop:
                if LCSS.sim(first[i], second[i], epsilon) == 1:
                    matrix[i][j] = matrix[i - 1][j - 1] + 1
                else:
                    matrix[i][j] = max(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j])
                j = j + 1
            if j_stop < length2:
                matrix[i][j_stop] = -np.inf
        res = 1.0 - (1.0 * matrix[length1 - 1][length2 - 1] / min_length)
        return res

    @staticmethod
    def sim(a, b, epsilon):
        if math.fabs((a - b)) <= epsilon:
            return 1
        return 0

    @staticmethod
    def get_random_epsilon(serie_length):
        std_train = statistics.stdev(serie_length)
        std_floor = std_train * 0.2
        return rand.random() * (std_train - std_floor) + std_floor

    @staticmethod
    def get_random_window(serie_lenght):
        return rand.randint(0, (serie_lenght + 1) / 4)
