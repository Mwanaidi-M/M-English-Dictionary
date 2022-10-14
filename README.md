# PROJECT: INTERACTIVE ENGLISH DICTIONARY

This is an English dictionary program made using Python. This program is meant to accept a word from a user and returns the various definitions of the word.

If a user gives an incorrectly spelt word, the program will confirm with the user by giving them a word that closely matches the input and return the definition, otherwise it will inform the user the word does not exist.

Modules used: **[json, difflib]**

Also created another version of the dictionary that was checking for word definitions from the database.

User is prompted for a word and a query is made to the table to check whether the word is present otherwise, the user will be shown some random words that have a close match to the input.

If the word is not in the database, the user will be informed of that.

Modules used **[mysql-connector-python]**