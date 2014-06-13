string = list(raw_input())

count = {}
for char in string:
    if char not in count: count[char] = 1
    else: count[char]+=1

found = False
if not len(string)%2:
    found = True if all(count[char]%2==0 for char in count) else False
else:
    vals = set(count.values())
    if len(vals)==1: found = True #check for string = 'aaaaa'
    found = True if not found and sum(vals)%2 else False 
        

if not found:
    print("NO")
else:
    print("YES")
