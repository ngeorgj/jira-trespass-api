# Jira Trespass API

### Flask Jira Database Connector - API

##### Description

This project is a Flask-based API that connects to a database and provides a route to query any table and return the results in JSON format. It utilizes SQLAlchemy for database connectivity and querying.
Installation

Create a new folder<br>
`mkdir trespass-api`

Clone the repository:<br>
`git clone https://github.com/ngeorgj/jira-trespass-api.git`

Navigate to the project directory:<br>
`cd trespass-api`

Install the dependencies
`pip install -r requirements.txt`

Create a .env file or edit the existing one in the project directory and add the following environment variables:
```bash
DB_ENGINE=database_engine
DB_USER=database_user
DB_PASSWORD=database_password
DB_HOSTNAME=database_hostname
DB_PORT=database_port
DB_DATABASE=database_name
```
Replace the values with your own database connection details.


## Usage

Start the Flask Server:<br>
`python api.py`

Make a request towards a table: <br>
`http://localhost:5000/query/<table_name>`
<small>Replace <table_name> with the name of the table you want to query.</small>

That should return you the api result for all columns in the database.

## Database Configuration

The database connection details are stored in the .env file. Ensure that you have correctly set the environment variables mentioned in the Installation section.

## Contact

For any inquiries or feedback, please contact nivaldo.georg@cprime.com or ngj.netrunner@gmail.com

> " Because the API does not provide enough information " - Nivaldo Georg Junior, circa 2023





