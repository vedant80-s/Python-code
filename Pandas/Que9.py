import pandas as pd

df = pd.read_csv("sample_data_files/student.csv")

df.rename(columns={"Final_Exam" : "F_Exam"})
print(df)