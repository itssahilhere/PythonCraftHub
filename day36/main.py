STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key_stock= 'IMYUREIMZ31WY64O'
symbol=None
import imp
from urllib import request
import requests
from twilio.rest import Client
from datetime import date, timedelta
account_sid="AC97c982bfc2be2eb0b9db40229487f84d"
auth_token="c064487c7a0b25e5c1150339126882e5"
today = date.today()
yesterday=today-timedelta(days=1)
day_bef_yes=today-timedelta(days=2)
y1=str(yesterday)
y2=str(day_bef_yes)
# print()
# print(yesterday)
# print(day_bef_yes)
param={'function':'TIME_SERIES_DAILY','symbol':STOCK,'apikey':api_key_stock}
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
r = requests.get(url='https://www.alphavantage.co/query',params=param)
r.raise_for_status()
data_YESTERDAY=r.json()["Time Series (Daily)"][y1]['4. close']
data_DAY_YESTERDAY=r.json()["Time Series (Daily)"][y2]['4. close']
d1=float(data_YESTERDAY)
d2=float(data_DAY_YESTERDAY)
diff=(d2-d1)
per=round(diff/d1*100)
if(diff>0):
    symbol="▲"
else:
    symbol="▼"
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def news():
    npar={'q':COMPANY_NAME,
        'sortBy':'popularity&',
        'apiKey':'6d76bee538e449feaa0bd95c3def5c16'}
    ul=requests.get(url='https://newsapi.org/v2/everything',params=npar)
    ul.raise_for_status()
    data_articles=ul.json()['articles']
    for i in range(0,3):
        headline=data_articles[i]["title"]
        description=data_articles["description"]
        format_article=f"{STOCK} {abs(per)} {symbol} % \n HEADLINE: {headline}\nDESCRIPTION: {description}"
        client = Client(account_sid, auth_token)
        message = client.messages \
                        .create(
                            body=format_article,
                            from_='+19402895845',
                            to='+918271442309'
                        )
        print(message.status)                

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
if(abs(per)>5):
    news()


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

