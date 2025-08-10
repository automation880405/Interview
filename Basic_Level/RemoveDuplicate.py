s = "Programming"
seen = set()
output = ""

for char in s:
    if char not in seen:
        seen.add(char)
        output += char


print(output)

