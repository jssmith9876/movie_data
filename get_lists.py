import requests
from bs4 import BeautifulSoup

# gets the top 100 lists for every year and puts them into a text file

# def get_all_lists(start_year, end_year):
#     for year in range(start_year, end_year + 1):
#         source = requests.get('https://www.google.com/search?q=top+100+movies+of+' + str(year)).text
#         soup = BeautifulSoup(source, 'lxml')

#         def is_website(url):
#             return ("http" in url) and ("imdb") in url


#         # Finds the first imdb link and returns it
#         for result in soup.find_all('a'):
#             link = result['href']
#             if is_website(link):
#                 real_url = link.split('&')[0]
#                 real_url = real_url[7:]

#                 with open("movie_links.txt", "a+") as outfile:
#                     outfile.write(str(year) + ": " + real_url + '\n')

#                 print("Retrieved url for year " + str(year))

#                 break
        

# gets the top 50 lists for every year for most popular movie and puts them into text file

def get_all_lists(start_year, end_year):
    for year in range(start_year, end_year + 1):
        url = "https://www.imdb.com/search/title/?title_type=feature&year="
        url += str(year)
        with open("movie_links.txt", "a+") as outfile:
            outfile.write(str(year) + ": " + url + "\n")
