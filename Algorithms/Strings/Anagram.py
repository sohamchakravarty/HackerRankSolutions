#!/usr/bin/py
def Compare(str1,str2):
    count = 0
    for char in str1:
        if char not in str2:
            count += 1
        if char in str2:
            str2 = str2.replace(char,'',1)
    return count

def Anagram(string):
    length = len(string)
    if length%2: return -1
    a = string[:length>>1]
    b = string[length>>1:]
    return Compare(a,b)

if __name__=="__main__":
    for _ in range(input()):
        print Anagram(raw_input())