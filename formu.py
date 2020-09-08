import csv
import requests


response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
currency = data[0]
rates = currency.get("rates")
print(rates)
for row in rates:
    print(f"{row.get('currency')};{row.get('code')};{row.get('bid')};{row.get('ask')}")

with open('rates.csv', 'w') as csvfile:
    rates_writer = csv.writer(csvfile, delimiter=';')
    for row in rates:
        rate = [row.get('currency'), row.get('code'), row.get('bid'), row.get('ask')]
        rates_writer.writerow(rate)