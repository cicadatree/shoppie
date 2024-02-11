from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, DateField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo

# create forms for user registrations, login, transaction creation, category creation, etc.