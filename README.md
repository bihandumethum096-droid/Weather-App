# Weather-App

## ABOUT   

- This is a simple weather app with a Command-line interface. This application can input location details from the user and output the current date-time, day-night status and the current weather information such as the apparent temperature,temperature at 2m,rainfall(in millimetres),wind speed and relative humidity of the location that the user has provided.

## FEATURES

- This application can take a location as a user input.
- This program displays the following information about weather.
        
    - Temperature at 2 metres
    - Apparent temperature
    - Rainfall (in millimetres)
    - Current date-time
    - Current wind speed
    - Relative humidity
    - Day-night status

- Weather application displays a welcome message when the user starts it, and displays a greeting when the user decides to exit.

## TECHNOLOGIES USED

- Python programming language
- Pyfiglet package
- Requests package
- Open-Meteo weather forecast API
- Open-Meteo geolocation API

## INSTALLATION

- To use this application, you would have to install the following beforehand
    
    - Python interpreter
    - Suitable text editor
    - Pyfiglet package
    - Requests package
- Make sure that weather_api.py and weather_main.py are in the same directory, as weather_main.py imports weather_api.py as a module.
## USAGE

- Once you have set the installations up, run the code using python interpreter and the text editor.
- You will be greeted by a welcome message and prompted for a city and country.
- Enter the city name and the country name that you want to check the weather and press enter
- The program will display the current weather information for the location you gave before
- The program will ask if you need to  check the weather again. if you want, press y. otherwise, press n.
- Once you want to exit the program, you will be greeted by a greeting message

## FUTURE IMPROVEMENTS

- Possible future improvements include

    - Better way to handle errors
    - Displaying a weather forecast instead of just current weather information
    - Using a GUI instead of a Command-line interface