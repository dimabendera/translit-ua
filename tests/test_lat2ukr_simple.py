import pytest
from translitua.translit import translit, Lat2UkrSimple

@pytest.mark.parametrize("latin,expected", [
    ("Kharkiv", "Харків"),
    ("shch", "щ"),
    ("zh", "ж"),
    ("kh", "х"),
    ("ts", "ц"),
    ("ch", "ч"),
    ("sh", "ш"),
    ("ju", "ю"),
    ("ja", "я"),
    ("ye", "є"),
    ("yi", "ї"),
    ("Don't", "Донт"),
    ("qz", "кз"),
])
def test_lat2ukr_simple(latin, expected):
    assert translit(latin, Lat2UkrSimple) == expected
