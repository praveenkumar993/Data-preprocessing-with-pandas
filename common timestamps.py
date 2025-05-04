import pandas as pd

# Read both CSV files containing the Timestamp column
df1 = pd.read_csv(r'C:\Users\dsp96\Desktop\New folder\Truedata_Timestamp.csv')
df2 = pd.read_csv(r'C:\Users\dsp96\Desktop\New folder\Unstructured_timestamp.csv')

# Assuming the Timestamp column in both files is named 'Timestamp'
# If the columns are named differently, replace 'Timestamp' with the correct name
timestamps1 = set(df1['Timestamp'])
timestamps2 = set(df2['Timestamp'])

# Find the intersection (common timestamps) between the two sets
common_timestamps = list(timestamps1.intersection(timestamps2))

# Create a new DataFrame with the common timestamps
df_common = pd.DataFrame(common_timestamps, columns=['Timestamp'])
print(len(df_common))
# Save the common timestamps to a new file
df_common.to_csv(r'C:\Users\dsp96\Desktop\New folder\common_timestamps.csv', index=False)

print("Matching timestamps saved to 'common_timestamps.csv'")
