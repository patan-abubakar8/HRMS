# HRMS (Human Resource Management System)

This is a basic HRMS (Human Resource Management System) built with Flask. It provides functionalities for employee management, attendance tracking, and basic reporting.

# Features

- Employee Management (CRUD operations)
- Attendance Tracking
- Department-wise Employee Count Report

# Features Detailed Explanation

Employee Management:


Add Employee: Employees can be added via the /employees route using a POST request.
View Employees: The list of employees is displayed on the same route.
Update Employee: An individual employee's details can be updated through the /employee/<id> route.
Delete Employee: Employees can be deleted using the /employee/delete/<id> route.


Attendance Management:


Mark Attendance: Attendance can be marked via the /attendance route using a POST request.
Get Attendance: The attendance records for a specific employee can be retrieved via the /attendance/<employee_id> route.


Report Generation:


Department Report: The department report can be generated and viewed through the /report route.

# Project Structure

```
hrms/
├── app.py
├── models.py
├── routes/
│   ├── __init__.py
│   ├── employee.py
│   ├── attendance.py
│   └── reports.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── employee_list.html
│   └── department_report.html
├── static/
│   └── css/
│       └── style.css
├── requirements.txt
├── README.md
└── db.yaml
```

# Setup and Installation

 Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

 Install the required packages:
   ```
   pip install -r requirements.txt
   ```
   if it doesnt works try install manually the packages mentioned in the requirements.txt file

 Create a `db.yaml` file in the project root with your MySQL credentials:
   ```yaml
   mysql_host: localhost
   mysql_user: rrot
   mysql_password: 1234
   mysql_db: hrms_database
   ```

5. Set up your MySQL database:
   - Create a database named `hrms_database`
   - Create tables for `employees` and `attendance`

6. Run the application:
   ```
   python app.py
   ```

The application will be accessible at `http://localhost:5000`.

## Usage

- Navigate to the home page to see an overview of the system.
- Use the "Employees" page to manage employee information.
- The "Department Report" page shows a graphical representation of employee count by department.


# Testing Suggestions

To ensure that all features work , consider the following testing steps:

Run the Application: Start the Flask app with python app.py.

Add Employee: Navigate to the employees page and test adding an employee.

View Employee List: Check if the added employee appears in the list.

Update Employee: Select an employee to edit and test the update functionality.

Delete Employee: Test the deletion of an employee.

Mark Attendance: Use the attendance functionality to mark and retrieve attendance for employees.

Generate Report: Check the report generation functionality for department statistics.

# reference

Youtube : https://www.youtube.com/watch?v=6L3HNyXEais&t=1086s
