from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField

from calorie import Calorie

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template("index.html")


class CaloriesFormPage(MethodView):
    def get(self):
        calories_form = CaloriesForm()

        return render_template("calories_form_page.html", caloriesform=calories_form)

    def post(self):
        calories_form = CaloriesForm(request.form)
        calories = Calorie(
            weight=float(calories_form.weight.data),
            height=float(calories_form.height.data),
            age=float(calories_form.age.data),
            country=calories_form.country.data,
            city= calories_form.city.data,
        ).calculate()
        return render_template(
            "calories_form_page.html",
            caloriesform=calories_form,
            calories=calories,
            result=True,
        )


class CaloriesForm(Form):
    weight = StringField("Weight: ", default=89)
    height = StringField("Height: ", default=185)
    age = StringField("Age: ", default=29)
    country = StringField("Country: ", default="Poland")
    city = StringField("City: ", default="Warsaw")
    button = SubmitField("Calculate")


app.add_url_rule("/", view_func=HomePage.as_view("home_page"))
app.add_url_rule(
    "/calories_form", view_func=CaloriesFormPage.as_view("calories_form_page")
)


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)