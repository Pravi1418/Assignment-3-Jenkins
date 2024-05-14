from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuration for connecting to RDS database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@hostname:port/database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    position = db.Column(db.String(100))

# Sample route to fetch employees from the database
@app.route('/employees')
def get_employees():
    employees = Employee.query.all()
    employee_list = []
    for employee in employees:
        employee_data = {'name': employee.name, 'position': employee.position}
        employee_list.append(employee_data)
    return jsonify(employee_list)

if __name__ == '__main__':
    app.run(debug=True)
