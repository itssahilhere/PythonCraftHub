import requests
from datetime import datetime
import smtplib
import time
MY_LAT = 22.3511148 # Your latitude
MY_LONG = -78.6677428 # Your longitude
MY_EMAIL = "sa7257934076@gmail.com"
MY_PASSWORD = "sahil@123420"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while(iss_latitude>=17.3511148 and iss_latitude<=22.3511148 and iss_longitude>=-83.6677428 and iss_longitude<=-78.6677428 and (time_now>=sunset or time_now<=sunrise)):
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:SPACE!\n\n hey! look up!!!"
            )
    time.sleep(60)

