import pandas as pd 
df = pd.read_csv("sample_data_files/duplicate.csv")
print(df)
print(df.drop_duplicates())