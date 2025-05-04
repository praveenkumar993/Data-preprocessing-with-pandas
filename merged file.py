import pandas as pd

# Replace these with your actual file names
file1 = "C:\Users\dsp96\Downloads\True_2_11_03_25_MD_old.csv"
file2 = "C:\Users\dsp96\Downloads\True_1_11_03_25_MD_old.csv"
output_file = 'merged_MD_old.csv'

# Load both files
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Merge the two DataFrames
merged_df = pd.concat([df1, df2], ignore_index=True)

# Save the merged result to a new CSV file
merged_df.to_csv(output_file, index=False)

print(f"✅ Files merged successfully into: {output_file}")
