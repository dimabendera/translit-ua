import pytest
from translitua.translit import translit, Lat2RuISO9SystemB

@pytest.mark.parametrize("latin,expected", [
    ("shh", "щ"),
    ("e'", "э"),
    ("y'", "ы"),
    ("yo", "ё"),
    ("yu", "ю"),
    ("ya", "я"),
    ("a", "а"),
    ("b", "б"),
    ("x", "х"),
    ("cz", "ц"),
])
def test_lat2ru_iso9systemb(latin, expected):
    assert translit(latin, Lat2RuISO9SystemB) == expected
