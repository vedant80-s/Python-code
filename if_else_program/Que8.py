marks = int(input("Enter Your Marks:- "))

if marks >= 30 and marks < 50:
    print("Grade C")
elif marks >= 50 and marks < 70:
    print("Grade B")
elif marks >= 70 and marks < 90:
    print("Grade A")
elif marks >= 90 and marks < 100:
    print("Grade A+")
else:
    print("Grade F")