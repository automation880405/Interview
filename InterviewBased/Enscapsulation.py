class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

P = Person("Avinash")
print(P.get_name())

