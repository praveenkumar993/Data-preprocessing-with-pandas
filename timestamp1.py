import pandas as pd

# Read the CSV file
df = pd.read_csv(r'C:\Users\dsp96\Desktop\New folder\True_03_12_11_24.csv')

# Extract the Timestamp column
timestamps = df['Timestamp']
print(len(timestamps))

# Convert 'Timestamp' to datetime format and remove milliseconds
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%d-%m-%Y %H:%M:%S:%f')

# Remove milliseconds and keep only hour, minute, and second
df['Timestamp'] = df['Timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')

# Save the formatted timestamps to a new file without the index column
df['Timestamp'].to_csv(r'C:\Users\dsp96\Desktop\New folder\Truedata_Timestamp.csv', index=False)

# Print a message to confirm
print("It's done")
