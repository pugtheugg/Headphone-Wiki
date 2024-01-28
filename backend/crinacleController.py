from flask import Flask, request, jsonify
from databaseHandler import *

app = Flask(__name__)

# Sample data to store information
data_store = '{"name":"John", "age":30, "car":null}'


# Route for handling GET requests
@app.route('/api/data', methods=['GET'])
def get_data():

    db_handler = DatabaseHandler()
    data = db_handler.get_all_iems()
    db_handler.close_connection()

    return jsonify(data)


# Route for handling POST requests
@app.route('/api/data', methods=['POST'])
def add_data():
    # Get JSON data from the request body
    new_data = request.get_json()

    # Add new data to the data store
    data_store.append(new_data)

    return jsonify({"message": "Data added successfully"})
