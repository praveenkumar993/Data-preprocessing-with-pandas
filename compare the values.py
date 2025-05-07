import pandas as pd
import matplotlib.pyplot as plt

# Load both CSV files (replace with your filenames)
file1 = r'C:\Users\dsp96\Desktop\New folder\Normal_file_with_person_1.csv'
file2 = r'C:\Users\dsp96\Desktop\New folder\processed_with_person_1.csv'

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Show row and column counts (optional)
#print(f"File 1 → Rows: {len(df1)}, Columns: {df1.shape[1]}")
#print(f"File 2 → Rows: {len(df2)}, Columns: {df2.shape[1]}")

# Extract RSSI column
rssi1 = df1['RSSI']
rssi2 = df2['RSSI']

# Optional: Downsample if the data is very large (e.g., every 10th point)
step = 10
rssi1_down = rssi1[::step]
rssi2_down = rssi2[::step]

# Plot the RSSI values
plt.figure(figsize=(16, 6))  # Adjust figure size to your preference
plt.plot(rssi1_down.reset_index(drop=True), label='File 1 RSSI', color='#90ee90')
plt.plot(rssi2_down.reset_index(drop=True), label='File 2 RSSI', color='#ff9999')

# Labels and legend
plt.title('RSSI Comparison')
plt.xlabel('Sample Index (downsampled)')
plt.ylabel('RSSI')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show plot
plt.show()
