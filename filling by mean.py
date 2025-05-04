import pandas as pd

# Load your dataset
file_path = r"C:\Users\dsp96\Desktop\New folder\Updated1_Merged_MD_old.csv"
df = pd.read_csv(file_path)

# Fill all missing values in 'BRate' with the median
mean_value = df['BRate'].mean()
df['BRate'] = df['BRate'].fillna(mean_value).round()

# Reset the SlNo column
df = df.reset_index(drop=True)
df['SNo'] = df.index + 1

# Reorder columns to have SlNo first
cols = df.columns.tolist()
cols = ['SNo'] + [col for col in cols if col != 'SNo']
df = df[cols]

# Save the final dataset
df.to_csv(r"C:\Users\dsp96\Desktop\New folder\Mean fill.csv", index=False)
print("✅ All missing values filled with Mean and SlNo reset.")
