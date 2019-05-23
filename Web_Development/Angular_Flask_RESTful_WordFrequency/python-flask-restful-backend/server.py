# Imports
from DatabaseUtils import *
from CSVUtils import *
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json
# End of Import Statements

app = Flask(__name__)
# Origin set to stackblitz project as I was using Stackblitz to edit at the time
cors = CORS(app, resources={r"/api/*": {"origins": "https://angular-blpafm.stackblitz.io"}})
FILEPATH1 = open("./Words.csv", "r").readlines()
FILEPATH2 = open("./Quotes.csv", "r").readlines()



# Dealing with CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

# Putting CSVs
@app.route("/putcsv", methods = ['PUT'])
def putCSVs():
    data = request.get_json()
    boolean = data["bool"]
    # So, we'll set it to true or false depending
    # on whether we want to put it in the Quotes table
    # or in the Words table.
    if(boolean):
        putCSVIntoDatabase2(FILEPATH2)
    else:
        putCSVIntoDatabase(FILEPATH1)
    return jsonify({}), 200

# This will get all the words.
@app.route("/words", methods = ['GET'])
def getWords():
    # Done!
    return jsonify({"allWords": getAllWords()}), 200

# We're using a post here because we're sending input to it
# So using a get doesn't make much sense.
@app.route("/word", methods = ['POST'])
def postWord():
    # Define get to get DB records and return count of word.
    data = request.get_json()   # This will get the data in JSON format.
    output = data['word'] # Now, output contains the word we passed in.
    return jsonify({"result": selectCount(output)}), 200 # Returned!

# Getting all quotes
@app.route("/quotes", methods = ['GET'])
def getQuotes():
    # Make a method called getAllQuotes in DatabaseUtils pls :D
    return jsonify({"allQuotes": getAllQuotes()}), 200


if __name__ == '__main__':
    app.run()
