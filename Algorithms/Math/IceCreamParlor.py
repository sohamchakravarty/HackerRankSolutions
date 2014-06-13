MAX = 10001
def CountingSort(arr,N):
    # Create a count array to store count of inidividul characters and
    # initialize count array as 0
    count = [0 for i in range(MAX)]
        
    # Store count of each character
    for i in arr:
        count[i] += 1
    
    # Change count[i] so that count[i] now contains actual position of
    # this number in output array
    for i in range(1,MAX):
        count[i]+=count[i-1]
    
    # Build the output character array
    output = [0 for i in range(N)]
    for i in arr:
        output[count[i]-1] = i
        count[i] -= 1
    
    return output

def GetFlavors(arr,M,N):
    i = 0
    j = N-1
    while i<j:
        if M-arr[j] < arr[i]: j-=1
        elif M-arr[j] > arr[i]: i+=1
        else: return arr[i],arr[j]

def GetIndices(arr,N,elements):
    posX = posY = -1
    for pos in xrange(N):
        if posX>0 and posY>0: break
        if posX<0 and arr[pos]==elements[0]: posX = pos+1
        elif arr[pos]==elements[1]: posY = pos+1
    return posX,posY
        

if __name__=="__main__":
    for _ in range(input()):
        M = input()
        N = input()
        arr = [int(x) for x in raw_input().split()]
        vals = sorted(GetIndices(arr,N,GetFlavors(CountingSort(arr,N),M,N)))
        print '{0} {1}'.format(vals[0],vals[1])
        