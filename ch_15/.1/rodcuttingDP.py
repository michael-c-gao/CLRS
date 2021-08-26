import math
#rod-cutting dynamic programming
"""
TD == top down
BU == bottom up
"""

def rodcutTD(p,n):
    r = [-math.inf] * (n+1)
    return memorodcutTD(p,n,r)

def memorodcutTD(p,n,r):
    if r[n] != -math.inf:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -math.inf
        for i in range(0, n):
            q = max(q, p[i] + memorodcutTD(p,n-i-1,r))
    r[n] = q
    
    return q

def rodcutBU(p,n):
    r = [0] * (n+1)
    r[0] = 0
    for i in range(1,n+1):
        q = -math.inf
        for j in range(i):
            q = max(q, p[j]+ r[i-j-1])
        r[i] = q
    
    return r[n]
            

def main():
    array = [1,5,8,9,10,17,17,20,24,30]
    arrayLen = len(array)
    
    print(rodcutTD(array, arrayLen))
    print(rodcutBU(array,arrayLen))

if __name__ == "__main__":
    main()
