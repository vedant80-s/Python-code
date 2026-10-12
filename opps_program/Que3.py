# Question 3
# Question 1
class Car:
    def __init__(self, name , prize):
        self.name = name 
        self.prize = prize

    def get_name(self):
        return self.name

    def get_prize(self):
        return self.prize


car = Car('Maruti 800','67000')

print(car.name)
print(car.prize)