import pandas as pd

# Load your dataset
file_path = r'C:\Users\dsp96\Desktop\New folder\NewM_removedfile.csv'
df = pd.read_csv(file_path)

# Fill all missing values in 'BRate' with the median
median_value = df['BRate'].median()
df['BRate'] = df['BRate'].fillna(median_value)

# Reset the SlNo column
df = df.reset_index(drop=True)
df['SNo'] = df.index + 1

# Reorder columns to have SlNo first
cols = df.columns.tolist()
cols = ['SNo'] + [col for col in cols if col != 'SNo']
df = df[cols]

# Save the final dataset
df.to_csv(r'C:\Users\dsp96\Desktop\New folder\Filled_by_Median.csv', index=False)
print("✅ All missing values filled with Median and SlNo reset.")
