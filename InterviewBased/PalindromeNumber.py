n = 343
copy = n
rev = 0
while n > 0:
    rem = n % 10
    rev = rev*10 + rem
    n = n//10


print(rev)

if rev == copy:
    print("Palindrome number")
else:
    print("Not Palindrome number")
    
# print("Palindrome number" if rev == copy else "Not Palindrome number")