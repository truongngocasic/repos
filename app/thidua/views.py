from flask import render_template
from flask_login import current_user, login_required

from . import thidua
from forms import PersonalForm
from .. import db
from ..models import Employee

@thidua.route('/personal')
@login_required
def personal():
    """
    Render the personal template on the /personal route
    """
    form = PersonalForm()
    return render_template('thidua/personal.html', form=form, title="Personal")

@thidua.route('/group')
@login_required
def group():
    """
    Render the personal template on the /personal route
    """
    return render_template('thidua/group.html', title="Group")

