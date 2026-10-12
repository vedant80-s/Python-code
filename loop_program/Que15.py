# Question 15
string = input("Enter String:- ")

count = 0
for char in string:
    if char in "aeiouAEIOU":
        count += 1

print("Count:-",count)