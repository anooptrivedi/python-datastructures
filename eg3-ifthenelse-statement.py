__author__ = 'anooptrivedi'

n = 200

#total time = c0 + c1 * n = O(n)

if (n==1):
    print ("Wrong value") #constant time, c0
else:
    for i in range (1, n): # n times
        print("Current number", i) #constant time, c1