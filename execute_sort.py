# -*- coding: utf-8 -*-

import argparse
import random
import time

from bubble_sort import BubbleSort
from insert_sort import InsertSort
from quick_sort import QuickSort
from simple_quick_sort import SimpleQuickSort


sorts = {
    'bubble': BubbleSort,
    'insert': InsertSort,
    'quick': QuickSort,    
    'squick': SimpleQuickSort
}


def init_array(n, is_ordered):
    if is_ordered:
        return [i for i in range(n)]
    return [random.randrange(n*10) for i in range(n)]


if __name__ == '__main__':
    # parse args
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', type=str, nargs='?', default='bubble',
                        choices=['bubble', 'insert', 'quick', 'squick'])
    parser.add_argument('-d',action='store_true', default=False)
    parser.add_argument('-n', type=int, nargs='?', default=20)
    parser.add_argument('-o',action='store_true', default=False)
    n = parser.parse_args().n
    is_debug = parser.parse_args().d
    algorithm = parser.parse_args().a
    is_ordered = parser.parse_args().o

    # execute sort    
    before = init_array(n, is_ordered)
    if is_debug:
        print before
    start = time.time()
    sort = sorts[algorithm]
    after = sort(before).execute()
    if is_debug:
        print after
    erapsed = time.time() - start
    print erapsed
