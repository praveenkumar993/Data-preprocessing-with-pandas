import pandas as pd

# Load your dataset
file_path = r"C:\Users\dsp96\Desktop\New folder\Updated1_Merged_MD_old.csv"
df = pd.read_csv(file_path)

# If the first row 'BRate' is missing, fill it with the median
if pd.isna(df['BRate'].iloc[0]):
    df.at[0, 'BRate'] = df['BRate'].median()

# Forward fill the remaining missing values
df['BRate'] = df['BRate'].fillna(method='ffill')

# Reset the SlNo column
df = df.reset_index(drop=True)
df['SNo'] = df.index + 1

# Reorder columns to keep SlNo first
cols = df.columns.tolist()
cols = ['SNo'] + [col for col in cols if col != 'SNo']
df = df[cols]

# Save the final dataset
df.to_csv(r"C:\Users\dsp96\Desktop\New folder\forward fill.csv", index=False)
print("its done")
