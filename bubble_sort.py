# -*- coding: utf-8 -*-


class BubbleSort():
    
    def __init__(self, a):
        self.a = a
    
    def execute(self):
        for i in range(len(self.a)-1, 0, -1):
            for j in range(i):
                if self.a[j] > self.a[j+1]:
                    self.a[j], self.a[j+1] = self.a[j+1], self.a[j]
        return self.a
