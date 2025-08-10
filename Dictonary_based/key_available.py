dict1 = {'a': 20, 'b': 30, 'c': 40, 'd':50, 'e':50}

for keys, values in dict1.items():
    if keys == 'b' :
      print(keys , values)



if 'c' in dict1:
    print('c', dict1['c'])