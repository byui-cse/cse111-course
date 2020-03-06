from words import prefix, suffix

def test_prefix():
	assert prefix("", "") == ""
	assert prefix("", "correct") == ""
	assert prefix("clear", "") == ""
	assert prefix("happy", "funny") == ""
	assert prefix("cat", "catalog") == "cat"
	assert prefix("dogmatic", "dog") == "dog"
	assert prefix("jump", "joyous") == "j"
	assert prefix("unwise", "ungrateful") == "un"
	assert prefix("Disable", "dIstasteful") == "dis"

def test_suffix():
	assert suffix("", "") == ""
	assert suffix("", "correct") == ""
	assert suffix("clear", "") == ""
	assert suffix("angelic", "awesome") == ""
	assert suffix("found", "profound") == "found"
	assert suffix("ditch", "itch") == "itch"
	assert suffix("happy", "funny") == "y"
	assert suffix("tired", "fatigued") == "ed"
	assert suffix("swimming", "FLYING") == "ing"
