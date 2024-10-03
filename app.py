# app.py
from flask import Flask
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Configure db
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

# Import routes AFTER initializing the app and MySQL
from routes import employee, attendance, reports

# Register blueprints
app.register_blueprint(employee.bp)
app.register_blueprint(attendance.bp)
app.register_blueprint(reports.bp)

if __name__ == '__main__':
    app.run(debug=True)
