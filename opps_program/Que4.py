# Question 4
# Question 1
class Car:
    def __init__(self, name , prize):
        self.__name = name 
        self.__prize = prize

    def get_name(self):
        return self.__name

    def get_prize(self):
        return self.__prize


car = Car('Maruti 800','67000')

print(car.get_name())
print(car.get_prize())