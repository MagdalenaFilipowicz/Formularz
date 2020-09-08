import csv
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/for")
def hello():
    code = get_code()
    print(code)
    return render_template("formu.html", code=code)
    
def get_rates():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()
    currency = data[0]
    rates = currency.get("rates")
    return rates

def get_code():
    rates = get_rates()
    return [row.get("code") for row in rates]

def get_bid():
    rates = get_rates()
    bid_pln = [row.get("bid") for row in rates] 
    return bid_pln

@app.route("/calc", methods=["POST"])
def post_message():
    rates = get_rates()
    x = request.form["amount"]
    y = bid_pln*int(x)
    return str(y)

app.run()