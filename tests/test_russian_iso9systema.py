import pytest
from translitua.translit import translit, RussianISO9SystemA

@pytest.mark.parametrize("src,expected", [
    ("Ёж", "Ëž"),
    ("Щёки", "Ŝëki"),
    ("Подъезд", "Pod″ezd"),
    ("Полоний", "Polonij"),
    ("Красный", "Krasnyj"),
    ("Варенье", "Varen′e"),
    ("Соловьи", "Solov′i"),
    ("Новьё", "Nov′ë"),
    ("Ель", "El′"),
    ("Подъёб", "Pod″ëb"),
])
def test_russian_iso9systema(src, expected):
    assert translit(src, RussianISO9SystemA) == expected
