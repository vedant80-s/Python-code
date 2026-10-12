# Question 7
string = "Kheer"

dict1 = {}

for i in string:
    dict1[i] = dict1.get(i,0) + 1 

print(dict1)