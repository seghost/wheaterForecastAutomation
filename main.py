import requests

apiKey = "Place your openWeather API key here"
cityName = "Chicago"
amountOfResults = 1
geoData = None
weatherData = None

geoUrl = f"http://api.openweathermap.org/geo/1.0/direct?q={cityName}&limit={amountOfResults}&appid={apiKey}"

response = requests.get(geoUrl)

if response.status_code == 200:
    geoData = response.json()
    print(geoData)
else:
    print("Request failed with status code: ", response.status_code)

Url = f"https://api.openweathermap.org/data/2.5/weather?lat={geoData[0]['lat']}&lon={geoData[0]['lon']}&appid={apiKey}&units=metric"

response = requests.get(Url)

if response.status_code == 200:
    weatherData = response.json()
    print(f"Weather in {cityName} is " + weatherData['weather'][0]['description'] + f" and the temperature is {weatherData['main']['temp']}º celsius")
else:
    print("Request failed with status code: ", response.status_code)
