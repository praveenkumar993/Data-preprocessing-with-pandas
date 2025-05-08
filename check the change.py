import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the files
df_normal = pd.read_csv(r'C:\Users\dsp96\Desktop\New folder\Normal_file_with_person_1.csv')
df_processed = pd.read_csv(r'C:\Users\dsp96\Desktop\New folder\processed_with_person_1.csv')

# Ensure equal length
min_len = min(len(df_normal), len(df_processed))
df_normal = df_normal.iloc[:min_len].reset_index(drop=True)
df_processed = df_processed.iloc[:min_len].reset_index(drop=True)

# Parse timestamps
df_normal['Timestamp'] = pd.to_datetime(df_normal['Timestamp'])
df_processed['Timestamp'] = pd.to_datetime(df_processed['Timestamp'])

# Identify numeric columns to compare (drop SNo, Timestamp, RSSI)
compare_cols = [col for col in df_normal.columns if col not in ['SNo', 'Timestamp', 'RSSI']]

# Calculate feature-wise mean difference
mean_diff = (df_processed[compare_cols] - df_normal[compare_cols]).mean()
mean_diff_sorted = mean_diff.sort_values()

# ---------- 📈 Plot 1: Mean Differences per Feature ----------
plt.figure(figsize=(16, 6))
mean_diff_sorted.plot(kind='bar', color='teal')
plt.title("Mean Difference Between Processed and Normal by Feature")
plt.ylabel("Mean Difference")
plt.xlabel("Feature")
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.show()

# Show top 5 most changed features
print("🔍 Top 5 features with highest mean differences:")
print(mean_diff_sorted.tail(5))

# ---------- 📉 Plot 2: Total Difference per Timestamp ----------
# Compute row-wise total absolute difference
row_diffs = (df_processed[compare_cols] - df_normal[compare_cols]).abs().sum(axis=1)

plt.figure(figsize=(14, 4))
plt.plot(df_normal['Timestamp'], row_diffs, color='maroon')
plt.title("Total Difference Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Total Absolute Difference")
plt.grid(True)
plt.tight_layout()
plt.show()

# Identify timestamps with highest changes
threshold = row_diffs.max() * 0.95  # top 5% peak
peaks = df_normal['Timestamp'][row_diffs > threshold]
print("\n⏱️ Timestamps with major differences:")
print(peaks)
