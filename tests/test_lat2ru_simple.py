import pytest
from translitua.translit import translit, Lat2RuSimple

@pytest.mark.parametrize("latin,expected", [
    ("Shchuka", "Щука"),
    ("Andrey", "Андрей"),
    ("yozh", "ёж"),
    ("shh", "шх"),
    ("e'", "е"),
    ("y'", "й"),
    ("o", "о"),
    ("g", "г"),
    ("sch", "щ"),
    ("ja", "я"),
])
def test_lat2ru_simple(latin, expected):
    assert translit(latin, Lat2RuSimple) == expected
