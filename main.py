import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

apiKey = "Insert your OpenWeather API key here"
cityName = "Buenos Aires"
amountOfResults = 1

driver = webdriver.Chrome()


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
driver.get("https://www.accuweather.com/")

wait = WebDriverWait(driver, 10)

inptBox = wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@name='query']")))
inptBox.click()
inptBox.send_keys(cityName)
time.sleep(2)

searchResults = driver.find_element(By.XPATH, "//div[@class='results-container']")
result = searchResults.find_element(By.XPATH, f"//div[@class='search-bar-result search-result']")
wait.until(ec.presence_of_element_located((By.XPATH, f"//div[@class='search-bar-result search-result']")))

result.click()

referenceTemp = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@class='temp']")))
details = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@class='phrase']")))




print(geoData)
print(f"Weather in {cityName} is " + weatherData['weather'][0]['description'] + f" and the temperature is {weatherData['main']['temp']}ºC")
print(f"Weather in {cityName} from the reference website accuweather is {details.text} the temperature  is {referenceTemp.text}")


