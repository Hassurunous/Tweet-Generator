

# # Make School OOP Coding Challenge Python Problem 2
#
# import sys
#
#
# # A Tiger's favorite food is meat
# favoriteFood = "meat"
#
#
# # Copy your sleep function here
# def sleep(name):
#     print(name + " sleeps for 8 hours")
#
#
# # Implement the eat function here
# def eat(name, food):
#     print(name + " eats " + food)
#     if food == favoriteFood:
#         print("YUM! " + name + " wants more " + food)
#
#
# # Implement the Tiger class and its initializer, sleep and eat methods here
# class Tiger(object):
#     # Implement the initializer method here
#     def __init__(self, name):
#         self.name = name
#         self.favoriteFood = "meat"
#
#     # Copy your sleep function here and modify it to work as a method
#     def sleep(self):
#         print(self.name + " sleeps for 8 hours")
#
#     # Copy your eat function here and modify it to work as a method
#     def eat(self, food):
#         print(self.name + " eats " + food)
#         if food == self.favoriteFood:
#             print("YUM! " + self.name + " wants more " + food)
#
#
# # Implement the Bear class and its initializer, sleep and eat methods here
# class Bear(object):
#     # Implement the initializer method here
#     def __init__(self, name):
#         self.name = name
#         self.favoriteFood = "fish"
#
#     # Copy your sleep function here and modify it to work as a method
#     def sleep(self):
#         print(self.name + " hibernates for 4 months")
#
#     # Copy your eat function here and modify it to work as a method
#     def eat(self, food):
#         print(self.name + " eats " + food)
#         if food == self.favoriteFood:
#             print("YUM! " + self.name + " wants more " + food)


# # Implement the Animal superclass here
# # Hint: Copy your Tiger class from Problem 4 and modify it to be more general
# class Animal(object):
#     # Implement the initializer method here
#     def __init__(self, name, favoriteFood):
#         self.name = name
#         self.favoriteFood = favoriteFood
#
#     # Copy your sleep function here and modify it to work as a method
#     def sleep(self):
#         print(self.name + " sleeps for 8 hours")
#
#     # Copy your eat function here and modify it to work as a method
#     def eat(self, food):
#         print(self.name + " eats " + food)
#         if food == self.favoriteFood:
#             print("YUM! " + self.name + " wants more " + food)
#
#
# # Implement the Tiger class here as a subclass of Animal
# # Hint: Implement the initializer method only
# class Tiger(Animal):
#     def __init__(self, name):
#         self.favoriteFood = "meat"
#         self.name = name
#
#
# # Implement the Bear class here as a subclass of Animal
# # Hint: Implement the initializer method and override the sleep method
# class Bear(Animal):
#     def __init__(self, name):
#         self.favoriteFood = "fish"
#         self.name = name
#
#     def sleep(self):
#         print(self.name + " hibernates for 4 months")


# # Copy your Animal class here
# class Animal(object):
#     # Implement the initializer method here
#     def __init__(self, name, favoriteFood):
#         self.name = name
#         self.favoriteFood = favoriteFood
#
#     # Copy your sleep function here and modify it to work as a method
#     def sleep(self):
#         print(self.name + " sleeps for 8 hours")
#
#     # Copy your eat function here and modify it to work as a method
#     def eat(self, food):
#         print(self.name + " eats " + food)
#         if food == self.favoriteFood:
#             print("YUM! " + self.name + " wants more " + food)
#
#
# # Copy your Tiger class here
# class Tiger(Animal):
#     def __init__(self, name):
#         self.favoriteFood = "meat"
#         self.name = name
#
#
# # Copy your Bear class here
# class Bear(Animal):
#     def __init__(self, name):
#         self.favoriteFood = "fish"
#         self.name = name
#
#     def sleep(self):
#         print(self.name + " hibernates for 4 months")
#
#
# # Implement the Unicorn class here as a subclass of Animal
# # Hint: Implement the initializer method and override the sleep method
# class Unicorn(Animal):
#     def __init__(self, name):
#         self.favoriteFood = "marshmallows"
#         self.name = name
#
#     def sleep(self):
#         print(self.name + " sleeps in a cloud")
#
#
# # Implement the Giraffe class here as a subclass of Animal
# # Hint: Implement the initializer method and override the eat method
# class Giraffe(Animal):
#     def __init__(self, name):
#         self.favoriteFood = "leaves"
#         self.name = name
#
#     def eat(self, food):
#         print(self.name + " eats " + food)
#         if food == self.favoriteFood:
#             print("YUM! " + self.name + " wants more " + food)
#         else:
#             print("YUCK! " + self.name + " spits out " + food)
#
#
# # Implement the Bee class here as a subclass of Animal
# # Hint: Implement the initializer method and override the sleep and eat methods
# class Bee(Animal):
#     def __init__(self, name):
#         self.favoriteFood = "pollen"
#         self.name = name
#
#     def sleep(self):
#         print(self.name + " never sleeps")
#
#     def eat(self, food):
#         print(self.name + " eats " + food)
#         if food == self.favoriteFood:
#             print("YUM! " + self.name + " wants more " + food)
#         else:
#             print("YUCK! " + self.name + " spits out " + food)


# Copy your Animal class here
class Animal(object):
    # Implement the initializer method here
    def __init__(self, name, favoriteFood):
        self.name = name
        self.favoriteFood = favoriteFood

    # Copy your sleep function here and modify it to work as a method
    def sleep(self):
        print(self.name + " sleeps for 8 hours")

    # Copy your eat function here and modify it to work as a method
    def eat(self, food):
        print(self.name + " eats " + food)
        if food == self.favoriteFood:
            print("YUM! " + self.name + " wants more " + food)


# Copy your Tiger class here
class Tiger(Animal):
    def __init__(self, name):
        self.favoriteFood = "meat"
        self.name = name


# Copy your Bear class here
class Bear(Animal):
    def __init__(self, name):
        self.favoriteFood = "fish"
        self.name = name

    def sleep(self):
        print(self.name + " hibernates for 4 months")


# Implement the Unicorn class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep method
class Unicorn(Animal):
    def __init__(self, name):
        self.favoriteFood = "marshmallows"
        self.name = name

    def sleep(self):
        print(self.name + " sleeps in a cloud")


# Implement the Giraffe class here as a subclass of Animal
# Hint: Implement the initializer method and override the eat method
class Giraffe(Animal):
    def __init__(self, name):
        self.favoriteFood = "leaves"
        self.name = name

    def eat(self, food):
        print(self.name + " eats " + food)
        if food == self.favoriteFood:
            print("YUM! " + self.name + " wants more " + food)
        else:
            print("YUCK! " + self.name + " spits out " + food)


# Implement the Bee class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep and eat methods
class Bee(Animal):
    def __init__(self, name):
        self.favoriteFood = "pollen"
        self.name = name

    def sleep(self):
        print(self.name + " never sleeps")

    def eat(self, food):
        print(self.name + " eats " + food)
        if food == self.favoriteFood:
            print("YUM! " + self.name + " wants more " + food)
        else:
            print("YUCK! " + self.name + " spits out " + food)


# Implement the Zookeeper class here
class Zookeeper(object):
    # Implement the initializer method here
    def __init__(self, name):
        self.name = name

    # Implement the feedAnimals method here
    def feedAnimals(self, animals, food):
        print(self.name, "is feeding", food, "to",  len(animals), "animals")
        for animal in animals:
            animal.eat(food)
            animal.sleep()
