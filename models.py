from flask import current_app

class Employee:
    @staticmethod
    def get_all():
        cur = current_app.config['MYSQL'].connection.cursor()
        cur.execute("SELECT * FROM employees")
        employees = cur.fetchall()
        cur.close()
        return employees

    @staticmethod
    def add(name, designation, department, date_of_joining):
        cur = current_app.config['MYSQL'].connection.cursor()
        cur.execute("INSERT INTO employees (name, designation, department, date_of_joining) VALUES (%s, %s, %s, %s)",
                    (name, designation, department, date_of_joining))
        current_app.config['MYSQL'].connection.commit()
        cur.close()

    @staticmethod
    def get_by_id(id):
        cur = current_app.config['MYSQL'].connection.cursor()
        cur.execute("SELECT * FROM employees WHERE id = %s", (id,))
        employee = cur.fetchone()
        cur.close()
        return employee

    @staticmethod
    def update(id, name, designation, department, date_of_joining):
        cur = current_app.config['MYSQL'].connection.cursor()
        cur.execute("UPDATE employees SET name=%s, designation=%s, department=%s, date_of_joining=%s WHERE id=%s",
                    (name, designation, department, date_of_joining, id))
        current_app.config['MYSQL'].connection.commit()
        cur.close()

    @staticmethod
    def delete(id):
        cur = current_app.config['MYSQL'].connection.cursor()
        cur.execute("DELETE FROM employees WHERE id = %s", (id,))
        current_app.config['MYSQL'].connection.commit()
        cur.close()

class Attendance:
    @staticmethod
    def mark(employee_id, date, status):
        cur = current_app.config['MYSQL'].connection.cursor()
        cur.execute("INSERT INTO attendance (employee_id, date, status) VALUES (%s, %s, %s)",
                    (employee_id, date, status))
        current_app.config['MYSQL'].connection.commit()
        cur.close()

    @staticmethod
    def get_by_employee(employee_id):
        cur = current_app.config['MYSQL'].connection.cursor()
        cur.execute("SELECT * FROM attendance WHERE employee_id = %s", (employee_id,))
        attendance = cur.fetchall()
        cur.close()
        return attendance

class Report:
    @staticmethod
    def get_department_report():
        cur = current_app.config['MYSQL'].connection.cursor()
        cur.execute("SELECT department, COUNT(*) as count FROM employees GROUP BY department")
        report_data = cur.fetchall()
        cur.close()
        return report_data
