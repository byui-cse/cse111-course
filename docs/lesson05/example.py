# example.py
# Copyright 2020, Brigham Young University - Idaho. All rights reserved.

def wind_chill(temperature, wind_speed):
    """Compute and return the wind chill factor as defined by the US
    National Weather Service.

    Parameters
        temperature: the air temperature in Fahrenheit at five feet
            above the ground.
        wind_speed: the spead of the wind in miles per hour at five feet
            above the ground.
    Return: The wind chill factor in degrees Fahrenheit.
    """
    chill_factor = 35.74 \
        + 0.6215 * temperature \
        - 35.75 * wind_speed**0.16 \
        + 0.4275 * temperature * wind_speed**0.16
    rounded = round(chill_factor, 1)
    return rounded


def heat_index(temperature, humidity):
    """Compute and return the heat index as defined by the US National
    Wather Service.

    Parameters
        temperature: the air temperature in Fahrenheit at five feet
            above the ground.
        humidity: the relative humidity of the air at five feet above
            the ground.
    Return: The heat index in degrees Fahrenheit.
    """
    index = -42.379 \
        + 2.04901523 * temperature \
        + 10.14333127 * humidity \
        - 0.22475541 * temperature * humidity \
        - 0.00683783 * temperature**2 \
        - 0.05481717 * humidity**2 \
        + 0.00122874 * temperature**2 * humidity \
        + 0.00085282 * temperature * humidity**2 \
        - 0.00000199 * temperature**2 * humidity**2
    rounded = round(index, 1)
    return rounded


def cels_from_fahr(fahr):
    """Convert a temperature in Fahrenheit to
    Celsius and return the Celsius temperature.
    """
    cels = (fahr - 32) * 5 / 9
    return cels


def fahr_from_cels(cels):
    """Convert a temperature in Celsius to
    Fahrenheit and return the Fahrenheit temperature.
    """
    fahr = cels * 9 / 5 + 32
    return fahr
