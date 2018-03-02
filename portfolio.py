#Jess Huang
#Cryptocurrency Portfolio Checker
#Checks price of your alt-coins and calculates your total worth daily then prints to console.

from bs4 import BeautifulSoup
import requests
import decimal
from decimal import Decimal
import datetime

#gets webpages of coins
ark_page = requests.get("https://coinmarketcap.com/currencies/ark/")
neo_page = requests.get("https://coinmarketcap.com/currencies/neo/")
omg_page = requests.get("https://coinmarketcap.com/currencies/omisego/")
eth_page = requests.get("https://coinmarketcap.com/currencies/ethereum/")
icx_page = requests.get("https://coinmarketcap.com/currencies/icon/")

#Scrapes and parses each coin price
ark_soup = BeautifulSoup(ark_page.content, "html.parser")
neo_soup = BeautifulSoup(neo_page.content, "html.parser")
omg_soup = BeautifulSoup(omg_page.content, "html.parser")
eth_soup = BeautifulSoup(eth_page.content, "html.parser")
icx_soup = BeautifulSoup(icx_page.content, "html.parser")

ark_price = ark_soup.find("span", {"id": "quote_price"}).get_text().split('\n', 2)[1].lstrip('$')
neo_price = neo_soup.find("span", {"id": "quote_price"}).get_text().split('\n', 2)[1].lstrip('$')
omg_price = omg_soup.find("span", {"id": "quote_price"}).get_text().split('\n', 2)[1].lstrip('$')
eth_price = eth_soup.find("span", {"id": "quote_price"}).get_text().split('\n', 2)[1].lstrip('$')
icx_price = icx_soup.find("span", {"id": "quote_price"}).get_text().split('\n', 2)[1].lstrip('$')

#Insert quantity of each coin. 
omg_coins = 10
ark_coins = 10
neo_coins = 10
eth_coins = 10
icx_coins = 10

#Calculates worth of each coin
ark_worth = float(ark_price)*ark_coins
neo_worth = float(neo_price)*neo_coins
omg_worth = float(omg_price)*omg_coins
eth_worth = float(eth_price)*eth_coins
icx_worth = float(icx_price)*icx_coins

#Calculates total worth
ans = ark_worth + neo_worth + omg_worth + eth_worth + icx_worth

#Rounds up worth
D = decimal.Decimal
cent = D('0.01')
ans = D(ans)
ans = ans.quantize(cent,rounding=decimal.ROUND_UP)
ans = int(ans)

#Display each coin price and then worth
print("Coin Prices: \nARK: $" + ark_price + " USD\nNEO: $"+ neo_price + " USD\nOMG: $" + omg_price +" USD\nETH: $" + eth_price +" USD\nICX: $" + icx_price + " USD\n" )
print("Coin Worth:  \nARK: $" + str(D(ark_worth).quantize(cent,rounding=decimal.ROUND_UP)) + " USD\nNEO: $"+ str(D(neo_worth).quantize(cent,rounding=decimal.ROUND_UP)) + " USD\nOMG: $" + str(D(omg_worth).quantize(cent,rounding=decimal.ROUND_UP))  + " USD\nETH: $" + str(D(eth_worth).quantize(cent,rounding=decimal.ROUND_UP)) +" USD\nICX: $" + str(D(icx_worth).quantize(cent,rounding=decimal.ROUND_UP)) + " USD\n")

#Converts USD to AUD
url = "http://www.xe.com/currencyconverter/convert/?Amount=" + str(ans) + "&From=USD&To=AUD"
currency_page = requests.get(url)
cp_soup = BeautifulSoup(currency_page.content, "html.parser")
aud = cp_soup.find("span", {"class": "uccResultAmount"}).get_text()

#Display current time and then total worth.
print("Time: " + str(datetime.datetime.now()))
print("Your total Cryptocurrency worth is $" + str(aud) + " AUD")

#Prints the percentage you are up or down by
original_investment = 1000


aud = aud.replace(',', '')
percentage = (Decimal(aud)-original_investment)/original_investment*100

if Decimal(aud) >= original_investment:
    print("+" + str(D(percentage).quantize(cent,rounding=decimal.ROUND_UP)) + '%')
else:
    print(str(D(percentage).quantize(cent,rounding=decimal.ROUND_UP)) + '%')



