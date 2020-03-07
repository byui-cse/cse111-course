from names import given_name, family_name, full_name

def test_full_name():
	"""Verify that the full_name function returns correct results."""
	assert full_name("Penelope", "Smith-Jones") == "Smith-Jones, Penelope"
	assert full_name("George", "Washington") == "Washington, George"
	assert given_name("J", "Ng") == "Ng, J"
	assert full_name("", "") == ", "

def test_given_name():
	"""Verify that the given_name function returns correct results."""
	assert given_name("Smith-Jones, Penelope") == "Penelope"
	assert given_name("Washington, George") == "George"
	assert given_name("Ng, J") == "J"
	assert given_name(", ") == ""

def test_famliy_name():
	"""Verify that the family_name function returns correct results."""
	assert family_name("Smith-Jones, Penelope") == "Smith-Jones"
	assert family_name("Washington, George") == "Washington"
	assert family_name("Ng, J") == "Ng"
	assert family_name(", ") == ""
