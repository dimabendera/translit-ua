import pytest
from translitua.translit import translit, Lat2UkrWWS

@pytest.mark.parametrize("latin,expected", [
    ("šč", "щ"),
    ("ž", "ж"),
    ("č", "ч"),
    ("š", "ш"),
    ("ju", "ю"),
    ("ja", "я"),
    ("je", "є"),
    ("ji", "ї"),
    ("x", "х"),
    ("a", "а"),
    ("b", "б"),
])
def test_lat2ukr_wws(latin, expected):
    assert translit(latin, Lat2UkrWWS) == expected
