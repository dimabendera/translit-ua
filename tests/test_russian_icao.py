import pytest
from translitua.translit import translit, RussianICAO

@pytest.mark.parametrize("src,expected", [
    ("Ёж", "Ezh"),
    ("Щёки", "Shcheki"),
    ("Подъезд", "Podieezd"),
    ("Полоний", "Polonii"),
    ("Красный", "Krasnyi"),
    ("Варенье", "Varene"),
    ("Соловьи", "Solovi"),
    ("Новьё", "Nove"),
    ("Ель", "El"),
    ("Подъёб", "Podieeb"),
])
def test_russian_icao(src, expected):
    assert translit(src, RussianICAO) == expected
