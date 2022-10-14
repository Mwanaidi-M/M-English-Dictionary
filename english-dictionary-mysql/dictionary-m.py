import mysql.connector

# variables for the database connection
my_db_creds = {
    "user": "my_username",
    "password": "my_password",
    "host": "localhost",
    "database": "my_dbname"
}

try:
    # creating a MySQLConnection object
    my_connection = mysql.connector.MySQLConnection(**my_db_creds)

except mysql.connector.Error as mysql_err:
    print(mysql_err)

else:
    # get user input; capitalize the input's first letter; remove any trailing white spaces.
    user_word = input("Enter a word:\t").capitalize().strip()

    # display message if the input is an empty string
    if user_word == ['']:
        print("No valid word was entered.")
    else:
        # create a cursor object
        with my_connection.cursor() as term_cursor:
            # define the query to search for the word definition
            term_query = "SELECT definition FROM entries WHERE word = %s "

            # execute the query passing the user input as a list
            term_cursor.execute(term_query, [user_word])

            # retrieve the search result set
            search_word_results = term_cursor.fetchall()

        # check if result set in empty
        if len(search_word_results) == 0:
            # taking first 3 characters in the user input
            cut_term = "".join(user_word)[:3]

            user_word = user_word.lower()

            # new cursor object to check for words with close match to user input
            with my_connection.cursor() as check_term_cursor:
                # writing the full cut_term using mysql wildcard to avoid issues for example-> 'we%'
                param = f"{cut_term}%"

                # query to search for word that match the param
                check_term_query = "SELECT word FROM entries WHERE word LIKE %s"

                check_term_cursor.execute(check_term_query, [param])

                # get the result set; convert into a set to remove duplicates; convert back to list
                results = list(set(check_term_cursor.fetchall()))

            # check if result set is empty
            if len(results) == 0:
                # inform user no such word is in the dictionary
                print(f"Sorry. The word {user_word} isn't in the dictionary.")
            else:
                # inform user which words closely match their input; showing 10 matches for now
                print(f"We have these words with similar spellings to ['{user_word}']:")

                for result in results[:9]:
                    print("".join(result))

        # if the result set is not empty, display the definitions in the database
        else:
            for result in search_word_results:
                definition = "".join(result).replace("\n  ", "").replace(",\n ", "")
                print(definition)

    my_connection.close()
