# class Cylinder:
#     pi = 3.14

#     def __init__(self, radius = 1, height = 1):
#         self.radius = radius
#         self.height = height
    
#     def volume(self):
#         return Cylinder.pi*self.radius*self.radius*self.height

#     def surface_area(self):
#         return (2*Cylinder.pi*self.radius*self.height)+(2*Cylinder.pi*self.radius*self.radius)


# cylndr = Cylinder(3,2)

# print(cylndr.volume())

# print(cylndr.surface_area())


# class Line:

#     def __init__(self,coord1, coord2):
#         self.x1, self.y1 = coord1
#         self.x2, self.y2 = coord2

#     def slope(self):
#         return (self.y2-self.y1)/(self.x2-self.x1)
    
#     def distance(self):
#         return (((self.x2-self.x1)**2 + (self.y2-self.y1)**2))**(0.5)

# coordinate1 = (8,10)
# coordinate2 = (3,2)

# li = Line(coordinate1, coordinate2)

# print(li.distance())
# print(li.slope())



class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposite(self, dep_amt):
        self.balance += dep_amt
        print('Deposite Successful. Current balance is : ', self.balance)
    
    def withdraw(self, wd_amt):
        if wd_amt > self.balance:
            print("Funds Unavailable")
        else:
            self.balance -= wd_amt
            print("withdrawal Successful!. Current balance is : ", self.balance)
        
    def __str__(self) -> str:
        return f"Owner : {self.owner} \nBalance : {self.balance}"

udit = Account('Udit', 100)
print(udit)
print(udit.balance)
udit.deposite(50)
udit.withdraw(30)
udit.withdraw(121)
print(udit.owner)
print(udit.balance)