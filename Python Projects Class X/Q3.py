d = True
while d == True:
   a = int(input("Number: "))
   c = 0
   for i in range(2,a//2 + 1):
       if a%i == 0:
           c += 1
           break
   if a == 2:
       print("Prime")
   elif c > 0 or a == 1:
       print("Not Prime")
   else:
       print("Prime")
   p = input("Want to Recheck[Yes/No]: ").upper()
   if 'Y' in p:
       d = True
   else:
       d = False
       print("Thanks For Using !")
