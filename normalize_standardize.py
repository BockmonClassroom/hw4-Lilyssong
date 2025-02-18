import pandas as pd

# Load dataset
df = pd.read_csv("Iris.csv")

# Normalization (Min-Max Scaling)
normalized = df.copy()
for col in normalized.columns[:4]:  # Assuming first 4 columns are numerical
    min_val = normalized[col].min()
    max_val = normalized[col].max()
    normalized[col] = (normalized[col] - min_val) / (max_val - min_val)
normalized.to_csv("iris_normalized.csv", index=False)

# Standardization (Z-Score)
standardized = df.copy()
for col in standardized.columns[:4]:  # Standardizing first 4 columns
    mean = standardized[col].mean()
    std = standardized[col].std()
    standardized[col] = (standardized[col] - mean) / std
standardized.to_csv("iris_standardized.csv", index=False)

print("Normalization and Standardization complete. Files saved.")
