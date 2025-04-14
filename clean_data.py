import pandas as pd
import numpy as np

# Read the Excel file into a DataFrame
df = pd.read_csv('data_set.csv')

# --- Handling Missing Values ---
# For numeric columns, fill missing values with the median
num_cols = df.select_dtypes(include=[np.number]).columns
df[num_cols] = df[num_cols].apply(lambda x: x.fillna(x.median()))

# For categorical columns, fill missing values with the mode (first mode value)
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    if df[col].isnull().sum() > 0:
        df[col].fillna(df[col].mode()[0], inplace=True)

# --- Removing Duplicates ---
df.drop_duplicates(inplace=True)

# --- Removing Outliers ---
# Using the IQR method on numeric columns:
def remove_outliers(data, col):
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return data[(data[col] >= lower_bound) & (data[col] <= upper_bound)]

# Apply the outlier removal for each numeric column iteratively
for col in num_cols:
    df = remove_outliers(df, col)

# Save the cleaned DataFrame to a new Excel file
df.to_csv('cleaned_dataset.csv', index=False)

print("Data cleaning completed successfully.")
