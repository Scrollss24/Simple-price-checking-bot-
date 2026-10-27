from bs4 import BeautifulSoup
import requests
import time
from mail import email_message




print("Hello to my price checking bot")
to = input("Firstly input your email address: ")
URL = input("Secondly input your URL adress: ")
Max_price = float(input("Lastly set your max price: "))

def checking_price():
    page = requests.get(URL)
    page.encoding = "utf-8"
    soup = BeautifulSoup(page.text, 'html.parser')
    finding = soup.find('p', class_='price_color')
    if finding:
        price = finding.text
        clean_price = float(price.replace("£",""))
        print(f"Actual price: {clean_price}")
        if clean_price < Max_price:
            return True
        else:
            print("Still too high price")
            return False
    else:
        print("Check your url address if it is correct")
        return False

while True:
    sending = checking_price()
    if sending:
        print("I´m sending an email")
        email_message(to)
        break
    time.sleep(10)