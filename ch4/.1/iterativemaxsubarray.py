import math

def iterativemaxsubarray(array):
    
    maxsum = -math.inf
    Sum = -math.inf
    arraylen = len(array)
    
    for i in range(0, arraylen):
        currhigh = i
        if Sum > 0:
            Sum = Sum + array[i]
        else:
            currlow = i
            Sum = array[i]
            
        if Sum > maxsum:
            maxsum = Sum
            low = currlow
            high = currhigh
    return (low, high, maxsum)

def main():
    a = iterativemaxsubarray([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7])
    print(a)
    
if __name__ == '__main__':
    main()
