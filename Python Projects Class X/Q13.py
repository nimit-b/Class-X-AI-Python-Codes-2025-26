import numpy as np
import statistics as stat
a = input("Enter Numbers: ").split()
c = len(a)
L = []
for i in range(c):
    L.append(int(a[i]))
print("Mean: ",np.mean(L))
print("Median: ",np.median(L))
print("Mode: ",stat.mode(L))
