from flask import Blueprint, request, redirect, url_for, jsonify
from models import Attendance

bp = Blueprint('attendance', __name__)

@bp.route('/attendance', methods=['POST'])
def mark_attendance():
    employee_id = request.form['employee_id']
    date = request.form['date']
    status = request.form['status']
    
    Attendance.mark(employee_id, date, status)
    return redirect(url_for('employee.employee', id=employee_id))

@bp.route('/attendance/<int:employee_id>')
def get_attendance(employee_id):
    attendance = Attendance.get_by_employee(employee_id)
    return jsonify(attendance)
