#1 student class:
class student:
    def __init__(self, name, markes):
        self.name = name
        self.markes = markes

    def disply(self):
        print("Student:", self.name, "Marks:", self.markes)

s1 = student("ravi", 65)
s1.disply()           


#2bank account class:


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful")
        else:
            print("Invalid deposit")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Invalid withdrawal")

    def show_balance(self):
        print("Balance:", self.balance)


# Create an object
account = BankAccount(1000)

account.show_balance()
account.deposit(500)
account.show_balance()
account.withdraw(200)
account.show_balance()
account.withdraw(2000)


#3 employee management:

class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("employee:",self.name,"salary:",self.salary)                

s1=employee("teja",25000)
s1.display()


#4vihicle interitance


class Vehicle:
    def start(self):
        print("Start the car")


class Car(Vehicle):
    def drive(self):
        print("driving car")

c1 = Car()

c1.start() 
c1.drive()
       

#5 shape area calc:

class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length   * self.width

class circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius **3


r=rectangle(20,5)
c=circle(3)


print("rectabgle area:",r.area)
print("area of circle:",c.area)


#6 shopping cart:


class ShoppingCart:
    def __init__(self):
        self.item = []

    def add_item(self, item, price):
        if price > 0:
            self.item.append((item, price))
        else:
            print("Invalid price")

    def show_item(self):
        for item, price in self.item:
            print(item, ":", price)

        total = sum(price for item, price in self.item)
        print("Cart total:", total)

c1 = ShoppingCart()

c1.add_item("ice cream", 234)
c1.show_item()


#7 movie rating systems


class Movie:
    def __init__(self, title):
        self.title = title
        self.ratings = []

    def average_rating(self):
        if not self.ratings:
            return 0

        return sum(self.ratings) / len(self.ratings)


# Create an object
m1 = Movie("RRR")

# Add ratings
m1.ratings.append(8)
m1.ratings.append(9)
m1.ratings.append(10)

print("Movie:", m1.title)
print("Average rating:", m1.average_rating())



#8 hostipal patient records:


class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)


s = Patient(101, "malli")
s.display()
           
#9school result processing:

class result:
    def __init__(self,name,markes):
        self.name = name
        self.markes = markes

    def total(self):
        return sum(self.markes)


    def avg(self):
        return self.total() / len(self.markes)


    def dispaly(self):
        print("name:",self.name)
        print("total",self.total())
        print("avg:",self.avg())


d1=result("ravi",[23,45,87])
d1.dispaly()


#10 online course management:

class course:
    def __init__(self,name,fee):
        self.name = name
        self.fee = fee


    def display(self):
        print("corse:",self.name) 
        print("fee:",self.fee)

a1=course("python",6000)
a1.display()




