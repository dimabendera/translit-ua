import pytest
from translitua.translit import translit, Lat2UkrKMU

@pytest.mark.parametrize("latin,expected", [
    ("BMW", "БМВ"),
    ("Bmw", "Бмв"),
    ("Kharkiv", "Харків"),
    ("boy", "бой"),
    ("busy", "бусй"),
    ("sphinx", "сфгінікс"),
    ("Fox", "Фоікс"),
    ("Shchastia", "Щастя"),
    ("Zgho", "Зго"),
    ("Kh", "Х"),
    ("Yevhen", "Євген"),
    ("yi", "ї"),
    ("Don't-touch", "Донт-тоуч"),
    ("C3PO", "К3ПО"),
    ("kHarkiv", "харків"),
    ("sHchash", "щаш"),
    ("Zghurovskyi", "Згуровський"),
    ("Kiev", "Київ"),
    ("Mykolaiv", "Миколаїв"),
    ("sHcHzGhKh", "шчзґгх"),
    ("qz", "кз"),
])
def test_lat2ukr_kmu(latin, expected):
    assert translit(latin, Lat2UkrKMU) == expected
