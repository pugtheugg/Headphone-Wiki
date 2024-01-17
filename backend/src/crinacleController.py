from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to store information
data_store = '{"name":"John", "age":30, "car":null}'


# Route for handling GET requests
@app.route('/api/data', methods=['GET'])
def get_data():

    query = """SELECT * FROM iem"""

    get_data(query)




# Route for handling POST requests
@app.route('/api/data', methods=['POST'])
def add_data():
    # Get JSON data from the request body
    new_data = request.get_json()

    # Add new data to the data store
    data_store.append(new_data)

    return jsonify({"message": "Data added successfully"})
