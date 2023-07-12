import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import paramiko

load_dotenv()

app = Flask(__name__)

# Get the Environment Variables
variables = os.environ

# SSH credentials
ssh_host = variables['SSH_HOST']
ssh_port = int(variables['SSH_PORT'])
ssh_username = variables['SSH_USERNAME']
ssh_password = variables['SSH_PASSWORD']

# Remote database connection details
db_host = variables['DB_HOST']
db_port = int(variables['DB_PORT'])
db_username = variables['DB_USERNAME']
db_password = variables['DB_PASSWORD']
database = variables['DB_DATABASE']

# Create an SSH client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the SSH server
ssh_client.connect(ssh_host, ssh_port, ssh_username, ssh_password)

# Set up the SSH tunnel
tunnel = ssh_client.get_transport().open_tunnel(
    (db_host, db_port),  # destination host and port
    ('localhost', 5432)  # local (tunnel) host and port
)

# Configure Flask SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://localhost:5432/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Route to query any table and return results in JSON format
@app.route('/query/<table>', methods=['GET'])
def query_table(table):
    result = db.session.execute(text(f"SELECT * FROM {table}"))
    columns = result.keys()
    rows = [dict(zip(columns, row)) for row in result]
    return jsonify(rows)


if __name__ == '__main__':
    app.run()

# Close the SSH tunnel and client when the application exits
@app.teardown_appcontext
def teardown_app(exception=None):
    tunnel.close()
    ssh_client.close()
