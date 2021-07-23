#insertion sort

def insertionsort(array):
  #increasing insertion sort (ex. [1,2,3,4])
    lenarray = len(array)
    for j in range(1,lenarray):
        key = array[j]
        i = j-1
        while (i > -1 and array[i] > key):
            array[i+1] = array[i]
            i = i -1
        array[i+1] = key
    print(array)


def decreasinginsertionsort(array):
  #decreasing insertion sort (ex. [4,3,2,1])
    lenarray = len(array)
    for j in range(1,lenarray):
        key = array[j]
        i = j-1
        while (i > -1 and array[i] < key):
            array[i+1] = array[i]
            i = i -1
        array[i+1] = key
    print(array)
