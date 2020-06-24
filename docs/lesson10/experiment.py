import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
import pandas as pd

def main():
    # Read the water.csv file and convert the
    # readDate column from a string to a datetime64.
    data = pd.read_csv("../lesson09/water.csv",
            dtype={"meterNumber":"str",
                "readDate":"str", "numberOfDays":"int_",
                "reading":"int_", "usage":"int_",
                "accountType":"str", "numberOfDwellings":"int_"
            },
            parse_dates=["readDate"])

    show_meter_size_hist(data)
    show_size_usage_scatter(data)
    plt.show()
    return

    show_meter_usage(data, "M4086", "2015-01-01", "2016-12-31")
    show_meter_usage(data, "M4103", "2016-01-01", "2017-12-31")
    show_comparison(data, "M4103", "2016-01-01", "2017-12-31")
    plt.show()
    return

    #show_number_of_days_box_plot(data, ["M1000", "M1001", "M1003"])
    plt.show()
    return

    # Add a column that contains just the year of the read date.
    data["year"] = data["readDate"].dt.year

    first = data[["accountType", "usage"]]
    first = first.groupby("accountType").aggregate(sumUsage=("usage", "sum"))
    first.plot()

    second = data[["year", "usage"]]
    second = second.groupby("year").aggregate(sumUsage=("usage", "sum"))
    second.plot()

    third = data[["meterNumber", "usage", "accountType"]]
    third = third[third["accountType"]
                .isin(["Business", "Business with Apartment"])]
    third = third.groupby("meterNumber").aggregate(sumUsage=("usage", "sum"))
    third.plot()

    plt.show()


def show_meter_size_hist(data):
    # Keep only the meterNumber and meterSize columns.
    #ms = data[["meterNumber", "meterSize"]]
    #unique = ms.drop_duplicates()
    #unique.plot.hist(bins=32)
    #plt.tight_layout()

    dow = data["readDate"].dt.day
    dow.plot.hist(bins=31)  # *
    plt.tight_layout()

def show_size_usage_scatter(data):
    #data.plot.scatter(x="meterSize", y="usage")  # *
    #data.plot.scatter(x="accountType", y="usage")
    #data.plot.scatter(x="numberOfDays", y="usage")
    #data["usagePerDay"] = data["usage"] / data["numberOfDays"]
    #data.plot.scatter(x="meterSize", y="usagePerDay")  # *
    #data.plot.scatter(x="numberOfDays", y="usage")  # *

    # Box plot seems to be buggy and offer nothing
    # that can't be done with a scatter plot.
    #data[["accountType", "usage"]].plot.box(column="usage", by="accountType")
    plt.tight_layout()


def show_number_of_days_box_plot(data, meters):
    # Keep only the rows for the specified meters.
    data = data[data["meterNumber"].isin(meters)]

    # Keep only the meterNumber and numberOfDays columns.
    data = data[["meterNumber", "numberOfDays"]]

    data.plot.box(by="meterNumber")


def filter_for_meter(data, meter):
    # Keep only the rows with the specified meter number.
    filtered = data[data["meterNumber"] == meter]
    return filtered


def filter_for_account_type(data, actype):
    # Keep only the rows with the specified account type.
    filtered = data[data["accountType"] == actype]
    return filtered


def filter_between_dates(data, start, end):
    # Keep only the rows between the start and end dates.
    filtered = data[(data["readDate"] >= start) & (data["readDate"] <= end)]
    return filtered


def add_usage_median_column(data):
    data = add_year_month_column(data)
    columns = data.columns.tolist()

    # Find the median usage value grouped by accountType and yearMonth.
    medians = data.groupby(["accountType", "yearMonth"]) \
            .aggregate(medianUsage=("usage", "median"))

    # Change the index so that joining the
    # medians with the original data will work.
    data = data.set_index(["accountType", "yearMonth"])

    # Join the original data and the medians.
    joined = data.join(medians)

    # The join sorts the data by the join key, which is a
    # different order than the CSV file, so sort the rows by
    # meterNumber and readDate like the CSV file, and then reset
    # the index as if the data were just read from the CSV file.
    joined.sort_values(["meterNumber", "readDate"], inplace=True)
    joined.reset_index(drop=False, inplace=True)

    # Reorder the columns to be similar to the CSV file.
    insert_column_name(columns, "usage", "medianUsage")
    joined = joined[columns]

    print(joined.dtypes)
    return joined


def add_year_month_column(data):
    # Add to the DataFrame a column that contains
    # only the year and the month of the readDate.
    if "yearMonth" not in data:
        columns = data.columns.tolist()
        data["yearMonth"] = data["readDate"].dt.to_period("M")
        data.astype({"yearMonth":"period[M]"}, copy=False, errors="raise")
        insert_column_name(columns, "readDate", "yearMonth")
        data = data[columns]
    return data


def insert_column_name(columns, prev, colname):
    index = columns.index(prev)
    if index > 0:
        index += 1
    columns.insert(index, colname)


def show_meter_usage(data, meter, start, end):
    indiv = filter_for_meter(data, meter)
    indiv = filter_between_dates(indiv, start, end)
    indiv = add_year_month_column(indiv)

    barplot = indiv.plot.bar(x="yearMonth", y="usage", legend=False)
    barplot.set_title(f"Water Usage for Meter #{meter}")
    barplot.set_xlabel("")
    barplot.set_ylabel("x1000 gallons")
    plt.tight_layout()


def show_comparison(data, meter, start, end):
    data = add_usage_median_column(data)

    indiv = filter_for_meter(data, meter)
    indiv = filter_between_dates(indiv, start, end)

    # Keep only the "yearMonth", "usage", and "medianUsage" columns.
    indiv = indiv[["yearMonth", "usage", "medianUsage"]]

    # Rename "medianUsage" to just "median".
    indiv.rename(columns={"medianUsage":"median"},
            copy=False, inplace=True, errors="raise")

    # Set the yearMonth column as the index. By default,
    # a line plot places the index on the x-axis.
    indiv.set_index("yearMonth", inplace=True)

    # Define a line plot with the usage and the median usage.
    lineplot = indiv.plot.line()
    lineplot.set_title(f"Water Usage for Meter #{meter}")
    lineplot.set_xlabel("")
    lineplot.set_ylabel("x1000 gallons")
    plt.tight_layout()


main()
