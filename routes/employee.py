from flask import Blueprint, render_template, request, redirect, url_for
from models import Employee

bp = Blueprint('employee', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/employees', methods=['GET', 'POST'])
def employees():
    if request.method == 'POST':
        name = request.form['name']
        designation = request.form['designation']
        department = request.form['department']
        date_of_joining = request.form['date_of_joining']
        
        Employee.add(name, designation, department, date_of_joining)
        return redirect(url_for('employee.employees'))
    
    employees = Employee.get_all()
    return render_template('employee_list.html', employees=employees)

@bp.route('/employee/<int:id>', methods=['GET', 'POST'])
def employee(id):
    if request.method == 'POST':
        name = request.form['name']
        designation = request.form['designation']
        department = request.form['department']
        date_of_joining = request.form['date_of_joining']
        
        Employee.update(id, name, designation, department, date_of_joining)
        return redirect(url_for('employee.employees'))
    
    employee = Employee.get_by_id(id)
    return render_template('employee.html', employee=employee)

@bp.route('/employee/delete/<int:id>')
def delete_employee(id):
    Employee.delete(id)
    return redirect(url_for('employee.employees'))
