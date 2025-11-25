a = input("String: ").lower()
c = 0
L = ['a','e','i','o','u']
for i in range(len(a)):
  for x in range(len(L)):
    if L[x] in a[i]:
       c += 1
print("Total Vowel in String: ",c)
