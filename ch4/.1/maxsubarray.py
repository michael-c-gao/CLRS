#maximum subarray (recursive)
import math

def findmaxsubarray(array, low, high):
    if(high == low):
        return(low,high,array[low])
    else:
        mid = ((low+high)//2)
        (leftlow,lefthigh,leftsum) = findmaxsubarray(array,low,mid)
        (rightlow,righthigh,rightsum) = findmaxsubarray(array,mid+1,high)
        (crosslow,crosshigh,crosssum) = findmaxcrossingsubarray(array,low,mid,high)
        if((leftsum >= rightsum) and (leftsum >= crosssum)):
            return (leftlow, lefthigh, leftsum)
        elif ((rightsum >= leftsum) and (rightsum >= crosssum)):
            return(rightlow,righthigh,rightsum)
        else:
            return(crosslow,crosshigh,crosssum)
    
def findmaxcrossingsubarray(array,low,mid,high):
    leftsum = -math.inf
    maxleft = None
    maxright= None
    Sum = 0
    for i in range(mid, low-1, -1):
        Sum = Sum + array[i]
        if(Sum > leftsum):
            leftsum = Sum
            maxleft = i
    rightsum = -math.inf
    Sum = 0
    for j in range((mid+1), high):
        Sum = Sum + array[j]
        if(Sum > rightsum):
            rightsum = Sum
            maxright = j
    return(maxleft,maxright, (leftsum+rightsum))
            
            



def main():
    a = findmaxsubarray([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7],0,15)
    print(a)





if __name__ == '__main__':
        main()
