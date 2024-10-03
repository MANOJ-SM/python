# defining a class 

# class Car:
#     def __init__(self,color,model):
#         self.color = color
#         self.model = model 

#     def start(self):
#         print(f"The {self.color} {self.model} is starting.")

# Creating a object 

# my_car = Car("Red","Honda")
# my_car.start()

# -----------------------------------------------------------------------------------------

# encapsulation 

# class BankAccount :
#     def __init__(self,balance):
#         self._balance = balance  #private variable 

#     def deposit(self,amount):
#         self._balance += amount

#     def get_balance(self):
#         return self._balance


# creating an object 

# account = BankAccount(2000)
# account.deposit(300)
# print(account.get_balance())

#--------------------------------------------------------------------

# Inheritence -->  inherit , code reuse , hireachy 

# parent Class 
         
# class Animal:
#     def speak(self):
#         print("Animal is making a sound")

# Chil class

# class Dog(Animal):
#     def speak(self):
#         print("Dog is barking")

# Creating an object of the child class 

# my_dog = Dog()
# my_dog.speak()

#--------------------------------------------------------------------------------

# polymorphism 

class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")            
        

# polymorphism in action 

def make_it_fly (flying_object):
    flying_object.fly()


# Creating Objects 

sparrow = Bird()
boeing = Airplane()

make_it_fly(sparrow)
make_it_fly(boeing)

