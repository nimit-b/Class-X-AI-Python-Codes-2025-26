L = [1,2,3,4,5,6,7,8,9,10]
Q = []
for n in L:
    if n%2 != 0:
        Q.append(n)
print("Sum of Odd Numbers: ",sum(Q))
