def CountValues(array):
    dct = {}
    for i in array:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    return dct
    
def MissingNumbers(dictA, dictB):
    res = []
    for i in sorted(dictB):
        if i in dictA and dictB[i]-dictA[i]!=0:
            res.extend([i])
    return res

if __name__=="__main__":
    n = input()
    A = [int(i) for i in raw_input().split()]
    m = input()
    B = [int(i) for i in raw_input().split()]
    
    #Create count hashes
    countA = CountValues(A)
    countB = CountValues(B)

    for num in MissingNumbers(countA,countB):
        print num,
