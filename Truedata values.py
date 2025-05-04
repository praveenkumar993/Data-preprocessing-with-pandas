import pandas as pd

file_path = r'C:\Users\dsp96\Desktop\New folder\3_palani_12-11-24_10-55am_10min_samDU-person-LOS-center-netgear_only-medical_ch-no-1_20mhz_sr-30.csv'

with open(file_path, 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

structured_data = []
for i in range(0, len(lines), 4):
    timestamp = lines[i]
    structured_data.append(timestamp)

columns = ['Timestamp']

df = pd.DataFrame(structured_data, columns=columns)
print(len(df))

# Convert 'Timestamp' to datetime format and remove milliseconds
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%d-%m-%Y %H:%M:%S.%f')  # Correct format

# Remove milliseconds and keep only hour, minute, and second
df['Timestamp'] = df['Timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')

# Save only the Timestamp values without the index column
df['Timestamp'].to_csv(r'C:\Users\dsp96\Desktop\New folder\Unstructured_timestamp.csv', index=False, header=True)

print("It's done")
