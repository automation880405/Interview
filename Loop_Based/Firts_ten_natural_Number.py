# Write a program to print the first 10 natural numbers using a loop.

#Using a for loop:

for i in range(1,11):
    print(i)

#Using list and range:
print(list(range(1, 11)))

#Using list comprehension:
numbers = [i for i in range(1, 11)]
print(numbers)