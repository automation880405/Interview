class A:
    def get_A(self):
        print("This is A")
    def get_B(self):
        print("A")

class B:
    def get_B(self):
        print("B")

class C:
    def get_B(self):
        print("C")

class D(B,A,C):                                #due to MRO
    def get_C(self):
       print("D")


d = D()
d.get_B()


