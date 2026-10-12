# Question 4
class Animal:
    def __init__(self):
        self.type = None 

    def get_type(self):
        return self.type

class Sound:
    def __init__(self):
        self.sound = None 

    def get_sound(self):
        return self.sound


class Dog(Animal , Sound):
    def __init__(self):
        Animal.__init__(self) # ye yaha self kyo lagaya jabki normal super. me toh self nahi lagta hai ? 
        Sound.__init__(self)
        self.type = "Gharelu"
        self.sound = "Bhao Bhao"

    def get_type(self):
        return self.type

    def get_sound(self):
        return self.sound


dog = Dog()
print(dog.get_type())
print(dog.get_sound())