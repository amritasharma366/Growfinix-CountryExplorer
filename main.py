import requests

API_KEY = "H5pJ5nXxJIUYsygQGA3Uxisuevp7Vzm9G6HmrYfD"

country = input("Enter a country name: ").strip()

# Country Information

headers = {
    "X-Api-Key": API_KEY
}

country_url = f"https://api.api-ninjas.com/v1/country?name={country}"

response = requests.get(country_url, headers=headers)

if response.status_code != 200:
    print("Error fetching country information.")
    exit()

data = response.json()

if not data:
    print("Country not found.")
    exit()

country_data = data[0]

country_name = country_data["name"]
capital = country_data["capital"]
population = country_data["population"]
region = country_data["region"]
currency = country_data["currency"]["name"]

# Get Coordinates of the Capital

geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={capital}&count=1"

geo_response = requests.get(geo_url)

if geo_response.status_code != 200:
    print("Unable to locate capital city.")
    exit()

geo_data = geo_response.json()

if "results" not in geo_data:
    print("Capital city not found.")
    exit()

latitude = geo_data["results"][0]["latitude"]
longitude = geo_data["results"][0]["longitude"]

# Get Weather

weather_url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
)

weather_response = requests.get(weather_url)

if weather_response.status_code != 200:
    print("Unable to fetch weather.")
    exit()

weather_data = weather_response.json()

current = weather_data["current"]

temperature = current["temperature_2m"]
humidity = current["relative_humidity_2m"]
wind_speed = current["wind_speed_10m"]

# Display

print("\n========================================")
print("        COUNTRY EXPLORER")
print("========================================")

print(f"Country      : {country_name}")
print(f"Capital      : {capital}")
print(f"Region       : {region}")
print(f"Population   : {int(population * 1000):,}")
print(f"Currency     : {currency}")

print(f"\n------ Current Weather in {capital} ------")

print(f"Temperature  : {temperature} °C")
print(f"Humidity     : {humidity}%")
print(f"Wind Speed   : {wind_speed} km/h")

print("========================================")