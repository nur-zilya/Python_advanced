from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__)
# app.config["SECRET_KEY"] = "mysecretkey"


class RegistrationForm(FlaskForm):
    email = StringField()
    phone = StringField()
    name = StringField()


@app.route("/registration", methods=["GET", "POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        if all(field.data for field in [form.email, form.phone, form.name]):
            email, phone, name = form.email.data, form.phone.data, form.name.data
            return "Registration successful!"
        else:
            return f"Validation error: {form.errors}", 400

    else:
        return """ <form method="POST">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email"><br>

            <label for="phone">Phone:</label>
            <input type="tel" id="phone" name="phone"><br>

            <label for="name">Name:</label>
            <input type="text" id="name" name="name"><br>

            <input type="submit" value="Submit">
        </form>
    """



if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
