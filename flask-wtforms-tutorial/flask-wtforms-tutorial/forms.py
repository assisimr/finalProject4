"""Form object declaration."""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, TextField, SubmitField, PasswordField, DateField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length, Email, URL


class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField(
        'Name',
        [DataRequired()]
    )
    email = StringField(
        'Email',
        [
            Email(message=('Not valid.')),
            DataRequired()
        ]
    )
    body = TextField(
        'Message',
        [
            DataRequired(),
            Length(min=4, message='Too short.')
        ]
    )
    # recaptcha = RecaptchaField()
    submit = SubmitField('Submit')


class SignupForm(FlaskForm):
    """Sign up for a user account."""
    email = StringField(
        "Email",
        [
            Email(message='Not valid .'),
            DataRequired()
        ]
    )
    password = PasswordField(
        "Password",
        [
            DataRequired(message="enter password.")
        ]
    )
    confirmPassword = PasswordField(
        "Repeat Password",
        [
            EqualTo(password, message="Passwords must match.")
        ]
    )
    title = SelectField(
        "Title",
        [DataRequired()],
        choices=[
            ("Aero", "aero"),

        ]
    )
    website = StringField("Website", validators=[URL()])
    birthday = DateField("Your Birthday")
    # recaptcha = RecaptchaField()
    submit = SubmitField("Submit")