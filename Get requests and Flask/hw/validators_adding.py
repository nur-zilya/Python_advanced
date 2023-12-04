from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField
from wtforms.validators import InputRequired, Email, NumberRange, Optional
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id


@login_manager.user_loader
def load_user(user_id):
    # Replace this with your user loading logic
    return User(user_id)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), NumberRange(min=10000000000, max=99999999999)])
    name = StringField(validators=[InputRequired()])
    password = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField(validators=[Optional()])


class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    password = PasswordField(validators=[InputRequired()])


@app.route("/registration", methods=["GET", "POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        if all(field.data for field in [form.email, form.phone, form.name]):
            email, phone, name = form.email.data, form.phone.data, form.name.data
            # You can perform user registration logic here
            return "Registration successful!"
        else:
            return f"Validation error: {form.errors}", 400

    return render_template("registration.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # Replace this with your user authentication logic
        user = User(form.email.data)
        login_user(user)
        return "Login successful!"

    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "Logged out successfully!"


@app.route("/dashboard")
@login_required
def dashboard():
    return f"Hello, {current_user.id}! This is your dashboard."


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
