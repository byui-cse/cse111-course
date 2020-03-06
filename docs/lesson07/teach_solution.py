from names import given_name, family_name, full_name

def test_full_name():
	assert full_name("Penelope", "Smith-Jones") == "Smith-Jones, Penelope"
	assert full_name("George", "Washington") == "Washington, George"
	assert full_name("", "") == ", "

def test_given_name():
	assert given_name("Smith-Jones, Penelope") == "Penelope"
	assert given_name("Washington, George") == "George"
	assert given_name(", ") == ""

def test_famliy_name():
	assert family_name("Smith-Jones, Penelope") == "Smith-Jones"
	assert family_name("Washington, George") == "Washington"
	assert family_name(", ") == ""
