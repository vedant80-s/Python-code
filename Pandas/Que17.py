import pandas as pd 

monthly_sales = pd.read_csv("pandas/sample_data_files/monthly_sales.csv")

monthly_sales["Date"] = pd.to_datetime(monthly_sales["Date"])
monthly_sales["Month"] = monthly_sales["Date"].dt.to_period('M')
print(monthly_sales.groupby(("Month"))[["Quantity" , "Revenue"]].sum())