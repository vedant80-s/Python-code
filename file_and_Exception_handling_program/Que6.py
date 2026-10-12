# Question 6
a = int(input("Enter A number 1:- "))
b = int(input("Enter A number 2:- "))

try:
    div = a//b
    print("Res:-",div)
except ZeroDivisionError as ze:
    print("Exception :- " , ze.args)
finally:
    print("Finally")