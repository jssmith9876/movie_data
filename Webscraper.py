import requests
from bs4 import BeautifulSoup
import json

def scrape_url(year, url):
    source = requests.get(url).text

    soup = BeautifulSoup(source, 'lxml')

    movies = {}
    movies['year'] = year

    movie_number = 1

    # grabs the current movie
    for movie in soup.find_all('div', class_='lister-item-content'):
        # display which movie we're retrieving data from
        

        # gets the title of that movie
        title = movie.h3.a.text

        # gets the genre of the movie
        all_genres = movie.p.find('span', class_='genre').text
        genre_list = all_genres.split(', ') # split the genres up into a list
        genre_list[0] = genre_list[0][1:]   # removes the \n from the first element
        genre_list[len(genre_list) - 1] = genre_list[len(genre_list) - 1].strip()  # removes spacing from last element

        # Puts the retrieved infomation into a dictionary
        data = {}
        data['title'] = title
        data['genre'] = genre_list

        movies['#' + str(movie_number)] = data

        movie_number += 1

    with open('movies.json', 'w') as outfile:
        
        json.dump(movies, outfile, indent=2)


