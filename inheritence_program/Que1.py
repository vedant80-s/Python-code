# Question 1
class Parent:
    def get_type(self):
        return "Parent"

class Child(Parent):
    def get_type(self):
        return "Child"


child = Child()
print(child.get_type())