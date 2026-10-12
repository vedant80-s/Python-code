# Question 6
# Question 3
dict1 = {"Ryan":23,
         "Trent":34,
         "Foy":45,
         "Mitchel":57}

# Normal
for k in dict1:
    print(f"Key:- {k} and Value:- {dict1.get(k)}")


# Using Enumerate (it is not Working properly)

for i , (k , v) in enumerate(dict1.items()):
    print(f"Key:- {k} and Value:- {v}")
