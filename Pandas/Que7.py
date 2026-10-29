import pandas as pd 

df = pd.read_csv("sample_data_files/student.csv")

print(df.sort_values(['Math' , 'Science', 'English'] , ascending=False))