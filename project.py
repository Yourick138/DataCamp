# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Filtrar apenas pelo que é considerado filme
netflix_subset = netflix_df[netflix_df['type'] == 'Movie']

# Filtrar apenas por filmes dos 90's
movies_90s = netflix_subset[(netflix_subset["release_year"] >= 1990) & (netflix_subset["release_year"] < 2000)]

# Plotar o gráfico da duração dos filmes dos 90's
plt.hist(movies_90s["duration"], bins=20, edgecolor='black')
plt.title("Movie Duration in the 90's")
plt.xlabel("Duration (min)")
plt.ylabel("Frequency")
plt.show()

# Selecionar apenas curtas de ação dos 90's
short_action_movies = movies_90s[(movies_90s["genre"] == "Action") & (movies_90s["duration"] < 90)]

# Número de curtas de ação dos 90's
num_short_action_movies = len(short_action_movies)
num_short_action_movies
