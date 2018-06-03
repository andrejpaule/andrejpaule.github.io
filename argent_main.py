import csv

currencies = {}
rates = {}

with open('currencies.csv','r') as currencies_input:
    currencies_reader = csv.reader(currencies_input)
    for row in currencies_reader:
        currencies[row[0].decode("utf-8-sig").encode("utf-8")] = str(row[1].decode("utf-8-sig").encode("utf-8"))

with open('rates.csv','r') as rates_input:
    rates_reader = csv.reader(rates_input)
    for row in rates_reader:
        rates[str(row[0]).decode("utf-8-sig").encode("utf-8")] = float(row[1])

def calculate_daily(country, days):
    daily_us = 50
    total_us = daily_us * days
    currency = currencies[country]
    rate = rates[currency]
    total_local = total_us * rate
    return total_local

country = raw_input("Which country are you visiting?")
duration = int(raw_input("How many days will you spend there?"))

print "Traveling to %s for %d days? You should take with you %d %ss." % (country, duration, calculate_daily(country.upper(), duration), currencies[country.upper()])
