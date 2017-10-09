#Jess Huang
#Cryptocurrency Portfolio Checker
#Checks price of your alt-coins and calculates your total worth daily then notifies you.

#figure how to run a script periodically.

from bs4 import BeautifulSoup
import requests
import decimal

#Gets Ark, Neo, then Omisego Coin price
ark_page = requests.get("https://coinmarketcap.com/currencies/ark/")
neo_page = requests.get("https://coinmarketcap.com/currencies/neo/")
omg_page = requests.get("https://coinmarketcap.com/currencies/omisego/")
eth_page = requests.get("https://coinmarketcap.com/currencies/ethereum/")

ark_soup = BeautifulSoup(ark_page.content, "html.parser")
neo_soup = BeautifulSoup(neo_page.content, "html.parser")
omg_soup = BeautifulSoup(omg_page.content, "html.parser")
eth_soup = BeautifulSoup(eth_page.content, "html.parser")


ark_price = ark_soup.find("span", {"id": "quote_price"}).get_text().lstrip('$')
neo_price = neo_soup.find("span", {"id": "quote_price"}).get_text().lstrip('$')
omg_price = omg_soup.find("span", {"id": "quote_price"}).get_text().lstrip('$')
eth_price = eth_soup.find("span", {"id": "quote_price"}).get_text().lstrip('$')


omg_coins = 49.97
ark_coins = 73.60398864
neo_coins = 17
eth_coins = 0.11470651

ark_worth = float(ark_price)*ark_coins
neo_worth = float(neo_price)*neo_coins
omg_worth = float(omg_price)*omg_coins
eth_worth = float(eth_price)*eth_coins

ans = ark_worth + neo_worth + omg_worth + eth_worth

D = decimal.Decimal
cent = D('0.01')

ans = D(ans)

ans = ans.quantize(cent,rounding=decimal.ROUND_UP)
ans = int(ans)

print("Coin Prices: \nARK: $" + ark_price + " USD\nNEO: $"+ neo_price + " USD\nOMG: $" + omg_price +" USD\nETH: $" + eth_price +" USD\n")
print("Coin Worth:  \nARK: $" + str(D(ark_worth).quantize(cent,rounding=decimal.ROUND_UP)) + " USD\nNEO: $"+ str(D(neo_worth).quantize(cent,rounding=decimal.ROUND_UP)) + " USD\nOMG: $" + str(D(omg_worth).quantize(cent,rounding=decimal.ROUND_UP))  + "USD\nETH: $" + str(D(eth_worth).quantize(cent,rounding=decimal.ROUND_UP)) +" USD\n")

#Convert USD to AUD

url = "http://www.xe.com/currencyconverter/convert/?Amount=" + str(ans) + "&From=USD&To=AUD"
currency_page = requests.get(url)
cp_soup = BeautifulSoup(currency_page.content, "html.parser")
aud = cp_soup.find("span", {"class": "uccResultAmount"}).get_text()


print("Your total Cryptocurrency worth is $" + str(aud) + " AUD")


