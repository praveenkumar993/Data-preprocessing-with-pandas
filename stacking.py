import pandas as pd


df2 = pd.read_csv(r'C:\Users\dsp96\Downloads\True_2_11_03_25_MD_old.csv')
df1 = pd.read_csv(r'C:\Users\dsp96\Downloads\True_1_11_03_25_MD_old.csv')

with open(r'C:\Users\dsp96\Desktop\New folder\final_output.csv', 'w') as f:
    
    df1.to_csv(f, index=False, line_terminator='\n')
    df2.to_csv(f, index=False, line_terminator='\n')
print("final_output.csv created successfully")
