#file = open('C:/Users/avina/Desktop/Bio Data/Namaste.txt')


with open('C:/Users/avina/Desktop/Bio Data/Namaste.txt') as file:

        print(file.readline())
        content = file.read()
        print(content) # Read all the content in once
