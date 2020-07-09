import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.volotea.com/it/offerte-voli/catania/bari/?adults=1&childs=0&infants=0&jorney=oneway"
user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]
HEADERS = {"User-Agent": user_agent_list[0]}
PRICE_VALUE = 160
EMAIL_ADDRESS = "vittoriopipoli@gmail.com"

def trackPrices():
    price = float(getPrice())
    if price > PRICE_VALUE:
        diff = int(price - PRICE_VALUE)
        print(f"Still £{diff} too expensive")
    else:
        print("Cheaper! Notifying...")
        # sendEmail()
    pass

def getPrice():
    page = requests.get(URL, headers=HEADERS)
    print(page)
    soup = BeautifulSoup(page.content)
    print(soup)
    print("Trying to Parse Html...")
    title = soup.find(attrs={"data-date" : "2020-10-28"})
    if title is not None:
        title = title.get_text().strip()

    price = soup.find(attrs={"data-date" : "2020-07-30"})
    if price is not None:
        price = price.get_text().strip()

    print(title)
    print(price)
    return price

def sendEmail():
    subject = "Amazon Price Dropped!"
    mailtext='Subject:'+subject+'\n\n'+URL

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_ADDRESS, 'wazLincsLuna18!')
    server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, mailtext)
    pass

if __name__ == "__main__":
    # trackPrices()
    getPrice()