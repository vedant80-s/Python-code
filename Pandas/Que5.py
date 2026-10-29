import pandas as pd

df = pd.read_csv("sample_data_files/student.csv")

print(f"{"  ":50} ====Name====")
print(df["Name"])
print(f"{"  ":50} ====Math Marks====")
print(df["Math"])