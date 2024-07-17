# HOMEWORK: Classes

# Basic Class
class HouseForSale:
    pass


# Create two instances
house1 = HouseForSale()
house2 = HouseForSale()

# Add instance attributes
house1.number_of_rooms = 3
house1.price = 250000
house2.number_of_rooms = 4
house2.price = 300000

# Print statements
print(f"House 1: {house1.number_of_rooms} rooms, ${house1.price}")
print(f"House 2: {house2.number_of_rooms} rooms, ${house2.price}")


# Instance Methods
class Computer:
    def turn_on(self):
        print("Computer has Turned On")

    def turn_off(self):
        print("Computer has Turned Off")


# Create an instance and call methods
my_computer = Computer()
my_computer.turn_on()
my_computer.turn_off()


# Constructor with Parameters
class Dog:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)


# Create an instance and call method
my_dog = Dog("Buddy")
my_dog.say_name()


# Inheritance
class Animal:
    def __init__(self, name=""):
        self.name = name

    def say_name(self):
        if self.name:
            print(self.name)
        else:
            print("I don't have a name yet.")

    def speak(self):
        print("I can't speak!")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Woof!")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Meow!")


# Create instances and test
animal = Animal()
animal.say_name()  # Prints: I don't have a name yet.
animal.speak()  # Prints: I can't speak!

dog = Dog('Fido')
dog.say_name()  # Prints: Fido
dog.speak()  # Prints: Woof!

cat = Cat('Max')
cat.say_name()  # Prints: Max
cat.speak()  # Prints: Meow!


# Exercise 1: Books and Authors
class Book:
    pass


book1 = Book()
book1.title = 'To Kill a Mockingbird'
book1.author = 'Harper Lee'
book1.publication_year = 1960

book2 = Book()
book2.title = '1984'
book2.author = 'George Orwell'
book2.publication_year = 1949

book3 = Book()
book3.title = 'Moby Dick'
book3.author = 'Herman Melville'
book3.publication_year = 1851

# Print statements
print(f"{book1.title} by {book1.author}, published in {book1.publication_year}")
print(f"{book2.title} by {book2.author}, published in {book2.publication_year}")
print(f"{book3.title} by {book3.author}, published in {book3.publication_year}")


# Exercise 2: Vehicle and Types of Vehicles
class Vehicle:
    def __init__(self, name, vehicle_type):
        self.name = name
        self.vehicle_type = vehicle_type

    def show_type(self):
        print(f"{self.name} is a {self.vehicle_type}")


class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name, "Car")


class Bike(Vehicle):
    def __init__(self, name):
        super().__init__(name, "Bike")


# Create instances and show types
car = Car("Toyota")
bike = Bike("Yamaha")

car.show_type()  # Prints: Toyota is a Car
bike.show_type()  # Prints: Yamaha is a Bike


# Exercise 3: Spot and Correct the Mistakes
class Car:
    def __init__(self, model, year):
        self.model = model  # Corrected: 'self.model = model'
        self.year = year  # Corrected: 'self.year = year'


my_car = Car("Toyota", 2021)  # Corrected: Added 'year' parameter
print(my_car.model)
print(my_car.year)


# Exercise 4: SmartHome with Constructor
class SmartHome:
    def __init__(self, home_name, location, number_of_devices):
        self.home_name = home_name
        self.location = location
        self.number_of_devices = number_of_devices

    def send_notification(self, message):
        print(f"Notification for {self.home_name} in {self.location}: {message}")


# Create instances
villa_rosa = SmartHome("Villa Rosa", "New York", 15)
green_house = SmartHome("Green House", "California", 10)
sea_view = SmartHome("Sea View", "Florida", 20)

# Send notifications
villa_rosa.send_notification("Please turn off the lights.")
green_house.send_notification("Please turn off the lights.")
sea_view.send_notification("Please turn off the lights.")


# Exercise 5: Inheritance. Spot and Correct Mistakes
class Animal:
    def __init__(self, name, age):
        self.name = name  # Corrected: 'self.name = name'
        self.age = age  # Corrected: 'self.age = age'


class Mammal(Animal):  # Corrected: Should inherit from 'Animal'
    def __init__(self, name, age, num_legs):
        super().__init__(name, age)
        self.num_legs = num_legs


class Bird(Animal):
    def __init__(self, name, age, can_fly):  # Corrected: Added 'name' and 'age' parameters
        super().__init__(name, age)  # Corrected: Call super().__init__(name, age)
        self.can_fly = can_fly


class Fish(Animal):  # Corrected: Should inherit from 'Animal'
    def __init__(self, name, age, num_fins):
        super().__init__(name, age)
        self.num_fins = num_fins


# Corrected: Create instances with the right parameters
tiger = Mammal('Tiger', 5, 4)
sparrow = Bird('Sparrow', 2, True)
goldfish = Fish('Goldfish', 1, 2)

print(f"{tiger.name}, {tiger.age} years old, {tiger.num_legs} legs")
print(f"{sparrow.name}, {sparrow.age} years old, can fly: {sparrow.can_fly}")
print(f"{goldfish.name}, {goldfish.age} years old, {goldfish.num_fins} fins")
