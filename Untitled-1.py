import pandas as pd

# Create a simple dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 22, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Print the whole DataFrame
print("Full DataFrame:\n", df)

# Print just the names column
print("\nNames:\n", df['Name'])

# Get the average age
average_age = df['Age'].mean()
print("\nAverage Age:", average_age)
