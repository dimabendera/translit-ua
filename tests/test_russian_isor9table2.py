import pytest
from translitua.translit import translit, RussianISOR9Table2

@pytest.mark.parametrize("src,expected", [
    ("Ёж", "Jozh"),
    ("Щёки", "Shhjoki"),
    ("Подъезд", "Pod″ezd"),
    ("Полоний", "Polonijj"),
    ("Красный", "Krasnyjj"),
    ("Варенье", "Varen′e"),
    ("Соловьи", "Solov′i"),
    ("Новьё", "Nov′jo"),
    ("Ель", "El′"),
    ("Подъёб", "Pod″job"),
])
def test_russian_isor9table2(src, expected):
    assert translit(src, RussianISOR9Table2) == expected
