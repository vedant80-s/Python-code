import pandas as pd 

df1 = pd.read_csv("pandas/sample_data_files/student.csv")
df2 = pd.read_csv("pandas/sample_data_files/attendence.csv")

print(pd.merge(df1 , df2 , how="inner" , on="Student_ID")[["AttendancePercentage" , "Name"]])