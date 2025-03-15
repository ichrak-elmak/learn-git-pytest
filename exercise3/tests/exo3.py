import pytest
from ..temperature_converter import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin, kelvin_to_celsius
def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32.0
def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0.0
def test_celsius_to_kelvin():
    assert celsius_to_kelvin(0) == 273.15
def test_kelvin_to_celsius():
    assert kelvin_to_celsius(273.15) == 0.0
    with pytest.raises(ValueError):
        kelvin_to_celsius(-1)