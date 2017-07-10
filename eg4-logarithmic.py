__author__ = 'anooptrivedi'

def logarithemic(n):
    i = 1
    while i < n:
        i = i*2 # i is doubling every time
        print(i)

logarithemic(100)

"""
log(2^k) = log(n)
klog2 = log(n)
k = log(n) - we assume Base2
Total Time = O(log(n))
"""