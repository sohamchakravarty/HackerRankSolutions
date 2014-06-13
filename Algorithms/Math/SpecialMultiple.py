def SpecialMultiple(N):
    i = 1
    multiplier = int(bin(i).replace('0b',''))
    while 9*multiplier%N :
        i+=1
        multiplier = int(bin(i).replace('0b',''))
    return 9*multiplier
    
if __name__=="__main__":
    for _ in range(input()):
        print SpecialMultiple(input())