# class Sample():

#     def __init__(self):
#         print("Hello World!")


# my_class = Sample()

# my_class


# class Dog():

#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
    
#     def age_method(self):
#         print(self.age)

#     def name_method(self):
#         print(self.name)
    
#     def breed_method(self):
#         print(self.breed)

# my_dog_name = Dog('sammy', 9, 'husky').name_method()
# Dog('sammy', 9, 'husky').age_method()
# Dog('sammy', 9, 'husky').breed_method()


# class Circle:
#     pi = 3.14

#     def __init__(self, radius = 1):
#         self.radius = radius
#         self.area = radius*radius*self.pi
    
#     def set_radius(self, new_radius):
#         self.radius = new_radius
#         self.area = new_radius*new_radius*self.pi
    
#     def getCircumference(self):
#         return self.radius * self.pi * 2
    
# c= Circle()

# print('Radius is: ',c.radius)
# print('Area is: ',c.area)
# print('Circumference is: ',c.getCircumference())

# c.set_radius(2)
# print('Radius is: ',c.radius)
# print('Area is: ',c.area)
# print('Circumference is: ',c.getCircumference())


# class Animal:
#     def __init__(self):
#         print("Animal Created")

#     def WhoAmI(self):
#         print("Animal")

#     def eat(self):
#         print("Eating")

# c= Animal()
# c.eat()
# c.WhoAmI()

# class Dog(Animal):

#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog Created")
    
#     def WhoAmI(self):
#         print("Dog")
    
#     def bark(self):
#         print("woof")

# d = Dog()
# d.eat()
# d.WhoAmI()
# d.bark()



# class Cat:
#     def __init__(self,name):
#         self.name = name
    
#     def speak(self):
#         return(f"{self.name} says meow!")

# class Dog:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         return(f"{self.name} says woof!")

# meenki = Cat("dholi meenki")
# kutro = Dog("kalo tegdo")

# print(meenki.speak())
# print(kutro.speak())

# def pet_speak(pet):
#     print(pet.speak())

# pet_speak(meenki)
# pet_speak(kutro)



# class Animal:
#     def __init__(self,name):
#         self.name = name
    
#     def speak(self):
#         raise NotImplementedError("Subclass must implement abstract method")


# class Cat(Animal):
    
#     def speak(self):
#         return(f"{self.name} says meow!")

# class Dog(Animal):

#     def speak(self):
#         return(f"{self.name} says woof!")


# meenki = Cat("dholi meenki")
# kutro = Dog("kalo tegdo")
# jaanwar = Animal("Bhesya")

# print(meenki.speak())
# print(kutro.speak())
# print(jaanwar.speak())


# class Book:
#     def __init__(self, title, author, pages):
#         print("A book has been created.")
#         self.title = title
#         self.author = author
#         self.pages = pages
    
#     def __str__(self):
#         return "Title: %s, Author: %s, Pages: %s" %(self.title, self.author, self.pages)
    
#     def __len__(self):
#         return self.pages
    
#     def __del__(self):
#         print("A book has been deleted")

# b = Book("Python King!", "Udit Bhati", 189)

# print(b)
# print(len(b))
# del b


class Customer:

    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance
    
    def withdraw(self,amount):
        if amount > self.balance:
            raise RuntimeError("Not enough balance")
        self.balance -= amount
        return self.balance
    
    def deposit(self,amount):
        self.balance += amount
        return self.balance

udit = Customer("Udit", 100)

print(udit.deposit(200))

print(udit.withdraw(100))