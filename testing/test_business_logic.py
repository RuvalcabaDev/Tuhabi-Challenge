import pytest
from business_logic import find_properties
from schemas import PropertiesRequestModel


@pytest.mark.parametrize(
    "city, year, expected",
    {
        ('cali','', 2)
    }
)
def test_find_properties_multi(city, year, expected):
    assert find_properties(city, year) == expected
