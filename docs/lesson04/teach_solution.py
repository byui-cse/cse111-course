import requests

# This is the uniform resource locator (URL)
# where this program will send an http request.
url = "https://swapi.co/api/planets/"

# Request the planet data from swapi.co
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
	total = 0

	# The planets are numbered from 1 to count, inclusive.
	for i in range(1, count+1):
		# Create the URL to get the data for a planet.
		url = f"https://swapi.co/api/planets/{i}"

		# Get the data for a planet.
		response = requests.get(url)

		if response.status_code == 200:
			data = response.json()
			text = data["population"]
			print(data["name"], text)

			# The population of some planets is unknown, so we must
			# check to see if the population is a number before
			# converting it to an integer and adding it to the total.
			if text.isnumeric():
				population = int(text)
				total += population

	# Print the total population.
	print(total)
else:
	# If the request was not successful, print the status code.
	print(response.status_code)
