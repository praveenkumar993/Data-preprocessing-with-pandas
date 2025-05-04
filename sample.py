from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Sample data
X = [[1, 2], [3, 4], [5, 6], [7, 8]]
y = [0, 1, 0, 1]

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

print("Scaled Training Data:\n", X_train)
print("Scaled Testing Data:\n", X_test)
print("Training Labels:\n", y_train)
print("Testing Labels:\n", y_test)
