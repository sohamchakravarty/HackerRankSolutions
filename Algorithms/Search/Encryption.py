from math import sqrt,floor,ceil
from itertools import izip_longest

if __name__=="__main__":
    string = raw_input();
    
    #Build matrix
    length = len(string)
    var = sqrt(length)
    row = int(floor(var))
    col = int(ceil(var))
    if row*col<length:
        row += 1
    
    matrix = [list(string[j:j+col]) for i,j in zip(xrange(int(row)),xrange(0,length,col)) ]
    
    for i in [[j for j in i if j is not None] for i in izip_longest(*matrix)]:
        print ''.join(i),
    