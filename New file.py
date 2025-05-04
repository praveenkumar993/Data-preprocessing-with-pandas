import pandas as pd

# Load the two CSV files
file1 = "C:/Users/dsp96/Downloads/True_2_11_03_25_MD_old.csv"
file2 = "C:/Users/dsp96/Downloads/True_1_11_03_25_MD_old.csv"
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Merge the two DataFrames
merged_df = pd.concat([df2, df1], ignore_index=True)

# Save the merged DataFrame to a new CSV file
output_file = "C:/Users/dsp96/Desktop/New folder\Merged_MD_old.csv"
merged_df.to_csv(output_file, index=False)

print(f'Merged file done')
