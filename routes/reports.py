from flask import Blueprint, render_template
from models import Report

bp = Blueprint('reports', __name__)

@bp.route('/report')
def department_report():
    report_data = Report.get_department_report()
    return render_template('department_report.html', report_data=report_data)
