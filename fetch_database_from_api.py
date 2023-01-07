# Importing necessary libraries and modules
from flask import Flask, request, jsonify
import mysql.connector as conn

# Creating the app object for the class Flask
app = Flask(__name__)

# ===============================================
# A function to fetch data from sql table via api
# ===============================================

# Setting the address of get_from_sql as '/sql'
# Methods allowed to 'POST' --> request through the body
# 'GET' --> visible request
@app.route('/sql', methods = ['GET','POST'])
def get_from_sql():

    # Establish the connection
    # Change the passwd before running
    mydb = conn.connect(host = "localhost", user = "root", passwd = "xxxxxxxx")

    # Create the cursor for executing the queries
    cursor = mydb.cursor()

    # Condition if the request through 'POST' or not
    if (request.method == 'POST'):
        
        # Getting the name of the database and the table to fetch records from
        table_name = request.json['table']

        # Creating the query
        query = "select * from " + table_name

        # Executing the query
        cursor.execute(query)

        # fetching all the records
        rows = cursor.fetchall()

        # Returning the json version of the records
        return jsonify(rows)

# ===========================================
# A function to fetch data from mongodb table
# ===========================================

@app.route('/mongodb', methods = ['GET', 'POST'])
def get_from_mongodb():
    pass

# Initializing to run the queries automatically without calling the functions 
if __name__ == '__main__':
    app.run()