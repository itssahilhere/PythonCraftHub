import requests
# import os
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient

# proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {'https': os.environ['https_proxy']}
account_sid="AC97c982bfc2be2eb0b9db40229487f84d"
token="c064487c7a0b25e5c1150339126882e5"
par={'lat':22.572645,'lon':88.363892,'appid':'4f3a37e19e1fd53376455a758eb5ccc1','exclude':'current,minutely,daily'}
data=requests.get(url="https://api.openweathermap.org/data/2.5/onecall?",params=par)
data.raise_for_status()
for i in range(0,12):
    result=data.json()['hourly'][i]['weather'][0]['id']
    if(True):
        client=Client(account_sid,token)
        message = client.messages \
                .create(
                     body="PAGA.",
                     from_='+19402895845',
                     to='+917257934076'
                 )
        print(message.status)

        
        break



# print(result)