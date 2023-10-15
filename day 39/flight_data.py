import requests
import datetime
class FlightData:
    def __init__(self):
        self.departurecity='LON'
        
    def price(self,d):
        arrival_city=d['iataCode']    
        datefrom="23/01/2022"
        dateTo="22/05/2022"
        curr='GBP'
        price_header={
            'apikey':'39aoTW6_LzvsJXLhZks1QzHAnl0xTgFr'
        }
        par={
            'fly_from':self.departurecity,
            'fly_to':arrival_city,
            'date_from':datefrom,
            'date_to':dateTo,
            'curr':curr
        }
        response=requests.get(url='https://tequila-api.kiwi.com/v2/search',headers=price_header,params=par)
        result=response.json()
        return result