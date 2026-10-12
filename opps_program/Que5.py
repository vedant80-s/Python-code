# Question 5
class Student:

    def __init__(self , name , cls , sub) -> None:
        self.name = name
        self.cls = cls
        self.sub =sub

    def set_sub(self , sub) -> None:
        self.sub = sub 
    def set_name(self , name) -> None:
        self.name = name
    def set_cls(self , cls) -> None:
        self.cls = cls

    def get_sub(self):
        return self.sub
    def get_cls(self):
        return self.cls
    def get_name(self):
        return self.name

student = Student(name='Rahul' , cls = '8th' , sub = 'Maths')
print(student.get_name())
print(student.get_cls())
print(student.get_sub())