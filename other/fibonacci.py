def fibonacci(n):
    if n == 1 or n ==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def memoFib(n,array):
    if array[n-1] != -1:
        return array[n-1]
    if n == 1 or n == 2:
        result = 1
    else:
        result = memoFib(n-1,array) + memoFib(n-2,array)
    array[n-1] = result
    return result

def iterFib(n,array):
    array[0] = 1
    array[1] = 1
    for i in range(2, len(array)):
        array[i] = array[i-1]+ array[i-2]
    return array[-1]
    

def main():
    n = 723
    array = [-1] * n
    array2 = [-1]*n
    print(memoFib(n,array))
    print("\n")
    print(iterFib(n,array2))
    #print(array2)
     


if __name__ == "__main__":
    main()
