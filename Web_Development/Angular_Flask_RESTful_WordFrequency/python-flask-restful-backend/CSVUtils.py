#Imports
import csv
from DatabaseUtils import *


# USAGE :

"""
FILE_PATH_1 = "/home/ayushi/project/Quotes.csv"
FILE_PATH_2 = "/home/ayushi/project/Words.csv"
putCSVIntoDatabase(FILE_PATH_1)
putCSVIntoDatabase(FILE_PATH_2)

"""

# This is the code that reads the CSV.
def putCSVIntoDatabase(data_file):
    # We'll have to pass the file path from the server file to this function
    data_dict = dict()  # This is the dictionary. It contains all the read CSV values.
    reader = csv.DictReader(data_file)
    num_rows = 0
    for row in reader:
        print(row.keys())
        print(row.values())
        num_rows += 1
        # Getting the contents of each column.
        dbObject = databaseObject2(int(row["word_id"]), str(row["search_word"]))
        insertIntoTable2(dbObject) # Inserted!

# Now, doing the same here, but for Quotes.csv
def putCSVIntoDatabase2(data_file):
    data_dict = dict()
    reader = csv.DictReader(data_file)
    num_rows = 0
    for row in reader:
        print(row.keys())
        print(row.values())
        num_rows += 1
        dbObject = databaseObject(int(row["quote_id"]), str(row["author"]), str(row["quote"]))
        insertIntoTable(dbObject)

