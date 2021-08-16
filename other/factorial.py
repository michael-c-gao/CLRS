def factorial(n):
    if (n >= 1):
        return (n * factorial(n-1))
    else:
        return 1

def main():
    n = 120
    print(factorial(n))
    


if __name__ == "__main__":
    main()
