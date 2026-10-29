import pandas as pd

df = pd.read_csv("sample_data_files/student-null.csv")

print(df.fillna(df.mean(numeric_only=True)))