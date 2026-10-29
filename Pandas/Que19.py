import pandas as pd 

df = pd.read_csv("pandas/sample_data_files/student.csv")
df["Average"] = (df["Math"] + df["Science"] + df["English"]) / 3
total = df["Student_ID"].count()

print()
print("=== KPI 1 ===")
print("=== Total Student ===")
print(total)
print()


print()
print(" === KPI 2 ===")
print("=== Average Total Student Marks ===")
print(df["Average"].mean())
print()

print()
print(" === KPI 3 ===")
print("=== Highest Marks Student ===")
idx = df["Average"].idxmax()
print(df.loc[idx])
print()

print()
print("=== KPI 4 ===")
print("=== Pass Percentage ===")
count = (df["Average"] >= 33).sum()
print(count/total*100)
print()