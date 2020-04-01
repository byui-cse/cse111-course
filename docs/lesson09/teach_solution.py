import pandas as pd

#Residence                   128638
#Apartment Complex            53125
#Business                     29626
#Town Homes                    5446
#Out of Town                   2790
#BYU-Idaho                     2170
#Church                        2123
#School                        1838
#Trailer Court                 1752
#City                           886
#Vacant                         634
#Residence with Apartment       541
#Sprinklers                     443
#Business with Apartment        367
#Free                            80
#Unknown                         53
#Airport Hanger                  35
#Name: accountType, dtype: int64

def main():
    # Read the water.csv file and convert the
    # readDate column from a string to a datetime64.
    data = pd.read_csv("water.csv",
            dtype={"meterNumber":"str",
                "readDate":"str", "numberOfDays":"int_",
                "reading":"int_", "usage":"int_",
                "accountType":"str", "numberOfDwellings":"int_"
            },
            parse_dates=["readDate"])

    # Reduce the data to one row per meter.
    acctTypes = data.groupby(["meterNumber", "accountType"])["readDate"].min().reset_index()
    # Count the number of account types.
    print(acctTypes["accountType"].value_counts())

    totalWaterUsed = data["usage"].sum()
    print(totalWaterUsed)

    print(data[data["accountType"] == "Residence"]["usage"].sum())
    print(data[data["accountType"] == "Apartment Complex"]["usage"].sum())

    # Reduce the data to one row per meter.
    dwellings = data.groupby(["meterNumber"])[["numberOfDwellings"]].max().reset_index()

    # Sum the number of dwellings.
    numDwells = dwellings["numberOfDwellings"].sum()
    print(dwellings)
    print(numDwells)

    avgPerDwelling = round(totalWaterUsed / numDwells, 1)
    print(avgPerDwelling)



main()
