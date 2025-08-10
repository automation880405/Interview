text = "Python is a great as Python hello is Python"

chars = text.lower()   # Convert to lowercase to count uniformly

freq = {}

for char in chars:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)
