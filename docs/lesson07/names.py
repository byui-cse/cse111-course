def full_name(given_name, family_name):
	"""Return a string in this form 'family_name, given_name'"""
	return family_name + "," + given_name


def given_name(full_name):
	"""Extract and return the given name from a
	string in this form 'family_name, given_name'
	"""
	comma = full_name.find(", ")
	return full_name[comma + 1:]


def family_name(full_name):
	"""Extract and return the family name from a
	string in this form 'family_name, given_name'
	"""
	comma = full_name.find(", ")
	return full_name[0:comma]
