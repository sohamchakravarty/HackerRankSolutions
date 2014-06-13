#!/bin/python
from math import ceil

def Flowers(C,N,K):
    limit = int(ceil(float(N)/K))
    amt = 0
    x = 0
    for i in xrange(limit):
        amt += sum([(x+1)*j for j in C[i*K:(i+1)*K]])
        x += 1
    return amt

if __name__=="__main__":
    # code snippet illustrating input/output methods 
    N, K = [int(x) for x in raw_input().split()]
    C = [int(x) for x in raw_input().split()]
    print Flowers(sorted(C,reverse = True),N,K)
