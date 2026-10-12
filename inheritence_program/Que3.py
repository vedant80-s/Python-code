# Question 3
class Car:
    def __init__(self):
        self.model = "Car"
        self.speed = 180 
    def get_info(self):
        return f"Model:- {self.model} , Speed:- {self.speed}"

class Alto(Car):

    def __init__(self):
        super().__init__()
        self.model = "Alto"
        self.speed = 90

    def get_info(self):
        return f"Model:- {self.model} , Speed {self.speed}"


alto = Alto()
print(alto.get_info())