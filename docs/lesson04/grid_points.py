import requests

print(
"""Weather forecasts from the U.S. National Weather Service are divided
into 2.5 km grids. In order to get a forecast, an application must
specify a desired grid. This program will convert a location in decimal
latitude and longitude into US NWS grid coordinates.""")

lat = float(input("Enter a decimal latitude [-90, 90]: ").strip())
lng = float(input("Enter a decimal longitude [-180, 180]: ").strip())

# Request the grid points from the U.S. National Weather Service.
url = f"https://api.weather.gov/points/{lat},{lng}"
response = requests.get(url)

# Check the status code to see if the request succeeded.
if response.status_code == 200:
    # The request succeeded, so get the city,
    # state, and forecast URL from the response.
    data = response.json()["properties"]

    # Check to see if the response contains city and
    # state information. The city and state information
    # is inside several levels of dictionaries.
    if data["relativeLocation"] and \
            data["relativeLocation"]["properties"] and \
            data["relativeLocation"]["properties"]["city"] and \
            data["relativeLocation"]["properties"]["state"]:
        city = data["relativeLocation"]["properties"]["city"]
        state = data["relativeLocation"]["properties"]["state"]
        print(f"{city}, {state}")

    forecast_url = data["forecast"]
    print(forecast_url)

else:
    # The request failed, so print the status code.
    print("Request failed with status code:", response.status_code)
