import mysql.connector
from mysql.connector import Error
import json

try:
    # connects to the database using the 'python_user' user
    connection = mysql.connector.connect(host = 'localhost',
                                         database = 'movies_db',
                                         user = 'python_user',
                                         password = 'password1')

    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to to MySQL Server Version ", db_info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

        # get the information from the json file
        with open('movies.json', 'r') as infile:
            movie_data = json.load(infile)
        
        # create the table
        table_name = 'movies_' + str(movie_data['year'])
        # cursor.execute("create table " + table_name + "(id int not null AUTO_INCREMENT, title varchar(50), genre_1 varchar(20), genre_2 varchar(20), genre_3 varchar(20), primary key (id));")
        # print("Table {} has been created.".format(table_name))

        # insert the data
        for k in movie_data:
            # We don't want the year inserted
            if k != 'year':
                title = movie_data[k]['title']
                genres = movie_data[k]['genre']
                values = '(null,"' + title + '",'
                # add in genres if they exist, null otherwise
                for g in genres:
                    values += '"' + g + '",'
                for _ in range(3 - len(genres)):
                    values += "null,"
                
                # remove the last comma and add final parentheses and semicolan
                values = values[:-1]
                values += ");"

                # execute the insert
                cursor.execute("insert into " + table_name + " (id, title, genre_1, genre_2, genre_3) values " + values)

        print("Movie data has been inserted into {}".format(table_name))

        # drop the table for testing
        # cursor.execute("drop table " + table_name + ";")
        # print("Table has been dropped for testing purposes")
                
        


except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")