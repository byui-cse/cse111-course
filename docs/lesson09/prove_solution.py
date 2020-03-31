import matplotlib.pyplot as plot
import pandas as pd

def main():
    # Read file
    data = pd.read_csv("readings.csv",
            dtype={"meterNumber":"str",
                "readDate":"str", "numberOfDays":"int_",
                "reading":"int_", "usage":"int_",
                "accountType":"str", "numberOfDwellings":"int_"
            },
            parse_dates=["readDate"])
    #print(data[data["usage"] > 10000][["meterNumber", "usage", "accountType"]])

    print(data["usage"].count())
    print(data.dtypes)
    #print(data.describe())
    #print(len(data["meterNumber"].unique()))
    #print(sorted(data["accountType"].unique().tolist()))

    data["year"] = data["readDate"].dt.year
    data["month"] = data["readDate"].dt.month
    #data["monthYear"] = data["readDate"].dt.to_period("M")
    print(data.dtypes)
    print(data[["readDate", "year", "month"]])

    data2014 = data[data["year"] == 2013]
    data2014 = data2014[data["accountType"]
            .isin(["Residence", "Apartment Complex"])]
    print(data2014["usage"].count())
    print(data2014.groupby(["month"]).groups.keys())
    print(data2014.groupby(["accountType", "month"])[["usage"]].sum())
    return
    data["usagePerDay"] = data["usage"] / data["numberOfDays"]

    ss = data.groupby(["meterNumber","stubSize"]).size().reset_index()["meterNumber","stubSize"]
    print(ss)
    return
    ss = data[["meterNumber","stubSize"]].unique()
    print(ss)
    return
    ss.plot.hist(by="meterNumber", bins=100)
    ss.plot.hist(by="meterNumber", bins=40)

    data[data["usage"] > 0][data["usage"] < 250][["usage"]].plot.hist(bins=100)

    gb = ss.groupby(by=["meterNumber"], axis=1)
    print(gb)
    gb.plot.hist(by="meterNumber", bins=100)

    plot.show()
    return

    plot.show()
    data["stubSize"].hist(by=data["meterNumber"])
    plot.show()

    print(data)
    data.sort_values(["accountType", "accountNumber"], inplace=True)
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
    print(data[data["meterNumber"] == "1007023238"])

    # Print all readings from schools.
#    print(data.query("accountType == 'School'"))
    print(data[data["accountType"] == "School"])

#    print(sorted(data["accountType"].unique().tolist()))

#    data.plot.hist()


main()


# According to the water meter reading data, how many residence
# dwellings existed in 2014?
# How many apartment dwellings existed in 2014?
# Which account type used the most water in 2014?

# In which month do apartments use the most water?
# In which month do residences use the most water?
# How much total water was used in 2010, 2011, 2012, 2013, 2014
