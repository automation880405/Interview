List1 = [7,8,9,10,128,2,48]

def scndHigh(list1):
    return sorted(set(list(list1)))[-2]


print(scndHigh(List1))