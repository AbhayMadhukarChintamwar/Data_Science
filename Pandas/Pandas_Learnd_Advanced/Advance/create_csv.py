import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of rows
n = 1000

# Generate realistic wine quality data
data = {
    'fixed acidity': np.round(np.random.uniform(4.0, 16.0, n), 2),
    'volatile acidity': np.round(np.random.uniform(0.1, 1.6, n), 3),
    'citric acid': np.round(np.random.uniform(0.0, 1.0, n), 3),
    'residual sugar': np.round(np.random.uniform(0.5, 15.0, n), 2),
    'chlorides': np.round(np.random.uniform(0.01, 0.2, n), 3),
    'free sulfur dioxide': np.random.randint(1, 75, n),
    'total sulfur dioxide': np.random.randint(6, 300, n),
    'density': np.round(np.random.uniform(0.9900, 1.0050, n), 5),
    'pH': np.round(np.random.uniform(2.8, 4.0, n), 2),
    'sulphates': np.round(np.random.uniform(0.3, 2.0, n), 2),
    'alcohol': np.round(np.random.uniform(8.0, 15.0, n), 2),

    # Quality score between 0 to 10
    'quality': np.random.randint(0, 11, n)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save CSV file
file_name = '1.0 - winequality-red.csv'
df.to_csv(file_name, sep=';', index=False)

print(f"CSV file '{file_name}' created successfully with {n} rows!")

# Display first 5 rows
print(df.head())