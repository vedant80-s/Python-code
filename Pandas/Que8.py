import pandas as pd

df = pd.read_csv("sample_data_files/student.csv")

def get_grade(x):
    if x > 90: return 'A+'
    elif x > 75 : return 'A'
    elif x > 50 : return 'B'
    elif x > 33 : return 'C'
    else : return 'F'

df["Average"] = (df["Math"] + df["Science"] + df["English"]) // 3 
df.insert(9 , "Grade" , value=df["Average"].apply(get_grade))
print(df)