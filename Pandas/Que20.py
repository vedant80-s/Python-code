
import pandas as pd

# 1. Read Data
file_path = "pandas/sample_data_files/student-null.csv"
df = pd.read_csv(file_path)

print("=" * 60)
print("             STUDENT DATA ANALYZER")
print("=" * 60)

print("\n--- Original Data ---")
print(df.head())

print("\nDataset Shape:", df.shape)
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# 2. Clean Data
numeric_cols = df.select_dtypes(include="number").columns

# Fill missing numeric values using linear interpolation
if df[numeric_cols].isnull().any().any():
    df[numeric_cols] = df[numeric_cols].interpolate(
        method="linear",
        limit_direction="both"
    )

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# 3. Analysis
numeric_df = df[numeric_cols]

print("\n" + "=" * 60)
print("                  DATA ANALYSIS")
print("=" * 60)

print("\n--- Mean ---")
print(numeric_df.mean().round(2))

print("\n--- Maximum ---")
print(numeric_df.max())

print("\n--- Minimum ---")
print(numeric_df.min())

print("\n--- Count ---")
print(numeric_df.count())

print("\n--- Summary Statistics ---")
print(numeric_df.describe().round(2))

# 4. Export Cleaned Data
output_path = "pandas/sample_data_files/cleaned_students.csv"
df.to_csv(output_path, index=False)

print(f"\nCleaned data exported to: {output_path}")