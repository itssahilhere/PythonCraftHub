import requests
from datetime import datetime
import smtplib
lat=22.3511148
lng=78.6677428
MY_EMAIL = "sa7257934076@gmail.com"
MY_PASSWORD = "sahil@123420"
par={'lat':lat,'lng':lng,'formatted':0}
response=requests.get("https://api.sunrise-sunset.org/json",params=par)

response.raise_for_status()
data=response.json()['results']['sunrise']
print(data)