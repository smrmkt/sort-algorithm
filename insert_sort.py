# -*- coding: utf-8 -*-


class InsertSort():
    
    def __init__(self, a):
        self.a = a

    def execute(self):
        for i in range(1, len(self.a)):
            v = self.a[i]
            j = i
            while self.a[j-1] > v:
                self.a[j] = self.a[j-1]
                j -= 1
                if j <= 0:
                    break
            self.a[j] = v
        return self.a