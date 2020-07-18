from datetime import datetime, timedelta
import requests

# qcode is short for Quandl Code and is the code that determines
# what data will be downloaded from Quandl by the http request.
qcode = "ODA/PWOOLC_USD"

# This is the uniform resource locator (URL)
# where this program will send an http request.
endpoint = f"https://www.quandl.com/api/v3/datasets/{qcode}.json"

# These are the start and end dates for the data request. The start date
# will be about 13 months before today, and the end date will be today.
end = datetime.today()
start = end - timedelta(days=13*30)

# Arguments that focus the http data request.
args = {
    # The API key should remain private. Do not save
    # it to a public repository or public web site.
    "api_key" : "The API key is in your I-Learn course.",

    "start_date" : start.strftime("%Y-%m-%d"),
    "end_date" : end.strftime("%Y-%m-%d"),
    "collaspe" : "monthly",
    "order" : "asc"
}

# Request the commodities data from Quandl.
response = requests.get(endpoint, params=args)

# Check the status code to see if the request succeeded.
if response.status_code == 200:
    # The request succeeded. Print the qcode so that
    # the user knows which commodity the prices are for.
    print(qcode)

    # Convert the price data from JSON to a Python dictionary.
    data_dict = response.json()

    # Print the price data that Quandl returned to us.
    dataset = data_dict["dataset"]
    print(dataset["name"])
    print(dataset["start_date"], dataset["end_date"])
    print(dataset["column_names"])
    data = dataset["data"]
    for datum in data:
        print(datum)
else:
    # The request failed, so print the status code.
    print("Request failed with status code:", response.status_code)
