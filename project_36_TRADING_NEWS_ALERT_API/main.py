import smtplib
import requests
import datetime
import  html

STOCK = "AAPL"
COMPANY_NAME = "apple"
API_KEY_MARKET = "key"
API_KEY_NEWSAPI = 'key'
FROM_EMAIL_ADDRESS = "sender_email"
PASSWORD = "password"
TO_EMAIL_ADDRESS = "recepient_address"
API_ENDPOINT_MARKET = "https://www.alphavantage.co/query"
API_ENDPOINT_NEWS = "https://newsapi.org/v2/everything"

ongoing_day = datetime.date.today()
yesterday = str(ongoing_day - datetime.timedelta(days=1))
day_before_yesterday = str(ongoing_day - datetime.timedelta(days=2))

list_of_titles = []
list_of_news = []

news_parameters = {
    "q":COMPANY_NAME,
    "apiKey": API_KEY_NEWSAPI
}
market_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_MARKET,
}
response_market = requests.get(url=API_ENDPOINT_MARKET, params=market_parameters)
response_market.raise_for_status()
market_data = response_market.json()
print(market_data)

yesterday_close_price = float(market_data["Time Series (Daily)"][yesterday]['4. close'])
day_before_yesterday_close_price = float(market_data["Time Series (Daily)"][day_before_yesterday]['4. close'])
difference = (day_before_yesterday_close_price - yesterday_close_price) / day_before_yesterday_close_price
difference_abs_and_rounded = round(abs((day_before_yesterday_close_price - yesterday_close_price) / day_before_yesterday_close_price), 2)

if difference_abs_and_rounded >= 5:
    response_news = requests.get(url=API_ENDPOINT_NEWS, params=news_parameters)
    response_news.raise_for_status()
    news_data = response_news.json()
    for item in range(0, 3):
        title = news_data["articles"][item]["title"]
        title = html.unescape(title)
        list_of_titles.append(title)
    for item in range(0, 3):
        news = news_data["articles"][item]["description"]
        news = html.unescape(news)
        list_of_news.append(news)
    with smtplib.SMTP_SSL("smtp.mail.ru", 465) as connection:
        connection.login(user=FROM_EMAIL_ADDRESS, password=PASSWORD)
        for item in range (0, 3):
            if difference >= 0:
                connection.sendmail(
                    from_addr=FROM_EMAIL_ADDRESS,
                    to_addrs=TO_EMAIL_ADDRESS,
                    msg=f"Subject: Difference is 🔺{difference_abs_and_rounded}%!"
                        f" \n Headline: {list_of_titles[item]}\n\n Brief: {list_of_news[item]}")
            else:
                connection.sendmail(
                    from_addr=FROM_EMAIL_ADDRESS,
                    to_addrs=TO_EMAIL_ADDRESS,
                    msg=f"Subject: Difference is 🔻{difference_abs_and_rounded}%!"
                        f" \n Headline: {list_of_titles[item]}\n\n Brief: {list_of_news[item]}")
