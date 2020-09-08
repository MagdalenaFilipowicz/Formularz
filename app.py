import csv
import requests
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/for")
def hello():
    code = get_code()
    print(code)
    return render_template("formu.html", code=code)

@app.route("/calc", methods=["POST"])
def post_message():
    x = input
    return x 

def get_rates():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()
    currency = data[0]
    rates = currency.get("rates")
    return rates

def get_code():
    rates = get_rates()
    return [row.get("code") for row in rates]

app.run()