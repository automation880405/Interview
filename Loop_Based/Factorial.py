#Write a program to find the factorial of a number using a loop.

def facto(number):
 fact=1
 if number==0 or number==1 :
     return 1
 for i in  range(1, number+1):
        fact= i*fact
 return fact
print(facto(0))