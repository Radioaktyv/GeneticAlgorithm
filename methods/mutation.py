from numpy.random import rand
from numpy import random
from random import randint


def evenMutation(p1, r_mut, bounds=[-4.5, 4.5]):
    c1 = p1.copy()
    if rand() < r_mut:
        if randint(1, 2) == 1:
            c1[0] = random.uniform(bounds[0], bounds[1])
        else:
            c1[1] = random.uniform(bounds[0], bounds[1])
    return c1


def gaussMutation(p1, r_mut):
    c1 = p1.copy()
    if rand() < r_mut:
        c1 = [p1[0] + random.normal(), p1[1] + random.normal()]
    return c1
