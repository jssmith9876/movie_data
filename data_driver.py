import get_lists
import Webscraper
import sql_connector


# Get all the top 100 urls and store them into a list
get_lists.get_all_lists(2015, 2018)

with open("movie_links.txt", "r") as url_list:
    for line in url_list:
        year = int(line[:4])
        url = line[6:]
        url = url[:-1] # Get rid of the break line
        Webscraper.scrape_url(year, url)
        sql_connector.make_table()

        break




