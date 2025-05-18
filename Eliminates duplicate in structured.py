import pandas as pd

# Load the file
file_path = r'C:\Users\dsp96\Desktop\New folder\NewM2_removedfile.csv'
df = pd.read_csv(file_path)

# Remove duplicates based on the 'Timestamp' column, keeping the first occurrence
df_cleaned = df.drop_duplicates(subset='Timestamp', keep='first')

# If you want to keep the last occurrence instead of the first, use:
# df_cleaned = df.drop_duplicates(subset='Timestamp', keep='last')

# Save the cleaned DataFrame to a new file
output_path = r'C:\Users\dsp96\Desktop\New folder\Cleaned_NewM_removedfile.csv'
df_cleaned.to_csv(output_path, index=False)

# Print a message to confirm
print("Duplicates removed. The output is saved.")
