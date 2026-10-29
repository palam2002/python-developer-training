#1.__repr__
#2.__len__

class A:
    def __repr__(self):
        return "hello python"


    def __len__(self):
        return 6


a=A()
print(repr(a))
print(len(a))   


#2 __eq__,__it__,__gt__

class number:
    def __init__(self, value):
        self.value = value



    def __eq__(self, other):
        return self.value == other.value


    def __lt__(self, other):
        return self.value < other.value


    def __gt__(self, other):
        return self.value > other.value


a=number(10)
b=number(20)

print(a==b)
print(a<b)
print(a>b)


#3.__add__,__sub__,
class calc:
    def __init__(self,x):
        self.x=x



    def __add__(self, other):
        return self.x + other.x



    def __sub__(self, other):
        return self.x - other.x




a=calc(10)
b=calc(5)

print(a+b)
print(a-b)


