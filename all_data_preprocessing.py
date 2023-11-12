import pandas as pd

# Load the joined dataset
# Replace 'your_dataset.csv' with the actual file path
dataset = pd.read_csv('merged_data_all.csv')

# Handling missing values
# For numeric columns, replace missing values with 0
numeric_columns = dataset.select_dtypes(include=['number'])
dataset[numeric_columns.columns] = dataset[numeric_columns.columns].fillna(0)

# For string columns, replace missing values with "empty"
string_columns = dataset.select_dtypes(include=['object'])
dataset[string_columns.columns] = dataset[string_columns.columns].fillna("empty")

# Trimming text fields
dataset[string_columns.columns] = dataset[string_columns.columns].apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Identifying redundant columns
redundant_columns = []

# Loop through each column to check for redundancy
for col1 in dataset.columns:
    for col2 in dataset.columns:
        # Skip comparing the column to itself
        if col1 != col2:
            # Check if the values in both columns are the same
            if dataset[col1].equals(dataset[col2]) and col2 not in redundant_columns and col1 not in redundant_columns:
                redundant_columns.append(col2)
print(redundant_columns)
dataset = dataset.drop(columns=redundant_columns)


# Save the merged DataFrame to a new CSV file
dataset.to_csv("preprocessed_data.csv", index=False)
# Now, the 'dataset' DataFrame is cleaned and ready for machine learning.
# You can proceed to build your machine learning models with this DataFrame.
