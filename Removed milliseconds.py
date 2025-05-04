import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Users\dsp96\Desktop\New folder\True_03_12_11_24.csv')

# Manually convert the 'Timestamp' column to datetime with the correct format
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%d-%m-%Y %H:%M:%S:%f')

# Remove milliseconds and keep only hour, minute, and second
df['Timestamp'] = df['Timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')
df = df.drop_duplicates(subset='Timestamp')
df = df[['Timestamp', 'BRate']]
print(len(df))


# Save the updated dataset to a new CSV file (you can overwrite the original or save as new)
df.to_csv(r"C:\Users\dsp96\Desktop\New folder\New4_removedfile.csv", index=False)

# Print the first few rows to verify the changeṣ
print("its over")