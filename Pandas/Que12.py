import pandas as pd 
df = pd.read_csv("sample_data_files/student.csv")

print(df.groupby("Department")["Math"].mean())