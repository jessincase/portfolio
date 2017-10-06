#Jess Huang
#Cryptocurrency Portfolio Checker
#Checks price of your alt-coins and calculates your total worth daily then notifies you.

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

print(ark_price)

omg_coins = 49.97
ark_coins = 73.60398864
neo_coins = 17
eth_coins = 0.11470651

ans = float(ark_price)*ark_coins + float(neo_price)*neo_coins + float(omg_price)*omg_coins + float(eth_price)*eth_coins

D = decimal.Decimal
cent = D('0.01')

ans = D(ans)
print("Your total Cryptocurrency worth is $" + str(ans.quantize(cent,rounding=decimal.ROUND_UP)) + " USD")
