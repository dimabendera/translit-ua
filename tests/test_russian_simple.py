import pytest
from translitua.translit import translit, RussianSimple

@pytest.mark.parametrize("src,expected", [
    ("Ёж", "Ezh"),
    ("Щёки", "Scheki"),
    ("Подъезд", "Pod'ezd"),
    ("Полоний", "Polonij"),
    ("Красный", "Krasnyj"),
    ("Варенье", "Varen'e"),
    ("Соловьи", "Solov'i"),
    ("Новьё", "Nov'e"),
    ("Ель", "El'"),
    ("Подъёб", "Pod'eb"),
])
def test_russian_simple(src, expected):
    assert translit(src, RussianSimple) == expected
