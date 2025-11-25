a = input("Enter names(separated by comma): ")
b = a.split(',')
c = sorted(b)
for i in range(len(c)):
    print("Ordered: ",i+1,' ',c[i])


