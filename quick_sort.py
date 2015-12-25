# -*- coding: utf-8 -*-


class QuickSort():
    
    def __init__(self, a):
        self.a = a
    
    def sort(self, l, u):
        if (l >= u):
            return
        m = l
        for i in range(l+1, u+1):
            if self.a[i] < self.a[l]:
                m += 1
                self.a[m], self.a[i] = self.a[i], self.a[m]
        self.a[l], self.a[m] = self.a[m], self.a[l]
        self.sort(l, m-1)
        self.sort(m+1, u)
    
    def execute(self):
        self.sort(0, len(self.a)-1)
        return self.a
