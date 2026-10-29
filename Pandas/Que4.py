import pandas as pd

df = pd.read_csv("sample_data_files/student.csv")

print(f"{"  ":50} ============Head===========\n")
print(df.head())
print(f"{"  ":50} ============Tail===========\n")
print(df.tail())
print(f"{"  ":50} ============Info===========\n")
print(df.info())
print(f"{"  ":50} ===========Shape============")
print(df.shape)