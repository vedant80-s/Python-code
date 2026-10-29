import pandas as pd

df = pd.read_csv("pandas/sample_data_files/student-null.csv")
numerical_col = df.select_dtypes("number")
numerical_col.interpolate(method="linear" , inplace=True)
df.to_csv("pandas/sample_data_files/student-clean-data.csv")