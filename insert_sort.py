# -*- coding: utf-8 -*-


class InsertSort():
    
    @staticmethod
    def execute(a):
        for i in range(1, len(a)):
            v = a[i]
            j = i
            while a[j-1] > v:
                a[j] = a[j-1]
                j -= 1
                if j <= 0:
                    break
            a[j] = v
        return a