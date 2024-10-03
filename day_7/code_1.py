# defining a class 

class Car:
    def __init__(self,color,model):
        self.color = color
        self.model = model 

    def start(self):
        print(f"The {self.color} {self.model} is starting.")

# Creating a object 

my_car = Car("Red","Honda")
my_car.start()

# -----------------------------------------------------------------------------------------

