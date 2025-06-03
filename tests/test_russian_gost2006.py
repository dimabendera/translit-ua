import pytest
from translitua.translit import translit, RussianGOST2006

@pytest.mark.parametrize("src,expected", [
    ("Ёж", "Ezh"),
    ("Щёки", "Shcheki"),
    ("Подъезд", "Podezd"),
    ("Полоний", "Polonii"),
    ("Красный", "Krasnyi"),
    ("Варенье", "Varene"),
    ("Соловьи", "Solovi"),
    ("Новьё", "Nove"),
    ("Ель", "El"),
    ("Подъёб", "Podeb"),
])
def test_russian_gost2006(src, expected):
    assert translit(src, RussianGOST2006) == expected
