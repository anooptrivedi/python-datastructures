__author__ = 'anooptrivedi'

n = 100

# total time = c * n * n = cn^2 = O(n^2)

#outer loop executes n times
for i in range(1,n):
    for j in range(1, n):     #inner loop executes n times
        print('i value', i, 'j value', j) # constant time

