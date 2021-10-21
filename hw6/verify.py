def origin_formala(k):
    ans=0
    n=2**k-1
    for i in range(n+1): # i=0~n
        for j in range(n+1): # j=0~n
            ans += (i-j)**2
    return ans

def my_formala(k):
    x=2**(2*k)
    return x*(x-1)/6

for k in range(10):
    print(origin_formala(k))    
    print(my_formala(k))