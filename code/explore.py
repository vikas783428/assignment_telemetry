import pandas as pd

# Load the dataset
df = pd.read_csv("data/network_telemetry.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Display dataset shape
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumns:")
print(df.columns)

# Display data types
print("\nData Types:")
print(df.dtypes)

# Display basic statistics
print("\nSummary Statistics:")
print(df.describe())

# Display fault counts
print("\nFault Counts:")
print(df["fault"].value_counts())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())