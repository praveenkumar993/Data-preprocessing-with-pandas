import pandas as pd

file_path = r'C:\Users\dsp96\Desktop\New folder\3_palani_12-11-24_10-55am_10min_samDU-person-LOS-center-netgear_only-medical_ch-no-1_20mhz_sr-30.csv'

# Read and clean lines from the file
with open(file_path, 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

structured_data = []
amplitude_lengths = []
phase_lengths = []

# First pass: collect max lengths for padding
for i in range(0, len(lines), 4):
    amplitude_list = eval(lines[i + 1])
    phase_list = eval(lines[i + 2])
    amplitude_lengths.append(len(amplitude_list))
    phase_lengths.append(len(phase_list))

max_amplitudes = max(amplitude_lengths)
max_phases = max(phase_lengths)

# Second pass: build structured rows
for i in range(0, len(lines), 4):
    timestamp = lines[i]
    amplitude_list = eval(lines[i + 1])
    phase_list = eval(lines[i + 2])
    rssi = lines[i + 3]

    # Pad amplitude and phase with NaNs to match max length
    amplitude_list += [float('nan')] * (max_amplitudes - len(amplitude_list))
    phase_list += [float('nan')] * (max_phases - len(phase_list))

    row = [timestamp] + amplitude_list + phase_list + [rssi]
    structured_data.append(row)

# Define column headers
columns = (
    ['Timestamp'] +
    [f'Amplitude_{i+1}' for i in range(max_amplitudes)] +
    [f'Phase_{i+1}' for i in range(max_phases)] +
    ['RSSI']
)

# Create DataFrame
df = pd.DataFrame(structured_data, columns=columns)
df.insert(0, 'SNo', range(1, len(df) + 1))

# Convert and format Timestamp: remove milliseconds
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%d-%m-%Y %H:%M:%S.%f', errors='coerce')
df['Timestamp'] = df['Timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')

# Save to CSV
output_path = r'C:\Users\dsp96\Desktop\New folder\structured_output.csv'
df.to_csv(output_path, index=False)

print("Structured data saved to:")
