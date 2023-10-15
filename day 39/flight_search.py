
import requests
search_url='https://tequila-api.kiwi.com/locations/query'
# search_header={
#     'apikey':'39aoTW6_LzvsJXLhZks1QzHAnl0xTgFr'
# }
class FlightSearch:
    def __init__(self) -> None:
        pass
    def update(self,d):
        search_header={
            
           'apikey':'39aoTW6_LzvsJXLhZks1QzHAnl0xTgFr'
        }
        par={
            'term':d['city'],
            'location_types':'airport',
            'limit':1
              
        }
        response=requests.get(url=search_url,headers=search_header,params=par).json()
        itaicode=response['locations'][0]['city']['code']
        d['iataCode']=itaicode
        return d
