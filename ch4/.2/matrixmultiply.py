#square matrix multiply

def matrixmultiply(a,b):
    n = len(a)
    c = [[0 for i in range(n)] for j in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            for k in range(0,n):
                c[i][j] = c[i][j] + a[i][k]*b[k][j]
    return c


def main():
    print(matrixmultiply([[1,2,3],[1,2,3],[1,2,3]],[[1,2,3],[1,2,3],[1,2,3]]))

if __name__ == "__main__":
    main()
