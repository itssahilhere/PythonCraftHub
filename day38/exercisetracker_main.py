from datetime import datetime
import requests
import os
API_ID="187724ce"
API_KEY="bd62fc95ff775776e3edab606f567129"
GENDER = "male"
WEIGHT_KG = 71
HEIGHT_CM = 176
AGE = 19
EXERCISE_END_PIONT=" https://trackapi.nutritionix.com/v2/natural/exercise"
shetty_add_row="https://api.sheety.co/0f5c956ffe3d6786037d2a4b7fb4665b/copyOfMyWorkouts/workouts"
exercise_text=input("TELL ME WHICH EXERCISE YOU DID? ")
headers={
    "x-app-id":API_ID,
    "x-app-key":API_KEY,
    
}
sheety_header={
     "Authorization":"Bearer SAHIL@123420"
}
body={
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response=requests.post(url=EXERCISE_END_PIONT,json=body,headers=headers)
result=response.json()
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
# requests.get('https://api.github.com/user', auth=('user', 'pass'))

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=shetty_add_row, json=sheet_inputs,headers=sheety_header)

    print(sheet_response.text)
# APP_ID = os.environ.get["APP_ID"]
# API_KEY = os.environ.get["API_KEY"]