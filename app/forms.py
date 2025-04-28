# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, TextAreaField, DateField
# from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
# from app.models import User

# class RegistrationForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Sign Up')

#     def validate_username(self, username):
#         user = User.query.filter_by(username=username.data).first()
#         if user:
#             raise ValidationError('That username is taken. Please choose a different one.')

#     def validate_email(self, email):
#         user = User.query.filter_by(email=email.data).first()
#         if user:
#             raise ValidationError('That email is taken. Please choose a different one.')

# class LoginForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('Login')

# class SearchForm(FlaskForm):
#     query = StringField('Search for places', validators=[DataRequired()])
#     submit = SubmitField('Search')

# class PreferencesForm(FlaskForm):
#     interests = SelectField('Interests', choices=[
#         ('adventure', 'Adventure'),
#         ('history', 'History & Culture'),
#         ('nature', 'Nature & Wildlife'),
#         ('spiritual', 'Spiritual'),
#         ('food', 'Food & Cuisine'),
#         ('beach', 'Beaches'),
#         ('hill_station', 'Hill Stations')
#     ], validators=[DataRequired()])
#     budget = SelectField('Budget', choices=[
#         ('low', 'Low (< ₹5000)'),
#         ('medium', 'Medium (₹5000 - ₹20000)'),
#         ('high', 'High (> ₹20000)')
#     ], validators=[DataRequired()])
#     duration = IntegerField('Duration (days)', validators=[DataRequired()])
#     submit = SubmitField('Get Recommendations')

# class BookingForm(FlaskForm):
#     start_date = DateField('Start Date', validators=[DataRequired()])
#     end_date = DateField('End Date', validators=[DataRequired()])
#     num_people = IntegerField('Number of People', validators=[DataRequired()])
#     submit = SubmitField('Book Now')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                                   validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is taken. Please choose another.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already registered.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class SearchForm(FlaskForm):
    query = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Search')

class BookingForm(FlaskForm):
    start_date = DateField('Start Date', validators=[DataRequired()])
    end_date = DateField('End Date', validators=[DataRequired()])
    num_people = IntegerField('Number of People', validators=[DataRequired()])
    submit = SubmitField('Book Now')

class PreferencesForm(FlaskForm):
    interests = TextAreaField('Travel Interests', validators=[DataRequired()])
    submit = SubmitField('Get Recommendations')