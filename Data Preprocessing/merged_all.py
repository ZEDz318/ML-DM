import pandas as pd

# Read the previously merged Oscar data
merged_data = pd.read_csv("merged_oscar_data.csv")

# Read the TMDB dataset
tmdb_data = pd.read_csv("datasets/imdb/tmdb_5000_movies.csv")

# Merge the two DataFrames based on the movie title
merged_data_tmdb = merged_data.merge(tmdb_data, left_on="Film_film", right_on="original_title", how="inner")

# List of columns to be dropped
columns_to_drop = [
    'Nowin_SAG_acting_actor', 'Win_SAG_acting_actor', 'Nonom_SAG_acting_actor', 'Nom_SAG_acting_actor',
    'Nowin_SAG_bestcast_actor', 'Win_SAG_bestcast_actor', 'Nonom_SAG_bestcast_actor', 'Nom_SAG_bestcast_actor',
    'Nowin_SAG_bestcast_film', 'Win_SAG_bestcast_film', 'Nonom_SAG_bestcast_film', 'Nom_SAG_bestcast_film',
    'Nowin_Criticschoice_actor', 'Win_Criticschoice_actor', 'Nonom_Criticschoice_actor', 'Nom_Criticschoice_actor',
    'Nowin_Criticschoice_director', 'Win_Criticschoice_director', 'Nonom_Criticschoice_director', 'Nom_Criticschoice_director',
    'Nowin_Criticschoice_film', 'Win_Criticschoice_film', 'Nonom_Criticschoice_film', 'Nom_Criticschoice_film',
    'Age_[0-25]_actor', 'Age_[25-35]_actor', 'Age_[35-45]_actor', 'Age_[45-55]_actor', 'Age_[55-65]_actor', 'Age_[65-75] _actor', 'Age_[75+] _actor',
    'MPAA_rating_actor', 'MPAA_G_actor', 'MPAA_PG_actor', 'MPAA_PG-13_actor', 'MPAA_R_actor', 'MPAA_NC-17_actor',
    'MPAA_rating_director', 'MPAA_G_director', 'MPAA_PG_director', 'MPAA_PG-13_director', 'MPAA_R_director', 'MPAA_NC-17_director',
    'MPAA_rating_film', 'MPAA_G_film', 'MPAA_PG_film', 'MPAA_PG-13_film', 'MPAA_R_film', 'MPAA_NC-17_film',
    'Release_Q1_actor', 'Release_Q2_actor', 'Release_Q3_actor', 'Release_Q4_actor', 'Release_date_actor', 'Birthyear_actor',
    'Film_actor', 'Film_director'
]

# Drop the specified columns from the DataFrame
merged_data_tmdb = merged_data_tmdb.drop(columns=columns_to_drop)

# Save the merged DataFrame to a new CSV file
merged_data_tmdb.to_csv("merged_data_all.csv", index=False)
