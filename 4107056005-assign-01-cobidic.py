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
                c.append(str(i))
                # print(i,end=' ')
                break
    return c

while True:
    n, k, m = map(int,input('請輸入n, k, m (用空格隔開): ').split())
    if not(1<=n<=81 and 1<=k<=n and 0<=m<=C(n,k)-1):
        print('Error (1<=n<=81 1<=k<=n 0<=m<=C(n,k)-1)')
        continue
    # if not 1<=n<=81: 
    #     print('Error,請輸入適當的n: 1<=n<=81 ')
    #     continue
    # elif not 1<=k<=n: 
    #     print('Error,請輸入適當的k: 1<=k<={}(n)'.format(n))
    #     continue
    # elif not 0<=m<=C(n, k)-1: 
    #     print('Error,請輸入適當的m: 0<=m<={}(C(n, k)-1)'.format(C(n, k)-1))
    #     continue
        
    # cobidic(n, k, m)
    for i in cobidic(n, k, m): print(i,end=' ')
    print()

    #verify
    # r=0
    # for i,n in enumerate(cobidic(n, k, m)): 
    #     r+=C(int(n), k-i)
    # print(r)
    
