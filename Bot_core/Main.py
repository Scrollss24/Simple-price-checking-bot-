from bs4 import BeautifulSoup
import requests
import time
from Mail import email_message




print("Hello to my price checking bot")
to = input("Firstly input your email address: ")
URL = input("Secondly input your URL adres: ")
while True:
    try:
        Max_price = float(input("Lastly set your max price: "))
        break
    except ValueError:
        print("Please input a valid price")


def checking_price(url, max_price):
    # taking URL from page
    try:
        page = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'},timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"Oops, something went wrong: {e}")
        return False
    else:
        page.encoding = "utf-8"
        soup = BeautifulSoup(page.text, 'html.parser')
        finding = soup.find('span', class_='price')
        if finding:
            price = finding.text
            clean_price = float(price.replace("zł","").replace(",","."))
            print(f"Actual price: {clean_price}")
            if clean_price < max_price:
                return True
            else:
                print("Still too high price")
                return False
        else:
            print("No price element found on the website")
            return False
while True:
    sending = checking_price(URL, Max_price)
    if sending:
        print("I´m sending an email")
        email_message(to)
        break
    time.sleep(25)