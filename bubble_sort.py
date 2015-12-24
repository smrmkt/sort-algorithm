# -*- coding: utf-8 -*-

import argparse
import random
import time


def init_array(n):
    return [random.randrange(n*10) for i in range(n)]


def bubble_sort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, nargs='?', default=20)
    parser.add_argument('-d', type=bool, nargs='?', default=0)
    n = parser.parse_args().n
    debug = parser.parse_args().d

    a = init_array(n)
    if debug:
        print a
    start = time.time()
    bubble_sort(a)
    if debug:
        print a
    erapsed = time.time() - start
    print erapsed
