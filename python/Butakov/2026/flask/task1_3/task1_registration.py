from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import Email, InputRequired, NumberRange, Optional
from hw2_validators import number_length

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(message="Укажите Email"), Email(message="Email некорректный")])
    phone = IntegerField(
        validators=[
            InputRequired(message="Укажите номер телефона"),
            NumberRange(min=1, message="Некорректный номер телефона"),
            number_length(10, 10, message="Некорректный номер телефона"),
        ]
    )
    name = StringField(validators=[InputRequired(message="Укажите имя")])
    address = StringField(validators=[InputRequired(message="Укажите адрес")])
    index = IntegerField(validators=[InputRequired(message="Укажите индекс")])
    comment = StringField(validators=[Optional()])


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Пользователь с {email} и +7{phone} зарегистрирован"

    return f"Ошибка ввода, {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
