from flask_wtf import FlaskForm
from wtforms import StringField,validators,PasswordField,BooleanField
from wtforms import StringField,validators,PasswordField,BooleanField,TextAreaField

class registrationForms(FlaskForm):
		username=StringField('username',validators=[validators.DataRequired(),validators.length(4,20)])
		email=StringField('email',validators=[validators.DataRequired(),validators.Email()])
		password=PasswordField('password',validators=[validators.data_required()])
		confrim_password=PasswordField('confrim password',validators=[validators.data_required()
																						 ,validators.equal_to('password')])

class loginform(FlaskForm):
		email = StringField('email', validators=[validators.DataRequired(), validators.Email()])
		password = PasswordField('password', validators=[validators.data_required()])
		remember=BooleanField('remember me')


class profileform(FlaskForm):
	new_username = StringField('new_username', validators=[validators.DataRequired(), validators.length(4,20)])
	new_email = StringField('new_email', validators=[validators.DataRequired(), validators.Email()])
	# new_password = PasswordField('new_password', validators=[validators.data_required()])

class postform(FlaskForm):
	title = StringField('title', validators=[validators.DataRequired(), validators.length(4,30)])
	content = TextAreaField('content', validators=[validators.DataRequired()])
