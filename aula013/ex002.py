def numerotriangular(n):
    for i in range(3,n+1):
        if (i-2)*(i-1)*(i)==n:
            return True
    return False
