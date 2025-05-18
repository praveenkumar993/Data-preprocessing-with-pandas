import pandas as pd

# Load your dataset
file_path = r"C:\Users\dsp96\Desktop\New folder\Merged_MD_old.csv"
df = pd.read_csv(file_path)

# Convert 'Timestamp' to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%d-%m-%Y %H:%M:%S:%f')

# Remove milliseconds
df['Timestamp'] = df['Timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')

# Find which Timestamps are duplicated
dup_counts = df['Timestamp'].value_counts()

# Split into two parts:
# 1. Non-duplicates (value count = 1)
non_dupes = df[df['Timestamp'].isin(dup_counts[dup_counts == 1].index)]

# 2. Duplicates - pick only second occurrence
dupes_only = df[df['Timestamp'].isin(dup_counts[dup_counts > 1].index)]
second_dupes = (
    dupes_only.groupby('Timestamp')
    .nth(1)      # Pick second
    .reset_index()
)

# Combine both
final_df = pd.concat([non_dupes, second_dupes]).sort_index()

# Save result
final_df.to_csv(r"C:\Users\dsp96\Desktop\New folder\Updated1_Merged_MD_old.csv", index=False)

print("Done — second duplicates + original non-duplicates kept.")
