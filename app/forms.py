from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, IntegerField
from wtforms.validators import DataRequired, ValidationError, EqualTo


class CreateQuestionForm(FlaskForm):
	indep_var = IntegerField('Year for prediction', validators=[DataRequired()])
	submit = SubmitField('Submit')