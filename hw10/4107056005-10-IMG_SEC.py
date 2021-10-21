import random
import math
from decimal import Decimal

with open("Input10.txt") as f:
    txt = f.read().split()

x0, rx = float(txt[0]),float(txt[1])
y0, ry = float(txt[2]),float(txt[3])
seed, N = int(txt[4]), int(txt[5])
L = float(txt[6])


random.seed(seed)
R1 = int(random.random()*N+1)
R2 = int(random.random()*N+1)
R3 = int(random.random()*N+1)

# print(seed,N)
# print(R1,R2,R3)

def logisticmap(x, r):
   
    return x * r * (1 - x)

# Return nth iteration of logisticmap(x. r)
def iterate(n, x, r):

    for i in range(n):
        x = logisticmap(x, r)

    return x
x = iterate(R1,x0,rx)
y = iterate(R2,y0,ry)

a = R1 + math.ceil(x/L)
b = R2 + math.ceil(y/L)

with open("Output10.txt",'w') as f:
    f.write("{} {}\n".format(txt[0],txt[1]))
    f.write("{} {}\n".format(txt[2],txt[3]))
    f.write("{} {}\n".format(txt[4],txt[5]))
    f.write("{}\n".format(txt[6]))
    f.write("{} {} {}\n".format(R1, R2, R3))
    f.write("{} {}\n".format(format(Decimal.from_float(x), '.21'),format(Decimal.from_float(y), '.21')))
    f.write("{} {}\n".format(a,b))
