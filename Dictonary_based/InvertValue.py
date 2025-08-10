dict1 = {'aman': 'billa', 'avinash': 'great', 'city1': 'begusarai', 'city2': 'Purnia'}

inverted = { values : keys for keys, values in dict1.items()}

print(inverted)