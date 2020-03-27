import pandas as pd

def main():
    # Read file
    data = pd.read_csv("readings.csv",
            dtype={"meterNumber":"str",
                "priorReadDate":"str", "readDate":"str",
                "startRead":"int_", "endRead":"int_",
                "stubSize":"single", "numberOfDwellings":"int_",
                "accountNumber":"str", "accountType":"str"
            },
            parse_dates=["priorReadDate", "readDate"])
    print(data)

    data.sort_values(["accountType", "accountNumber"], inplace=True)
    print(type(data))
    print(data)

    print()
    print(type(data.iloc[3]))
    print(data.iloc[3])
    print()
    print(type(data.loc[3]))
    print(data.loc[3])

    # Causes an error
    #print(data.loc["priorReadDate"])

    print()
    print(type(data["priorReadDate"]))
    print(data["priorReadDate"])

#    print(data.iloc[3]["priorReadDate"])
#    print(data.loc[3, "priorReadDate"])
#    print(data["priorReadDate"][3])

#    data.sort_values(["meterNumber", "readDate"], inplace=True)

    # Print all readings from meter number 1007023238.
#    meter1007023238 = data.query("meterNumber == '1007023238'")
#    print(meter1007023238)

    # Print all readings from schools.
#    print(data.query("accountType == 'School'"))

#    print(sorted(data["accountType"].unique().tolist()))


main()
