import pandas as pd

# Step 1: List your CSV files manually
csv_files = [
    r'C:\Users\dsp96\Desktop\New folder\True_1_11_03_25_MD_old.csv',
    r'C:\Users\dsp96\Desktop\New folder\True_2_11_03_25_MD_old.csv'
]

# Step 2: Open final output file
output_file = r'C:\Users\dsp96\Desktop\New folder\final_output1.csv'


with open(output_file, 'w') as f:
    for file in csv_files:
        df = pd.read_csv(file)
        df.to_csv(f, index=False, line_terminator='\n')


print(f"final_output1.csv is done")