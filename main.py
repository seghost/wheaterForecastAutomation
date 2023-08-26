import requests

apiKey = "Insert your OpenWeather API key here"
cityName = "Canada"
amountOfResults = 1


def get_geo_data(cityname, amount_of_results, api_key):
    geoUrl = f"http://api.openweathermap.org/geo/1.0/direct?q={cityname}&limit={amount_of_results}&appid={api_key}"
    response = requests.get(geoUrl)
    if response.status_code == 200:
        return response.json()
    else:
        print("Geo Data request failed with status code: ", response.status_code)


def get_weather_data(lat, lon, api_key):
    weatherUrl = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(weatherUrl)
    if response.status_code == 200:
        return response.json()
    else:
        print("Weather Data request failed with status code: ", response.status_code)


geoData = get_geo_data(cityName, amountOfResults, apiKey)
weatherData = get_weather_data(geoData[0]['lat'], geoData[0]['lon'], apiKey)

print(geoData)
print(f"Weather in {cityName} is " + weatherData['weather'][0]['description'] + f" and the temperature is {weatherData['main']['temp']}º celsius whit a humidity of {weatherData['main']['humidity']}%")