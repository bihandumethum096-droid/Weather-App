import requests

def welcome_msg():
    from pyfiglet import Figlet
    f=Figlet(font='slant')
    print(f.renderText('WEATHER APP'))

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

def take_user_input():
    while True:
        city=input('City: ').capitalize()
        country=input('Country: ').capitalize()
        if not city or not country:
            print('please fill both feeds')
        else:
            return (f'{city}, {country}')
            
def quit_or_not():
    while True:
        quit_stat=input('check weather again?(y,n)\n').lower()
        if quit_stat=='y':
            return True
        elif quit_stat=='n':
            return False
        else:
            print('please enter y or n')

def main():
    welcome_msg()
    while True:
        location=take_user_input()
        try:
            lat,long=search_location(location)
            get_weather_info(lat,long)
        except requests.HTTPError:
            print('http request failed')
        except requests.exceptions.Timeout:
            print('connection timed out')
        except requests.ConnectionError:
            print('your internet connection has problems')
        except KeyError:
            print('you have entered an invalid country. please check the country you input')

        if quit_or_not():
            continue
        else:
            print('-----GOOD BYE-----')
            break      

main()