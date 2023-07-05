while True:
    n=int(input())
    i=1
    if n<0:
        break
    while n>=1:
        i=i*n
        n=n-1
    print(i)