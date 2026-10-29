import pandas as pd 

df = pd.read_csv("sample_data_files/student.csv")
print("\n===Count===\n",df.count(numeric_only=True))
print("\n===Mean===\n",df.mean(numeric_only=True))
print("\n===Max===\n",df.max(numeric_only=True))
print("\n===Min===\n",df.min(numeric_only=True))