# Question 2
class Car:
    def __init__(self):
        self.model = "Car"
        self.speed = 180 
    def get_info(self):
        return f"Model:- {self.model} , Speed:- {self.speed}"

class Alto(Car):
    def get_info(self):
        return super().get_info()


alto = Alto()
print(alto.get_info())