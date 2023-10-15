SHEETY_PRICES_ENDPOINT='https://api.sheety.co/0f5c956ffe3d6786037d2a4b7fb4665b/copyOfFlightDeals/prices/'
import requests
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        
        self.response=requests.get("https://api.sheety.co/0f5c956ffe3d6786037d2a4b7fb4665b/copyOfFlightDeals/prices").json()
        self.data=self.response
    def update_sheet(self):
        for city in self.data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

