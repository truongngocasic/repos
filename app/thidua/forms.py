from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

class PersonalForm(FlaskForm):
    """
    Form for Personal - Thidua
    """

    field_1       = StringField('field_1', validators=[DataRequired()])
    field_2       = StringField('field_2', validators=[DataRequired()])
    field_2_1     = StringField('field_2_1', validators=[DataRequired()])
    field_2_2     = StringField('field_2_2', validators=[DataRequired()])
    field_2_3     = StringField('field_2_3', validators=[DataRequired()])
    field_2_3_1   = StringField('field_2_3_1', validators=[DataRequired()])
    field_2_3_2   = StringField('field_2_3_2', validators=[DataRequired()])
    field_2_3_3   = StringField('field_2_3_3', validators=[DataRequired()])
    field_2_3_3_a = StringField('field_2_3_3_a', validators=[DataRequired()])
    field_2_3_3_b = StringField('field_2_3_3_b', validators=[DataRequired()])
    field_2_4     = StringField('field_2_4', validators=[DataRequired()])
    field_3       = StringField('field_3', validators=[DataRequired()])
    field_4       = StringField('field_4', validators=[DataRequired()])
    field_4_1     = StringField('field_4_1', validators=[DataRequired()])
    field_4_2     = StringField('field_4_2', validators=[DataRequired()])
    field_4_2_a   = StringField('field_4_2_a', validators=[DataRequired()])
    field_4_2_b   = StringField('field_4_2_b', validators=[DataRequired()])
    field_4_2_c   = StringField('field_4_2_c', validators=[DataRequired()])
    field_5       = StringField('field_5', validators=[DataRequired()])
    field_5_1     = StringField('field_5_1', validators=[DataRequired()])
    field_5_2     = StringField('field_5_2', validators=[DataRequired()])
    field_6       = StringField('field_6', validators=[DataRequired()])

    submit = SubmitField('Submit')

