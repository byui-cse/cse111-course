# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

def extract_city(full_address):
    """Extract and return the name of a city from
    a properly formatted U.S. mailing address.
    Parameter
        full_address: a U.S. mailing address in this format:
            number and street, city, state zipcode
    Return: the city name
    """
    full_address = full_address.strip()
    last_comma_index = full_address.rindex(",")
    mid_comma_index = full_address.rindex(",", 0, last_comma_index)
    city = full_address[mid_comma_index + 1 : last_comma_index]
    city = city.strip()
    return city


def extract_state(full_address):
    """Extract and return the two letter abbreviation for
    a state from a properly formatted U.S. mailing address.
    Parameter
        full_address: a U.S. mailing address in this format:
            number and street, city, state zipcode
    Return: the two letter state abbreviation
    """
    full_address = full_address.strip()
    last_comma_index = full_address.rindex(",")
    last_space_index = full_address.rindex(" ")
    state = full_address[last_comma_index + 1 : last_space_index]
    state = state.strip()
    return state


def extract_zipcode(full_address):
    """Extract and return the ZIP code from
    a properly formatted U.S. mailing address.
    Parameter
        full_address: a U.S. mailing address in this format:
            number and street, city, state zipcode
    Return: the ZIP code
    """
    full_address = full_address.strip()
    last_space_index = full_address.rindex(" ")
    zipcode = full_address[last_space_index + 1 : ]
    return zipcode
