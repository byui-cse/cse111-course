def full_name(given_name, family_name):
	"""Return a string in this form 'family_name, given_name'.
	For example, if this function were called like this:
	full_name("Sally", 'Brown"), it would return "Brown, Sally".
	"""
	return family_name + "," + given_name


def given_name(full_name):
	"""Extract and return the given name from a
	string in this form 'family_name, given_name'.
	For example, if this function were called like this:
	given_name("Brown, Sally"), it would return "Sally".
	"""
	comma = full_name.find(", ")
	return full_name[comma + 1:]


def family_name(full_name):
	"""Extract and return the family name from a
	string in this form 'family_name, given_name'.
	For example, if this function were called like this:
	family_name("Brown, Sally"), it would return "Brown".
	"""
	comma = full_name.find(", ")
	return full_name[0:comma]
