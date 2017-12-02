import os

from app import create_app
from app.models import Employee
from flask_sqlalchemy import SQLAlchemy
from app import db

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)
admin = Employee(email="truongngocasic@gmail.com",username="admin",password="linhidecaf",is_admin=True)

db = SQLAlchemy(app)
db.session.add(admin)
db.session.commit()
