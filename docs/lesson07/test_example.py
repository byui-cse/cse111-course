from weather import wind_chill, heat_index
from pytest import approx
import pytest

def test_wind_chill():
    assert wind_chill(0, 3) == approx(-6.9)
    assert wind_chill(-5, 5) == approx(-16.4)
    assert wind_chill(-10, 3) == approx(-18.2)


def test_heat_index():
    assert heat_index(80, 80) == approx(84.2)
    assert heat_index(85, 80) == approx(96.8)
    assert heat_index(96, 70) == approx(126.4)


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=no", "test_weather.py"])
