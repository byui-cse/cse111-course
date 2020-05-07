# This file contains two different solutions to the team activity
# assignment. The first solution retrieves the data about each planet
# one at a time. The second solution retrieves the data about planets in
# pages of data. A single page of data at swapi.dev contains the data
# for about ten planets.


import requests


# FIRST SOLUTION: Get data about the planets, one planet at a time.

# This is the uniform resource locator (URL)
# where this program will send an http request.
url = "http://swapi.dev/api/planets/"

# Request the planet data from swapi.dev
response = requests.get(url)

# Check the status code to see if the request succeeded.
if response.status_code == 200:
    # If the request was succesful, convert the JSON data
    # from the response into a dictionary named data.
    data = response.json()

    # Get the number of planets from the dictionary.
    count = int(data["count"])

    # For each planet, get the population (if known), and add it
    # to the total population of the known Star Wars universe.
    population = 0

    # Count the number of planets known to have surface water.
    water = 0

    # The planets are numbered from 1 to count, inclusive.
    # Retrieve the data about each planet one at a time.
    for i in range(1, count+1):
        # Create the URL to get the data for a planet.
        url = f"http://swapi.dev/api/planets/{i}"

        # Get the data for a planet.
        response = requests.get(url)

        if response.status_code == 200:
            planet = response.json()

            text_pop = planet["population"]
            text_water = planet["surface_water"]
            print(planet["name"], "pop:", text_pop, "water:", text_water)

            # The population of some planets is unknown, so we must
            # check to see if the population is a number before
            # converting it to an integer and adding it to the total.
            if text_pop.isnumeric():
                pop = int(text_pop)
                population += pop

            if text_water.isnumeric():
                percent = int(text_water)
                if percent > 0:
                    water += 1
        else:
            # If the request was not successful, print the status code.
            print(response.status_code)

    # Print the total population and the number
    # of planets known to have surface water.
    print(f"Population {population}, Water {water}")
    print()
else:
    # If the request was not successful, print the status code.
    print(response.status_code)


# SECOND SOLUTION: Get data about the planets
# in pages (about ten planets in each page).

# This is the uniform resource locator (URL)
# where this program will send an http request.
url = "http://swapi.dev/api/planets/"

population = 0
water = 0
while url != "None":
    # Request a page of planet data from swapi.dev. Each page
    # contains the data for multiple (likely 10) planets.
    response = requests.get(url)

    # Check the status code to see if the request succeeded.
    if response.status_code == 200:
        # If the request was succesful, convert the JSON data
        # from the response into a dictionary named data.
        data = response.json()

        # For each planet, get the population (if known), and add it
        # to the total population of the known Star Wars universe.
        planets = data["results"]
        for planet in planets:
            text_pop = planet["population"]
            text_water = planet["surface_water"]
            print(planet["name"], "pop:", text_pop, "water:", text_water)

            # The population of some planets is unknown, so we must
            # check to see if the population is a number before
            # converting it to an integer and adding it to the total.
            if text_pop.isnumeric():
                pop = int(text_pop)
                population += pop

            if text_water.isnumeric():
                percent = int(text_water)
                if percent > 0:
                    water += 1

        url = str(data["next"]).strip()
    else:
        # If the request was not successful, print the status code.
        print(response.status_code)
        url = "None"

# Print the total population and the number
# of planets known to have surface water.
print(f"Population {population}, Water {water}")
print()
