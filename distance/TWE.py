import numpy as np
import math
import random as rand


class TWE:
    twe_params = [0.00001, 0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1]
    twe_lamdaParams = [0, 0.011111111, 0.022222222, 0.033333333, 0.044444444, 0.055555556, 0.066666667,
                       0.077777778, 0.088888889, 0.1]

    @staticmethod
    def distance(first, second, nu, lambada):

        m = len(first)
        n = len(second)
        max_lenght = max(m, n)
        r = len(first)
        c = len(second)

        D = np.zeros([max_lenght+1, max_lenght+1])
        Di1 = np.zeros([max_lenght+1])
        Dj1 = np.zeros([max_lenght+1])

        for j in range(1, c + 1):
            distj1 = 0
            if j > 1:
                distj1 = distj1 + math.pow((second[j - 2] - second[j - 1]), 2)
            else:
                distj1 = distj1 + math.pow(second[j - 1], 2)
            Dj1[j] = distj1

        for i in range(1, r + 1):
            disti1 = 0
            if i > 1:
                disti1 = disti1 + math.pow((first[i - 2] - first[i - 1]), 2)
            else:
                disti1 = disti1 + math.pow(first[i - 1], 2)
            Di1[i] = disti1

            for j in range(1, c + 1):
                dist = 0
                dist = dist + math.pow((first[i - 1] - second[j - 1]), 2)
                if i > 1 and j > 1:
                    dist = dist + math.pow((first[i - 2] - second[j - 2]), 2)
                D[i][j] = dist
        D[0][0] = 0
        for i in range(1, r + 1):
            D[i][0] = D[i - 1][0] + Di1[i]
        for j in range(1, c + 1):
            D[0][j] = D[0][j - 1] + Dj1[j]

        for i in range(1, r + 1):
            for j in range(1, c + 1):
                h_trans = math.fabs(i - j)
                if i > 1 and j > 1:
                    h_trans = h_trans + math.fabs((i - 1) - (j - 1))
                dist0 = D[i - 1][j - 1] + nu * h_trans + D[i][j]
                dmin = dist0
                if i > 1:
                    h_trans = 1
                else:
                    h_trans = i
                dist = Di1[i] + D[i - 1][j] + lambada + nu * h_trans
                if dmin > dist:
                    dmin = dist
                if j > 1:
                    h_trans = 1
                else:
                    h_trans = j
                dist = Dj1[j] + D[i][j - 1] + lambada + nu * h_trans
                if dmin > dist:
                    dmin = dist
                D[i][j] = dmin
        dist = D[r][c]
        return dist

    @staticmethod
    def get_random_nu():
        return TWE.twe_params[rand.randint(0, len(TWE.twe_params)-1)]

    @staticmethod
    def get_random_lambda():
        return TWE.twe_params[rand.randint(0, len(TWE.twe_lamdaParams)-1)]
