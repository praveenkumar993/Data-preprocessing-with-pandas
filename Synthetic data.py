import pandas as pd
import numpy as np

# Load the original dataset
df = pd.read_csv(r'C:\Users\dsp96\Desktop\New folder\Normal_file_with_person_1.csv')

# Number of synthetic rows to generate (this will be equal to the original data length)
n_rows = len(df)

# Select only numeric columns, excluding 'Timestamp' and 'SNo'
numeric_columns = df.select_dtypes(include=np.number).columns.difference(['SNo', 'Timestamp'])

# Extract statistical properties (mean and std) for numeric columns
means = df[numeric_columns].mean()
stds = df[numeric_columns].std()

# Generate synthetic data for numeric columns
synthetic_data = np.random.normal(loc=means, scale=stds, size=(n_rows, len(numeric_columns)))
synthetic_df = pd.DataFrame(synthetic_data, columns=numeric_columns)

# Use the 'Timestamp' and 'SNo' from the original dataset
synthetic_df['Timestamp'] = df['Timestamp']
synthetic_df['SNo'] = df['SNo']

# Reorder columns to ensure 'SNo' is the first column and 'Timestamp' second
column_order = ['SNo', 'Timestamp'] + [col for col in numeric_columns]
synthetic_df = synthetic_df[column_order]

# Save to CSV
synthetic_df.to_csv(r'C:\Users\dsp96\Desktop\New folder\synthetic_data_from_normal_file.csv', index=False)

print("✅ Synthetic data generated with original timestamps and SNo, saved as 'synthetic_data_with_same_timestamps_and_SNo.csv'")
