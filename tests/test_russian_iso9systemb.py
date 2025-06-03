import pytest
from translitua.translit import translit, RussianISO9SystemB

@pytest.mark.parametrize("src,expected", [
    ("Ёж", "Yozh"),
    ("Щёки", "Shhyoki"),
    ("Подъезд", "Pod''ezd"),
    ("Полоний", "Polonij"),
    ("Красный", "Krasny'j"),
    ("Варенье", "Varen'e"),
    ("Соловьи", "Solov'i"),
    ("Новьё", "Nov'yo"),
    ("Ель", "El'"),
    ("Подъёб", "Pod''yob"),
])
def test_russian_iso9systemb(src, expected):
    assert translit(src, RussianISO9SystemB) == expected
