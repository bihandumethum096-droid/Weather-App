import requests,weatherAPI
from pyfiglet import Figlet

def welcome_msg():
    f=Figlet(font='slant')
    print(f.renderText('WEATHER APP'))

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
            lat,long=weatherAPI.search_location(location)
            weatherAPI.get_weather_info(lat,long)
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
                    
if __name__=="__main__":
    main()