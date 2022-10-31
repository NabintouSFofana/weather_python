import requests

API_KEY = "ba28b5c869dc505ba6f85fdb2c47cdb3"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

# send a request
response = requests.get(request_url)

# check the status of the response
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15)
    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("An error occurred")