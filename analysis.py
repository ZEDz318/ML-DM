import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("preprocessed_data.csv")

film_unique_values = df['Film_film'].unique()
actor_unique_values = df['Nominee_actor'].unique()
director_unique_values = df['Nominee_director'].unique()

# You can check for duplicate rows based on the "MovieID" column
# duplicate_movies = df[df.duplicated(subset='Film_film', keep=False)]
#
# # If duplicate_movies is empty, it means every movie is unique
# if duplicate_movies.empty:
#     print("Every movie is unique in the dataset.")
# else:
#     print("There are duplicate movies in the dataset.")
#     print("Duplicate rows:")
#     print(len(duplicate_movies))


# Budget vs Revenue
profit = []
for i in df['Film_film']:
    for j in film_unique_values:
        if i == j:
            d = {'film' : i,
                 'p': df[df['Film_film'] == i]['revenue'].values[0]-df[df['Film_film'] == i]['budget'].values[0]}
            profit.append(d)

names = [entry["film"] for entry in profit]
values = [entry["p"] for entry in profit]

# Create a scatter plot
plt.scatter(names, values)

# Labeling the axes
plt.xlabel('Film')
plt.ylabel('Profit')

# Show the plot
plt.show()
# plt.figure(figsize=(8, 6))
# plt.scatter(film_unique_values, df["budget"] - df["revenue"], alpha=0.7, c='b', edgecolors='k')
# plt.title("Revenue vs Budget")
# plt.xlabel("Budget")
# plt.ylabel("Revenue")
# plt.grid(True)

# Show the plot
plt.show()

# Actors vs Revenue

# plt.figure(figsize=(8, 6))
# plt.scatter(df["Nominee_actor"], df["revenue"], alpha=0.7, c='b', edgecolors='k')
# plt.title("Revenue vs Nominee_actor")
# plt.xlabel("Nominee_actor")
# plt.ylabel("Revenue")
# plt.grid(True)
#
# # Show the plot
# plt.show()
