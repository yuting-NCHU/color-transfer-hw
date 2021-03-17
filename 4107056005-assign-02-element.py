import math
def C(n, k):
    if n<k: return 0
    if n==k: return 1
    if k==1: return n
    f = math.factorial
    return f(n) // f(k) // f(n-k)

def cobidic(n, k, m):
    c=[]
    R=m
    s=n-1
    for x in range(k,0,-1):
        for i in range(s,k-2,-1):
            if C(i,x) <= R:
                k-=1
                s=i
                R-=C(i,x)
                c.append(i)
                break
    return c

def element(n, k, m):
    d = C(n, k)-1-m
    s = cobidic(n, k, d)
    s = map(lambda x: (n-1)-x, s)
    return s


while True:
    n, k, m = map(int,input('請輸入n, k, m (用空格隔開): ').split())
    if not(1<=n<=81 and 1<=k<=n and 0<=m<=C(n,k)-1):
        print('Error (1<=n<=81 1<=k<=n 0<=m<=C(n,k)-1)')
        continue

    for i in element(n, k, m): print(i,end=' ')
    print()
    
