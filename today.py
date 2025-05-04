import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Basic operation: filter people older than 28
older_than_28 = df[df['Age'] > 28]
print("\nPeople older than 28:")
print(older_than_28)
