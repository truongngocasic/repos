# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import Department, Role

class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RoleForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EmployeeAssignForm(FlaskForm):
    """
    Form for admin to assign departments and roles to employees
    """
    department = QuerySelectField(query_factory=lambda: Department.query.all(),
                                  get_label="name")
    role = QuerySelectField(query_factory=lambda: Role.query.all(),
                            get_label="name")
    submit = SubmitField('Submit')

class SalaryCodeForm(FlaskForm):
    """
    Form for admin to add or edit salary code
    """
    cur_code = StringField('Current Code', validators=[DataRequired()])
    next_code = StringField('Next Code', validators=[DataRequired()])
    notes = StringField('Notes', validators=[DataRequired()])
    submit = SubmitField('Submit')

class SalaryIndexForm(FlaskForm):
    """
    Form for admin to add or edit salary index
    """
    cur_index = StringField('Current Index', validators=[DataRequired()])
    next_index = StringField('Next Index', validators=[DataRequired()])
    notes = StringField('Notes', validators=[DataRequired()])
    submit = SubmitField('Submit')

class SalaryRateForm(FlaskForm):
    """
    Form for admin to add or edit salary rate
    """
    cur_rate = StringField('Current Rate', validators=[DataRequired()])
    next_rate = StringField('Next Rate', validators=[DataRequired()])
    notes = StringField('Notes', validators=[DataRequired()])
    submit = SubmitField('Submit')

