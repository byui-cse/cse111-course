from datetime import datetime, timedelta
import requests

qcode = "ODA/PWOOLC_USD"
print(qcode)
url = f"https://www.quandl.com/api/v3/datasets/{qcode}.json"

end = datetime.today()
start = end - timedelta(days=13*31)
args = {
	"start_date" : start.strftime("%Y-%m-%d"),
	"end_date" : end.strftime("%Y-%m-%d"),
	"collaspe" : "daily",
	"order" : "asc"
}

# Request the commodities data from Quandl.
response = requests.get(url, params=args)

if response.status_code == 200:
	# If the request was succesful, print
	# the data that Quandl returned to us.
	dataset = response.json()["dataset"]
	print(dataset["name"])
	print(dataset["start_date"], dataset["end_date"])
	print(dataset["column_names"])
	data = dataset["data"]
	for datum in data:
		print(datum)
else:
	# If the request was not successful, print the status code.
	print(response.status_code)
