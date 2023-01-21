from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


class LoginForm(FlaskForm):
    email = StringField(label="email", validators=[validators.DataRequired(), Email(message="either @ or you missed . ")])
    password = PasswordField(label="Password", validators=[validators.Length(min=8)])
    submit = SubmitField(label="Log in")

app.secret_key = 'otilia04'


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@gmail.com" and login_form.password.data == "123456789":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)