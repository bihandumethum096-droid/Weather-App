import requests

def get_weather_info(latitude,longitude):   
    url = "https://api.open-meteo.com/v1/forecast"
    parameters = {
	"latitude": latitude,
	"longitude": longitude,
	"current": ["temperature_2m","rain","is_day",
               "wind_speed_10m","apparent_temperature","relative_humidity_2m"],
    "timezone":"auto"}
    
    response=requests.get(url,params=parameters,timeout=(5,10))
    response.raise_for_status()
    content=response.json()
    for result in content['current']:
        if result=='interval':
            continue
        print(f'* {result} => {content["current"][result]}')


def search_location(location):
    url='https://geocoding-api.open-meteo.com/v1/search?'
    parameters={
        'name':location,
        'count':'1',
        'language':'en',
        'format':'json'
                        }

    response=requests.get(url,params=parameters,timeout=(5,10))                        
    response.raise_for_status()
    content=response.json()
    info=content['results'][0]
    co_ordinates=info['latitude'],info['longitude']
    return (co_ordinates)

