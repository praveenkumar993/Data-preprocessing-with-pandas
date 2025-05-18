import pandas as pd

# Load the two files
df_brate = pd.read_csv(r'C:\Users\dsp96\Desktop\New folder\NewM_removedfile.csv')
df_rssi = pd.read_csv(r'C:\Users\dsp96\Desktop\New folder\NewM2_removedfile.csv')

# Merge the two DataFrames on the 'Timestamp' column
merged_df = pd.merge(df_brate, df_rssi, on='Timestamp', how='inner')
print(len(merged_df))
merged_df = merged_df[['Timestamp', 'BRate', 'Timestamp', 'RSSI']]


# Save the result to a new CSV file
merged_df.to_csv(r'C:\Users\dsp96\Desktop\New folder\NewM3_mergedfile.csv', index=False)

# Print a message to confirm
print("Merging complete. The output is saved.")
