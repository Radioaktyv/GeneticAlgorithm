from numpy.random import randint
from numpy.random import rand
from algorithms.functions import beale_function
import numpy as np


def arithmeticCrossover(p1, p2):
    k = rand()
    x1n = k * p1[0] + (1 - k) * p1[1]
    y1n = k * p2[0] + (1 - k) * p2[1]
    x2n = (1 - k) * p1[0] + k * p1[1]
    y2n = (1 - k) * p2[0] + k * p2[1]
    xn = [x1n, y1n]
    yn = [x2n, y2n]
    return [xn, yn]


def linearCrossover(p1, p2, minmax):
    Z = [-1 * p1[0] + p1[1] / 2, p2[0] / 2 + p2[1] / 2]
    V = [3 * p1[0] / 2 - p1[1] / 2, 3 * p2[0] / 2 - p2[1] / 2]
    W = [-1 * p1[0] / 2 + 3 * p1[1] / 2, -1 * p2[0] / 2 + 3 * p2[1] / 2]
    output = np.array(3)
    output[0] = [beale_function(Z), Z]
    output[1] = [beale_function(V), V]
    output[2] = [beale_function(W), W]
    output = output.sort()
    if minmax == 'min':
        return [output[0][1], output[1][1]]
    else:
        return [output[2][1], output[1][1]]


def blendCrossoverA(p1, p2, a, r_cross):
    if rand() < r_cross:
        d1 = abs(p1[0] - p2[0])
        d2 = abs(p1[1] - p2[1])
        x1n = rand(min(p1[0], p2[0]) - a * d1, max(p1[0], p2[0]) + a * d1)
        y1n = rand(min(p1[1], p2[1]) - a * d1, max(p1[1], p2[1]) + a * d1)

        x2n = rand(min(p1[0], p2[0]) - a * d2, max(p1[0], p2[0]) + a * d2)
        y2n = rand(min(p1[1], p2[1]) - a * d2, max(p1[1], p2[1]) + a * d2)
        xn = [x1n, y1n]
        yn = [x2n, y2n]
        return [xn, yn]
    return [p1, p2]


def blendCrossoverAB(p1, p2, a, b):
    d1 = abs(p1[0] - p2[0])
    d2 = abs(p1[1] - p2[1])
    x1n = rand(min(p1[0], p2[0]) - a * d1, max(p1[0], p2[0]) + b * d1)
    y1n = rand(min(p1[1], p2[1]) - a * d1, max(p1[1], p2[1]) + b * d1)
    x2n = rand(min(p1[0], p2[0]) - a * d2, max(p1[0], p2[0]) + b * d2)
    y2n = rand(min(p1[1], p2[1]) - a * d2, max(p1[1], p2[1]) + b * d2)
    xn = [x1n, y1n]
    yn = [x2n, y2n]
    return [xn, yn]


def averageCrossover(p1, p2, r_cross):
    if rand() < r_cross:
        x1n = (p1[0] + p2[0]) / 2
        y1n = (p2[0] + p2[0]) / 2
        xn = [x1n, y1n]
        return [x1n, y1n]
    return [p1, p2]
