import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

load_dotenv()

app = Flask(__name__)

# Get the Environment Variables
variables = os.environ

# Connect to the database
engine = variables['DB_ENGINE']
user = variables['DB_USER']
password = variables['DB_PASSWORD']
hostname = variables['DB_HOSTNAME']
port = variables['DB_PORT']
database = variables['DB_DATABASE']

app.config['SQLALCHEMY_DATABASE_URI'] = f'{engine}://{user}:{password}@{hostname}:{port}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Route to query any table and return results in JSON format
@app.route('/query/<table>', methods=['GET'])
def query_table(table):
    result = db.session.execute(text(f"SELECT * FROM {table}"))
    columns = result.keys()
    rows = [dict(zip(columns, row)) for row in result]
    return jsonify(rows)


@app.route('/query', methods=['POST'])
def query_table():
    data = request.get_json()  # Retrieve JSON data from request
    result = db.session.execute(text(data['query']))
    columns = result.keys()
    rows = [dict(zip(columns, row)) for row in result]
    return jsonify(rows)


if __name__ == '__main__':
    app.run()
