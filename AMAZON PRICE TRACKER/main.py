import pprint
import lxml
import requests
from bs4 import BeautifulSoup
import smtplib
import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

SMTP_ADDRESS = os.environ.get("SMTP_ADDRESS")
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
TO_EMAIL_ADDRESS = os.environ.get("TO_EMAIL_ADDRESS")
PORT = int(os.environ.get("PORT"))
URL = "https://www.wildberries.ru/catalog/311657546/detail.aspx?size=471382771"

DESIRED_PRICE = 2939
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "DNT": "1",
    "Host": "www.wildberries.ru",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
}

def scrape_a_price_from_a_website(url, header):
    session = requests.Session()
    response = requests.get(url=url, headers=header)
    print("Status Code:", response.status_code)

    web_site_content = response.text
    with open("page.html", "w", encoding="utf-8") as file:
        file.write(web_site_content)
        
    soup = BeautifulSoup(web_site_content, "html.parser")
    # soup = BeautifulSoup(web_site_content, "lxml")
    print(soup.prettify())

    price_tag = soup.find(name="ins", class_="price-block__final-price wallet")
    if price_tag:
        price_text = price_tag.get_text(strip=True)
        price_float = float(price_text.replace(" ₽", "").replace(" ", "").replace(",", "."))
        return price_float
    else:
        print("⚠️ Price tag not found!")    
        return None

def scrape_a_title_of_a_product_from_a_website(url, header):
    session = requests.Session()
    response = requests.get(url=url, headers=header)
    web_site_content = response.text
    soup = BeautifulSoup(web_site_content, "html.parser")
    # soup = BeautifulSoup(web_site_content, "lxml")
    print(soup.prettify())
    title_tag = soup.find(name="h1", class_="product-page__title")
    if title_tag:
        title = title_tag.get_text()
        return title
    else:
        print("⚠️ Title not found!")
        return "Unknown Product"

def sending_notification_via_email(current_price, desired_price, from_email, to_email, password, smtp_address, port, title_of_a_product):
    if current_price is None:
        print("⚠️ No price found. Email not sent.")
        return

    if current_price <= desired_price:
        with smtplib.SMTP_SSL(host=smtp_address, port=port) as connection:
            connection.login(user=from_email, password=password)
            connection.sendmail(
                from_addr=from_email,
                to_addrs=to_email,
                msg=f"Subject:Price Alert 🚨\n The price has dropped!\n The current price of {title_of_a_product}is: ${current_price}!")


sending_notification_via_email(current_price=scrape_a_price_from_a_website(url=URL, header=headers),
                               desired_price=DESIRED_PRICE,
                               from_email=EMAIL_ADDRESS,
                               to_email=TO_EMAIL_ADDRESS,
                               password=EMAIL_PASSWORD,
                               smtp_address=SMTP_ADDRESS,
                               port=PORT,
                               title_of_a_product=scrape_a_title_of_a_product_from_a_website(url=URL, header=headers))
