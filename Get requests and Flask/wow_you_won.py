from flask import Flask, render_template_string
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

app = Flask(__name__)



class RegistrationForm(FlaskForm):
    name = StringField()
    family_name = StringField()
    ticket = IntegerField()

@app.route('/', methods=['GET', 'POST'])
def check_winner():
    message = ""
    form = RegistrationForm()

    if form.validate_on_submit():
        name = form.name.data
        family_name = form.family_name.data
        ticket = form.ticket.data

        # Проверим номер билета на счастливый
        if str(ticket)[0] != '0' and len(str(ticket)) == 6 and sum(int(d) for d in str(ticket)[:3]) == sum(int(d) for d in str(ticket)[3:]):
            message = f'Поздравляем, {name} {family_name}!'
        else:
            message = 'Неудача. Попробуйте ещё раз!'

    return render_template_string(
        '''
        <h1>{{ message }}</h1>
        <form method="POST">
            {{ form.name.label }} {{ form.name() }}<br>
            {{ form.family_name.label }} {{ form.family_name() }}<br>
            {{ form.ticket.label }} {{ form.ticket() }}<br>
            <input type="submit" value="Submit">
        </form>
        ''',
        form=form,
        message=message
    )


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
