"""Practical examples of the main object-oriented programming concepts."""


# Encapsulation: keep the balance private and control access through methods.
class BankAccount:
    def __init__(self, owner: str, opening_balance: float = 0.0) -> None:
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative.")
        self.owner = owner
        self.__balance = opening_balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount

    def get_balance(self) -> float:
        return self.__balance


# Basic inheritance: Car reuses and extends the behavior of Vehicle.
class Vehicle:
    def __init__(self, brand: str) -> None:
        self.brand = brand

    def start(self) -> str:
        return f"{self.brand} vehicle is starting."


class Car(Vehicle):
    def __init__(self, brand: str, doors: int = 4) -> None:
        super().__init__(brand)
        self.doors = doors

    def describe(self) -> str:
        return f"{self.brand} car with {self.doors} doors."


# Multiple inheritance: a SmartPhone gets independent capabilities from
# both Phone and Camera.
class Phone:
    def call(self, number: str) -> str:
        return f"Calling {number}..."


class Camera:
    def take_photo(self) -> str:
        return "Photo captured."


class SmartPhone(Phone, Camera):
    pass


# Multilevel inheritance: Dog inherits from Mammal, which inherits from Animal.
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def eat(self) -> str:
        return f"{self.name} is eating."


class Mammal(Animal):
    def nurse_young(self) -> str:
        return f"{self.name} nurses its young."


class Dog(Mammal):
    def fetch(self) -> str:
        return f"{self.name} fetches the ball."


# Hierarchical inheritance: multiple child classes share the same Shape parent.
class Shape:
    def area(self) -> float:
        raise NotImplementedError("Each shape must calculate its own area.")


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius**2


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


# Polymorphism and method overriding: each notification class provides its
# own implementation of send(), and callers can use them interchangeably.
class Notifier:
    def send(self, message: str) -> str:
        raise NotImplementedError("A notifier must implement send().")


class EmailNotifier(Notifier):
    def send(self, message: str) -> str:
        return f"Email sent: {message}"


class SMSNotifier(Notifier):
    def send(self, message: str) -> str:
        return f"SMS sent: {message}"


# Python does not support traditional method overloading. Default arguments
# let one method handle several common call shapes instead.
class Order:
    def summary(
        self,
        item: str = "general item",
        quantity: int = 1,
        delivery: str = "standard",
    ) -> str:
        return f"{quantity} x {item}; {delivery} delivery."


# Composition: the Car creates and owns its Engine as part of its setup.
class Engine:
    def start(self) -> str:
        return "Engine started."


class ComposedCar:
    def __init__(self, brand: str) -> None:
        self.brand = brand
        self.engine = Engine()

    def start(self) -> str:
        return f"{self.brand}: {self.engine.start()}"


# Aggregation: a Team uses Player objects supplied from outside. A player can
# also exist independently of the team that currently includes them.
class Player:
    def __init__(self, name: str) -> None:
        self.name = name


class Team:
    def __init__(self, name: str, players: list[Player]) -> None:
        self.name = name
        self.players = players

    def roster(self) -> str:
        return ", ".join(player.name for player in self.players)


def main() -> None:
    """Run each example and print its practical result."""
    print("ENCAPSULATION")
    account = BankAccount("Avery", 100.0)
    account.deposit(25.0)
    account.withdraw(10.0)
    print(f"{account.owner}'s balance: ${account.get_balance():.2f}")

    print("\nBASIC INHERITANCE")
    car = Car("Toyota")
    print(car.start())
    print(car.describe())

    print("\nMULTIPLE INHERITANCE")
    phone = SmartPhone()
    print(phone.call("555-0100"))
    print(phone.take_photo())

    print("\nMULTILEVEL INHERITANCE")
    dog = Dog("Rex")
    print(dog.eat())
    print(dog.nurse_young())
    print(dog.fetch())

    print("\nHIERARCHICAL INHERITANCE")
    for shape in (Circle(2), Rectangle(3, 4)):
        print(f"{type(shape).__name__} area: {shape.area():.2f}")

    print("\nPOLYMORPHISM AND METHOD OVERRIDING")
    notifiers: list[Notifier] = [EmailNotifier(), SMSNotifier()]
    for notifier in notifiers:
        print(notifier.send("Your order is ready."))

    print("\nDEFAULT-ARGUMENT METHOD OVERLOADING")
    order = Order()
    print(order.summary())
    print(order.summary("coffee", 2))
    print(order.summary("book", 1, "express"))

    print("\nCOMPOSITION")
    composed_car = ComposedCar("Honda")
    print(composed_car.start())

    print("\nAGGREGATION")
    players = [Player("Sam"), Player("Jordan")]
    team = Team("Tigers", players)
    print(f"{team.name} roster: {team.roster()}")


if __name__ == "__main__":
    main()
