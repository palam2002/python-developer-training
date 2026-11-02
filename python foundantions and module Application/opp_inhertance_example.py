#encapsulation:
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)

    def get_balance(self):
        return self.__balance

account = BankAccount("John Doe", 1000)
account.deposit(500)
print("Current Balance:", account.get_balance())  

#2single inheritance:
class animal:
    def eat(self):
        print("animal is eating")

class dog(animal):
    def walk(self):
        print("dog is walking")


dog = dog()
dog.eat()  
dog.walk()                

#3multiple inheritance:
class animal:
    def eat(self):
        print("animal is eating")

class elephant:
    def walk(self):
        print("elephant is walking")   

class hybrid(animal, elephant):
    pass



mobile = hybrid()
mobile.eat()    
mobile.walk()


#4mutilevel inheritance:
class person:
    def introduce(self):
        print("I am a man")

class employee(person):
    def work(self):
        print("i am working")    


class manager(employee):
    def manage(self):
        print("i am managing")



manager = manager()
manager.introduce()        
manager.work()
manager.manage()        


#5heirarchical inheritance:
#muttiple child classes are inheried from a single parent.
class vehicle:
    def start(self):
        print("vehicle is starting")


class car(vehicle):
    def drive(self):
        print("car is driving")

class bike(vehicle):
    def ride(self):
        print("bike is riding")     

car=car()
bike=bike()

car.start()
car.drive()
bike.start()
bike.ride()


#6 ploymorphism and method overriding:
#python supports fiexed arguments rather than 
#traditional method overloading by signature.

class shape:
    def area(self):
        print("area of the shape")



class rectangle(shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("area of the rectangle:", self.length * self.breadth)

class Square(shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print("area of the square:", self.side * self.side)

class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("area of the circle:", 3.14 * self.radius * self.radius)

shapes=[rectangle(5, 10), Square(4), Circle(3)]
for shape in shapes:
    shape.area()



#7Method overloading using default arguments

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c




calculator = Calculator()

print("one number:", calculator.add(5))
print("two numbers:", calculator.add(5, 10))
print("three numbers:", calculator.add(5, 10, 15))

#8composition:
#a car create and ownws its engine object,
#the engine create inside the car.


class Engine:
    def start(self):
        print("Engine is starting")


class compositionCar:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car is starting")



composition_car = compositionCar()
composition_car.start_car()       


#9aggregation:

class officeemployee:
    def __init__(self, name):
        self.name = name

class department:
    def __init__(self, employee):
        self.employee = employee


    def show_employee(self):
        print("Employee Name:", self.employee.name)


employee = officeemployee("John Doe")
department = department(employee)
department.show_employee()


print("All oop concepts are implemented successfully")

