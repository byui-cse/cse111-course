"""Write U.S. National Weather Service forecasts to an HTML file

To successfully use this module to write an HTML file, your code must
first retrieve a weather forecast from the US National Weather Service.
The weather service organizes a weather forecast into periods of time.
Each period covers about 12 hours and is either a day, an afternoon, or
a night.

After your code retrieves the periods, it should call these functions
from this module:

1. weather_html.create_report - must be called once before the other
functions.
2. weather_html.start_new_row - must be called once at the beginning of
each desired row of periods.
3. weather_html.add_period - must be called once for each period in the
current row.
4. weather_html.write_report - must be called once after your code has
added all desired rows and periods.
"""

import math


# Option Constants
PERIOD_NAME = "name"
TEMPERATURE = "temperature"
WIND = "wind"
ICON = "icon"
SHORT_FORECAST = "shortForecast"
DETAILED_FORECAST = "detailedForecast"


def create_report(filename, locname,
		options=[PERIOD_NAME, TEMPERATURE, SHORT_FORECAST]):
	"""Create and return a weather report that will be used for adding
	rows and periods and then writing the report.

	param filename: path and name of the HTML file where this module
		will write the weather forecasts.
	param locname: name of the geographic location (city) where the
		forecasts apply.
	param options: a list of weather forecast data that the user desires
		to be written in a report.
	"""
	return {
		"filename" : filename,
		"location" : locname,
		"options" : options,
		"rows" : []
	}


def start_new_row(report):
	"""Add one row to the weather report."""
	report["rows"].append([]);


def add_period(report, period):
	"""Add one period to the current row in the weather report."""
	report["rows"][-1].append(period)


def write_report(report):
	"""Write the weather report to an HTML file."""

	# Determine the maximum number of columns for all rows.
	max_cols = max([len(row) for row in report["rows"]])

	# Compute the column width as a percentage and
	# round down to the nearest tenth of one percent.
	col_width = 100 / max_cols
	col_width = math.floor(col_width * 10) / 10

	with open(report["filename"], "wt") as outfile:

		# Write the HTML document head and start of the body.
		outfile.write(
f'''<!DOCTYPE HTML>
<html lang="en-us">
	<head>
		<meta charset="utf-8">
		<title>U.S. National Weather Service Forecast</title>
		<style>
			td {{ width: {col_width}%; vertical-align: top; }}
			td.img {{ text-align: center; }}
		</style>
	</head>
	<body>
		<h2>U.S. National Weather Service Forecast</h2>
		<h1>{report["location"]}</h1>
		<table>
''')

		# Write each of the rows.
		options = report["options"]
		for row in report["rows"]:
			write_row(outfile, row, options, max_cols)

		# Write the end of the HTML document.
		outfile.write(
'''		</table>
	</body>
</html>
''')


# Writer functions that write various parts of a period to an HTML file.
def write_period_name(out, period):
	name = period[PERIOD_NAME]
	out.write(f"\t\t\t\t<th>{name}</th>\n")

def write_temperature(out, period):
	name = "High" if period["isDaytime"] else "Low"
	temp = str(period[TEMPERATURE]) + period["temperatureUnit"]
	out.write(f"\t\t\t\t<td>{name}: {temp}</td>\n")

def write_wind(out, period):
	wind = str(period["windSpeed"]) + " out of the " \
			+ period["windDirection"]
	out.write(f"\t\t\t\t<td>Wind: {wind}</td>\n")

def write_icon(out, period):
	src = period[ICON]
	alt = period[SHORT_FORECAST]
	out.write(f'\t\t\t\t<td class="img"><img alt="{alt}" title="{alt}" src="{src}"></td>\n')

def write_short_forecast(out, period):
	forecast = period[SHORT_FORECAST]
	out.write(f"\t\t\t\t<td>{forecast}</td>\n")

def write_detailed_forecast(out, period):
	forecast = period[DETAILED_FORECAST]
	out.write(f"\t\t\t\t<td>{forecast}</td>\n")

WRITERS = {
	PERIOD_NAME : write_period_name,
	TEMPERATURE : write_temperature,
	WIND : write_wind,
	ICON : write_icon,
	SHORT_FORECAST : write_short_forecast,
	DETAILED_FORECAST : write_detailed_forecast
}

def write_row(out, periods, options, max_cols):
	"""Write one row of periods to the HTML file."""

	tr = "\t\t\t<tr>\n"
	_tr = "\t\t\t</tr>\n"
	empty_cell = "\t\t\t\t<td>&nbsp;</td>\n"
	empties = max_cols - len(periods)

	for option in options:
		# Write an opening <tr> tag to the HTML file.
		out.write(tr)

		# Find the writer function that corresponds to the current option.
		write_part = WRITERS[option]

		for period in periods:
			if len(period) > 0:
				# Call the writer function which will write to
				# the HTML file a piece of data from a period.
				write_part(out, period)
			else:
				out.write(empty_cell)

		# Write empty cells as needed.
		for _ in range(empties):
			out.write(empty_cell)

		# Write an closing </tr> tag to the HTML file.
		out.write(_tr)


__all__ = [create_report, start_new_row, add_period, write_report]
