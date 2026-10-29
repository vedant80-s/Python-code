import pandas as pd 

df = pd.read_csv("pandas/sample_data_files/student.csv")

df.sort_values(by=["Math" , "Science" , "English"] , inplace=True)

print("\t\t\t\t\t\t\t ===Top 10 Student===")
print(df.tail(10))

print("\t\t\t\t\t\t\t ===Bottom 10 Student===")
print(df.head(10))
