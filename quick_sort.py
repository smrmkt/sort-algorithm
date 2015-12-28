# -*- coding: utf-8 -*-

import random


class QuickSort():
    
    def __init__(self, a):
        self.a = a

    def sort(self, l, u):
        if u-l <= 1:
            return
        m = random.randrange(l, u)
        self.a[l], self.a[m] = self.a[m], self.a[l]
        t = self.a[l]
        i = l
        j = u+1
        while True:
            i += 1
            j -= 1
            while i <= u and self.a[i] < t:
                i += 1
            while self.a[j] > t:
                j -= 1
            if i > j:
                break
            self.a[i], self.a[j] = self.a[j], self.a[i]
        self.a[l], self.a[j] = self.a[j], self.a[l]
        self.sort(l, j-1)
        self.sort(j+1, u)
    
    def execute(self):
        self.sort(0, len(self.a)-1)
        return self.a
