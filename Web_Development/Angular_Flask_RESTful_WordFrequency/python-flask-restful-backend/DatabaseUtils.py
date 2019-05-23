# Imports
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


"""
    First, we'll create a class that will represent whatever you have in your database.
"""

#Classes to represent the tables in the database
class databaseObject:
    def __init__(self, quote_id, author, quote):
        self.quote_id = quote_id
        self.author = author
        self.quote = quote

class databaseObject2:
    def __init__(self, word_id, search_word):
        self.word_id = word_id
        self.search_word = search_word


# Insertion function for quotes table
def insertIntoTable(databaseObject):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='testdb', #name of database
                                             user='root',   # replace with username
                                             password='noitsme')   # replace with password
        sql_insert_query = """ INSERT INTO `quotes`
                                                 (`quote_id`, `author`, `quote`) VALUES ({},{},{})""".format(databaseObject.quote_id, 							databaseObject.author, databaseObject.quote)
        cursor = connection.cursor()
        result  = cursor.execute(sql_insert_query) # gets inserted here.
        connection.commit() # committing changes in DB.
        print ("Record inserted successfully into quotes table")
    except mysql.connector.Error as error :
        connection.rollback() #rollback if any exception occured
        print("Failed inserting record into quotes table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


#Insertion function for words table
def insertIntoTable2(databaseObject2):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='testdb', # name of database
                                             user='root',   # replace with username
                                             password='noitsme')   # replace with password
        sql_insert_query = """ INSERT INTO `words`
                                                 (`word_id`, `search_word`) VALUES ({},{},{})""".format(databaseObject2.word_id, 							databaseObject2.search_word)
        cursor = connection.cursor()
        result  = cursor.execute(sql_insert_query) # gets inserted here.
        connection.commit() # committing changes in DB.
        print ("Record inserted successfully into words table")
    except mysql.connector.Error as error :
        connection.rollback() #rollback if any exception occured
        print("Failed inserting record into words table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Selecting count of word.
def selectCount(word):
    # This is a counter
    returnValue = 0
    try:
        mySQLconnection = mysql.connector.connect(host='localhost',
                                                  database='testdb',
                                                  user='root',
                                                  password='noitsme')
        
        
        sql_select_Query = "select quote from quotes"
        cursor = mySQLconnection .cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchAll()
        for record in records:
            # For every quote
            for each_word in record:
                if(each_word == word):
                    returnValue += 1
        # Now, returning count.
        return returnValue

    except Exception as exc:
        print("[!] Exception occurred!")
        print(exc)

# Simple function to return a list of all words
def getAllWords():
    try:
        mySQLconnection = mysql.connector.connect(host='localhost',
                                                 database='testdb',
                                                 user='root',
                                                 password='noitsme')
        sql_select_Query = "select word from words"
        cursor = mySQLconnection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchAll()
        return records
    except Exception as exc:
        print("[!] Exception occurred!")
        print(exc)

