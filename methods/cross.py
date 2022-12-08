import random
from numpy.random import rand
from algorithms.functions import beale_function


def arithmeticCrossover(p1, p2, r_cross):
    if rand() < r_cross:
        k = rand()
        x1n = k * p1[0] + (1 - k) * p1[1]
        y1n = k * p2[0] + (1 - k) * p2[1]
        x2n = (1 - k) * p1[0] + k * p1[1]
        y2n = (1 - k) * p2[0] + k * p2[1]
        xn = [x1n, y1n]
        yn = [x2n, y2n]
        return [xn, yn]
    return [p1, p2]


def linearCrossover(p1, p2, minmax, r_cross, bounds=[-4.5, 4.5]):
    if rand() < r_cross:
        Z = [-1 * p1[0] + p1[1] / 2, p2[0] / 2 + p2[1] / 2]
        if Z[0] > bounds[1]:
            Z[0] = bounds[1]
        elif Z[0] < bounds[0]:
            Z[0] = bounds[0]
        if Z[1] > bounds[1]:
            Z[1] = bounds[1]
        elif Z[1] < bounds[0]:
            Z[1] = bounds[0]
        V = [3 * p1[0] / 2 - p1[1] / 2, 3 * p2[0] / 2 - p2[1] / 2]
        if V[0] > bounds[1]:
            V[0] = bounds[1]
        elif V[0] < bounds[0]:
            V[0] = bounds[0]
        if V[1] > bounds[1]:
            V[1] = bounds[1]
        elif V[1] < bounds[0]:
            V[1] = bounds[0]
        W = [-1 * p1[0] / 2 + 3 * p1[1] / 2, -1 * p2[0] / 2 + 3 * p2[1] / 2]
        if W[0] > bounds[1]:
            W[0] = bounds[1]
        elif W[0] < bounds[0]:
            W[0] = bounds[0]
        if W[1] > bounds[1]:
            W[1] = bounds[1]
        elif W[1] < bounds[0]:
            W[1] = bounds[0]
        output = []
        output.append([beale_function(Z), Z])
        output.append([beale_function(V), V])
        output.append([beale_function(W), W])
        output.sort()
        if not minmax:
            return [output[0][1], output[1][1]]
        else:
            return [output[2][1], output[1][1]]
    return [p1, p2]


def blendCrossoverA(p1, p2, a, r_cross, bounds=[-4.5, 4.5]):
    if rand() < r_cross:
        d1 = abs(p1[0] - p2[0])
        d2 = abs(p1[1] - p2[1])
        x1n = random.uniform(min(p1[0], p2[0]) - a * d1, max(p1[0], p2[0]) + a * d1)
        if x1n > bounds[1]:
            x1n = bounds[1]
        elif x1n < bounds[0]:
            x1n = bounds[0]
        y1n = random.uniform(min(p1[1], p2[1]) - a * d1, max(p1[1], p2[1]) + a * d1)
        if y1n > bounds[1]:
            y1n = bounds[1]
        elif y1n < bounds[0]:
            y1n = bounds[0]
        x2n = random.uniform(min(p1[0], p2[0]) - a * d2, max(p1[0], p2[0]) + a * d2)
        if x2n > bounds[1]:
            x2n = bounds[1]
        elif x2n < bounds[0]:
            x2n = bounds[0]
        y2n = random.uniform(min(p1[1], p2[1]) - a * d2, max(p1[1], p2[1]) + a * d2)
        if y2n > bounds[1]:
            y2n = bounds[1]
        elif y2n < bounds[0]:
            y2n = bounds[0]
        xn = [x1n, y1n]
        yn = [x2n, y2n]
        return [xn, yn]
    return [p1, p2]


def blendCrossoverAB(p1, p2, a, b, r_cross, bounds=[-4.5, 4.5]):
    if rand() < r_cross:
        d1 = abs(p1[0] - p2[0])
        d2 = abs(p1[1] - p2[1])
        x1n = random.uniform(min(p1[0], p2[0]) - a * d1, max(p1[0], p2[0]) + b * d1)
        if x1n > bounds[1]:
            x1n = bounds[1]
        elif x1n < bounds[0]:
            x1n = bounds[0]
        y1n = random.uniform(min(p1[1], p2[1]) - a * d1, max(p1[1], p2[1]) + b * d1)
        if y1n > bounds[1]:
            y1n = bounds[1]
        elif y1n < bounds[0]:
            y1n = bounds[0]
        x2n = random.uniform(min(p1[0], p2[0]) - a * d2, max(p1[0], p2[0]) + b * d2)
        if x2n > bounds[1]:
            x2n = bounds[1]
        elif x2n < bounds[0]:
            x2n = bounds[0]
        y2n = random.uniform(min(p1[1], p2[1]) - a * d2, max(p1[1], p2[1]) + b * d2)
        if y2n > bounds[1]:
            y2n = bounds[1]
        elif y2n < bounds[0]:
            y2n = bounds[0]
        xn = [x1n, y1n]
        yn = [x2n, y2n]
        return [xn, yn]
    return [p1, p2]


def averageCrossover(p1, p2, r_cross):
    if rand() < r_cross:
        x1n = (p1[0] + p2[0]) / 2
        y1n = (p1[1] + p2[1]) / 2
        xn = [x1n, y1n]
        return [xn, xn]
    return [p1, p2]
