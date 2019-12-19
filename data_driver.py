import get_lists
import Webscraper
import sql_connector


# Get all the top 100 urls and store them into a list
get_lists.get_all_lists(1970, 1971)


with open("movie_links.txt", "r") as url_list:
    for line in url_list:
        year = int(line[:4])
        print("Year: " + str(year))
        url = line[6:]
        url = url[:-1] # Get rid of the break line
        Webscraper.scrape_url(year, url)
        sql_connector.make_table()

        




