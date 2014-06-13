def ClosestNumbers(array,n):
    diff = []
    small = array[0]-array[1]
    for i in xrange(n-1):
        diff.append(array[i]-array[i+1])
        if small>diff[i]:
            small = diff[i]

    res = []
    for i in xrange(n-1):
        if diff[i]==small:
            res.append(array[i])
            res.append(array[i+1])
    return res

if __name__=="__main__":
    n = input()
    array = sorted([int(x) for x in raw_input().split()],reverse = True)
    for value in ClosestNumbers(array,n)[::-1]:
        print value,
    
    