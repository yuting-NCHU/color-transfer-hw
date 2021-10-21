import random
import csv
import numpy as np

with open("input09.txt") as f:
    txt = f.read().split()

# print(txt) #x0 r M Seed
x = float(txt[0])
r = float(txt[1])
M = int(txt[2])
Seed = int(txt[3])
random.seed(Seed)

val=[]
for i in range(M):
    x = r*x*(1-x)
    val.append([i+1, round(x,6), random.random()])

arr = np.array(val)
mean = np.round(np.mean(arr, axis = 0),6)
std = np.round(np.std(arr, axis = 0),6)
mean = ["mean", mean[1],mean[2]]
std = ["std", std[1],std[2]]

with open("output09.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["x0", "r", "N", "seed"])
    writer.writerow(txt)
    writer.writerows(val)
    writer.writerow(mean)
    writer.writerow(std)