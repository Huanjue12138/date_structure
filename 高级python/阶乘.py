def jc(n):
    if n <= 2 :
        return n
    return jc(n-1)*n
