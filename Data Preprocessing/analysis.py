import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("preprocessed_data.csv")

film_unique_values = df['Film_film'].unique()
actor_unique_values = df['Nominee_actor'].unique()
director_unique_values = df['Nominee_director'].unique()

Nom_GoldenGlobe = df[df.columns[df.columns.str.startswith("Nom_GoldenGlobe")+df.columns.str.startswith("Nom_BAFTA")+df.columns.str.startswith("Oscarstat_totalnoms")]]
Win_GoldenGlobe = df[df.columns[df.columns.str.startswith("Win_GoldenGlobe")+df.columns.str.startswith("Win_BAFTA")+df.columns.str.startswith("Oscarstat_previouswins")]]

total_g_noms = Nom_GoldenGlobe.sum(axis=1)
total_g_wins = Win_GoldenGlobe.sum(axis=1)

df['total_talent'] = total_g_noms + total_g_wins


revenue = df['revenue']
total_talent = df['total_talent']

# create a new df with unique films
new_df = df.groupby('Film_film').agg({'budget': 'first', 'total_talent': 'sum', 'revenue': 'first', 'Rating_IMDB_actor': 'first'}).reset_index()
new_df.to_csv("simplified.csv", index=False)
genre_columns = [col for col in df.columns if col.startswith("Genre_") and col.endswith("_actor") or col.startswith("Film_film") or col.startswith("budget")]
# print(genre_columns)


genre_counts = {}

# Iterate through the columns
for column in df.columns:
    if column.startswith("Genre") and column.endswith("actor"):
        genre = column.split("_")[1]  # Extract the genre name
        genre_count = df[column].sum()  # Sum of values in the column
        if genre_count > 0:
            genre_counts[genre] = genre_counts.get(genre, 0) + genre_count

# Calculate the average budget for each genre
for genre in genre_counts:
    genre_counts[genre] = int(df[df["Genre_" + genre + "_actor"] == 1]["budget"].mean())

plt.figure(figsize=(8, 8))
plt.pie(genre_counts.values(), labels=['']*len(genre_counts), autopct='%1.1f%%', startangle=140)

# Add a legend with genre labels
plt.legend(genre_counts.keys(), title="Genres")

plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
plt.title("Budget Distribution by Genre")
plt.show()
# #--------------------------GENRE-------------------------------
# Create a new DataFrame from the dictionary
# genre_df = pd.DataFrame(list(genre_counts.items()), columns=["Genre", "Count"])
# genre_df = genre_df.sort_values(by="Count", ascending=False)
#
# print(genre_df)
# plt.figure(figsize=(8, 8))
#
# plt.pie(genre_df["Count"],  autopct=lambda p: f"{p:.1f}%" if p >= 1.5 else '', startangle=140)
# plt.legend(genre_df["Genre"], title="Genres", loc="center left", bbox_to_anchor=(1, 0.5))
#
# plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
#
# plt.title("Genre Distribution")
#
# # Display the pie chart
# plt.show()
#--------------------------GENRE-------------------------------
# # Create a scatter plot
# plt.figure(figsize=(8, 6))
# plt.scatter(new_df['budget'], new_df['Rating_IMDB_actor'], alpha=0.5)
# plt.title('Rating vs. budget')
# plt.xlabel('budget')
# plt.ylabel('Rating')
# plt.grid(True)
#
# # Display the plot
# plt.show()