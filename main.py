import requests
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

current_date = datetime.date.today()
previous_day = current_date - datetime.timedelta(days=1)
two_days_ago = current_date - datetime.timedelta(days=2)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = ""#get your unique api key
API_ENDPOINT = "https://www.alphavantage.co/query"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "datatype": "json",
    "apikey": API_KEY,
    "symbol": STOCK
}
response = requests.get(url=API_ENDPOINT, params=parameters)
data = response.json()

yesterday_price = data["Time Series (Daily)"][str(previous_day)]["4. close"]
day_before_yesterday_price = data["Time Series (Daily)"][str(two_days_ago)]["4. close"]

delta_percentage = ((float(yesterday_price)-float(day_before_yesterday_price))/float(day_before_yesterday_price)) *100
delta_percentage= abs(delta_percentage)


if delta_percentage>1:



    NEWS_API = ""#get your unique api key
    news_parameters = {
        "apiKey":NEWS_API,
        "q":"Tesla",
    }

    news_response= requests.get(url="https://newsapi.org/v2/top-headlines",params=news_parameters)
    data_news=news_response.json()


    news1_headline = data_news["articles"][0]["title"]
    news1_link = data_news["articles"][0]["url"]

    news2_headline =data_news["articles"][1]["title"]
    news2_link = data_news["articles"][1]["url"]

    news3_headline = data_news["articles"][2]["title"]
    news3_link = data_news["articles"][1]["url"]

    subject = f"{delta_percentage}% change observed in your {STOCK}"
    body = f"Here are the latest headlines affecting your {STOCK}:\n1- {news1_headline} || {news1_link}\n2- {news2_headline} || {news2_link}\n3- {news3_headline} || {news3_link}"

    msg = MIMEMultipart()
    msg['From'] = ""#enter from mail
    msg['To'] = ""#enter to mail
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        connection = smtplib.SMTP('smtp.gmail.com', 587)#put any other smtp server according to your service
        connection.starttls()
        connection.login(user="", password="")#get unique app password from mail , and user is your mail
        connection.send_message(msg)
        connection.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error:", e)

