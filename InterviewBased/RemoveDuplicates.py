s = "Hello World"
text = s.lower()
seen = set()
unq = []

for x in text:
    if x.isalpha() and x not in seen:
        seen.add(x)
        unq.append(x)

print(unq)