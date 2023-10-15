#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from tkinter import N
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from flight_data import FlightData
data=DataManager()
flight=FlightSearch()
flight_DATA=FlightData()
sheet_data=(data.response['prices'])
new_data=[]
price=[]
for i in sheet_data:
    new_data.append(flight.update(i))
    city_name=i['city']
    # print(city_name)
    pric=flight_DATA.price(i)['data'][0]['price']
    # price.append({city_name:pric})
    print(f"{city_name}:{pric}")
# print(new_data)    
# data.data=new_data
# data.update_sheet()  
# e=new_data[0]
# print(flight_DATA.price(e)['data'][0])
# print(price)







