# -*- coding: utf-8 -*-

import argparse
import random
import time

from bubble_sort import BubbleSort
from insert_sort import InsertSort


sorts = {
    'bubble': BubbleSort,
    'insert': InsertSort
}


def init_array(n):
    return [random.randrange(n*10) for i in range(n)]


if __name__ == '__main__':
    # parse args
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', type=str, nargs='?', default='bubble',
                        choices=['bubble', 'insert', 'quick'])
    parser.add_argument('-d',action='store_true', default=False)
    parser.add_argument('-n', type=int, nargs='?', default=20)
    n = parser.parse_args().n
    debug = parser.parse_args().d
    algorithm = parser.parse_args().a

    # execute sort    
    before = init_array(n)
    if debug:
        print before
    start = time.time()
    sort = sorts[algorithm]
    after = sort.execute(before)
    if debug:
        print after
    erapsed = time.time() - start
    print erapsed
