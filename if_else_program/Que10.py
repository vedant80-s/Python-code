num1 = int(input("Enter Number 1:- "))
num2 = int(input("Enter Number 2:- "))

print("Enter + for + ")
print("Enter - for - ")
print("Enter / for / ")
print("Enter * for * ")

char = input("Enter your choice:- ")



# if elif else 
if char == '+':
    print("Sum:-", num1 + num2)

elif char == '-':
    print("Subtraction:-", num1 - num2)

elif char == '*':
    print("Multiplication:-", num1 * num2)

elif char == '/':
    print("Division:-", num1 / num2)

else:
    print("Please enter a valid operator")



# MAtch case Example 
# match char[0]:
#     case '+':
#         print("Sum:- " ,(num1+num2))
#     case '-':
#         print("Subtraction:- " ,(num1 - num2))
#     case '/':
#         print("Divison:- " ,(num1 // num2))
#     case '*':
#         print("Multiplication:- " ,(num1*num2))
#     case _:
#         print("please enter a valid operator")