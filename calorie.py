import requests
from selectorlib import Extractor


class Calorie:

    # BMR= 10*weight + 6.25*height - 5*age + 5 - 10*temperature

    def __init__(self, weight, height, age, country, city):
        self.weight = weight
        self.height = height
        self.age = age
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def get_temperature(self):
        url = f"https://www.timeanddate.com/weather/{self.country}/{self.city}"
        text = requests.get(url).text
        extractor = Extractor.from_yaml_file("tem.yaml")
        tem = extractor.extract(text)["temp"].replace("\xa0°C", "").strip()
        return float(tem)

    def calculate(self):
        return (
            10 * self.weight
            + 6.25 * self.height
            - 5 * self.age
            + 5
            - 10 * self.get_temperature()
        )


if __name__ == "__main__":
    calorie = Calorie(89, 185, 29, "poland", "warsaw")
    print(calorie.calculate())
