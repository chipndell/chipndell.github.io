from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

class FeedbackForm(FlaskForm):
	f_name = StringField('Username', [validators.Length(min=4, max=25)])    
	l_name = StringField('Username', [validators.Length(min=4, max=25)])
	email = StringField('Email Address', [validators.Length(min=6, max=35)])
	subject = StringField('Username', [validators.Length(min=4, max=25)])
	message = StringField('Username', [validators.Length(min=4, max=25)])
	send_now = SubmitField('Send Now')
   
