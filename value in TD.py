import pandas as pd

# Load the two files
df_brate = pd.read_csv(r'C:\Users\dsp96\Desktop\New folder\NewM_removedfile.csv')  # File containing Timestamp and brate
df_rssi = pd.read_csv(r'C:\Users\dsp96\Desktop\New folder\structured_output.csv')  # File containing Timestamp and rssi

# Merge the two DataFrames on 'Timestamp' column, keeping all timestamps
merged_df = pd.merge(df_brate, df_rssi, on='Timestamp', how='outer')

# Remove duplicates based on the 'Timestamp' column
merged_df = merged_df.drop_duplicates(subset='Timestamp')

# Extract only the 'Timestamp' and 'brate' columns
final_df = merged_df[['Timestamp', 'brate']]
print(len(final_df))

# Save the result to a new CSV file
output_path = r'C:\Users\dsp96\Desktop\New folder\Value_added_to_TD.csv'
final_df.to_csv(output_path, index=False)

# Print a message to confirm
print("Merging complete. The output is saved.")
