import mysql.connector
from mysql.connector import Error
import matplotlib.pyplot as plt
import numpy as np

year = int(input("Enter year: "))

genres = {}

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='movies_db',
                                         user='python_user',
                                         password='password1')
    if connection.is_connected():
        db_info = connection.get_server_info()
        cursor = connection.cursor()

        cursor.execute("select * from movies_" + str(year))
        record = cursor.fetchall()
        
        for movie in record:
            for genre_index in range(1, 3):
                current_genre = movie[genre_index + 2]
                if current_genre is not None:
                    if current_genre not in genres:
                        genres[current_genre] = 1
                    else:
                        genres[current_genre] += 1



except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()

# Sort the list of genres
genres = {k: v for k, v in sorted(genres.items(), key=lambda item: item[1])}

genre_list = list(genres.keys())
y_vals = np.arange(len(genre_list))
num_movies = list(genres.values())

plt.barh(y_vals, num_movies, align='center', alpha=0.5)
plt.yticks(y_vals, genre_list)
plt.xlabel("Number of movies")

plt.show()
