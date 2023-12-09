import pandas as pd

# Read the acting data
acting_data = pd.read_csv("datasets/oscars/oscardata_acting.csv")

# Read the director data
director_data = pd.read_csv("datasets/oscars/oscardata_bestdirector.csv")

# Read the best picture data
picture_data = pd.read_csv("datasets/oscars/oscardata_bestpicture.csv")

# Define a function to rename columns
def rename_columns(df, suffix):
    renamed_columns = {}
    for column in df.columns:
        renamed_columns[column] = f"{column}_{suffix}"
    df.rename(columns=renamed_columns, inplace=True)

# Replace suffixes with "_actor" for acting_data columns
rename_columns(acting_data, "actor")

# Replace suffixes with "_director" for director_data columns
rename_columns(director_data, "director")

# Replace suffixes with "_film" for picture_data columns
rename_columns(picture_data, "film")

# Merge the acting_data, director_data, and picture_data DataFrames
merged_data1 = acting_data.merge(director_data, left_on=["Year_actor", "Film_actor"], right_on=["Year_director", "Film_director"], how="inner")

merged_data = merged_data1.merge(picture_data, left_on=["Year_actor", "Film_actor"], right_on=["Year_film", "Film_film"], how="inner")

# Save the merged_data DataFrame to a new CSV file
merged_data.to_csv("merged_oscar_data.csv", index=False)