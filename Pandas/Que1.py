import pandas as pd


data = {
    "Name":["Raj","Rahul","Tony","Hitesh","Ved","Vipul","Deeraj","Sachin","Ramesh","Virupaksha"],
    "Age":[20,19,18,19,21,20,17,18,15,18],
    "Marks":[45,56,34,48,89,67,59,78,67,50]
}


df = pd.DataFrame(data)

print(df)