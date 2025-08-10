text = "Avinash is a great guy"
s2 = text.replace(" ", "")
letter= s2.lower()


freq = {}

for x in letter:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

print(freq)