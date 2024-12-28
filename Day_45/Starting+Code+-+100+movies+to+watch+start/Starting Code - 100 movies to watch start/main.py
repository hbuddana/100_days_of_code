import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)    
movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, "html.parser")

# Extract all the movie titles
movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in movies]

# Reverse the list to get the movies in descending order
movie_titles = movie_titles[::-1]

# Write the movie titles to a file      
with open("movies.txt", mode="w") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")



