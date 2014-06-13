# Enter your code here. Read input from STDIN. Print output to STDOUT
def factorial(n):
    if n==0: return 1
    return reduce(lambda x,y:x*y,range(1,n+1))

def getAnswer(word):
    count = {}
    for char in word:
        if char not in count: count[char] = 1
        else: count[char]+=1
    if len(count)==1:
        return 1
            
    arr = map(lambda val:val>>1 if val%2==0 else (val-1)>>1,count.values())
    numerator = factorial(sum(arr))
    denominator = reduce(lambda x,y:x*y,map(factorial,arr))
    return (numerator/denominator)%(10**9+7)
 
    
def main():
  word = raw_input()
  print getAnswer(word)  

if __name__ == '__main__':
  main()
