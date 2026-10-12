num1 = int(input("Enter Number:- "))
num2 = int(input("Enter Number:- "))
num3 = int(input("Enter Number:- "))

greater = num1 if num1 > num2 else num2
greater = greater if greater > num3 else num3
print(f"Greater {greater}")