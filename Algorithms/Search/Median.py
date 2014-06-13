#!/bin/python
from bisect import bisect_right
def median(arr,n):
    mid = n//2
    if n%2 :
        return arr[mid]
    else :
        return (arr[mid]+arr[mid-1])/2.0

length = 0
def addElement(arr,e):
    global length
    if not arr:
        arr.append(e)
    else:
        pos = bisect_right(arr,e)
        arr.insert(pos,e)
    length += 1
    return True

def delElement(arr,e):
    global length
    if not arr:
        return False
    else:
        try:
            arr.remove(e)
            length -= 1
        except ValueError:
            return False
    return True

if __name__=="__main__":
    N = input()
    arr = []
    flag = False
    global length 
    for i in xrange(N):
        op, val = raw_input().split()
        val = int(val)
        if op=='a':
            flag = addElement(arr,val)
        else:
            flag = delElement(arr,val)
        
        if flag and length>0 and length%2:
            print median(arr,length)
        elif flag and length:
            print str(median(arr,length)).rstrip('0').rstrip('.')
        else:
            print "Wrong!"