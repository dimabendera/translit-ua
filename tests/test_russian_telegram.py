import pytest
from translitua.translit import translit, RussianTelegram

@pytest.mark.parametrize("src,expected", [
    ("Ёж", "Ej"),
    ("Щёки", "Sceki"),
    ("Подъезд", "Podezd"),
    ("Полоний", "Polonii"),
    ("Красный", "Krasnyi"),
    ("Варенье", "Varene"),
    ("Соловьи", "Solovi"),
    ("Новьё", "Nove"),
    ("Ель", "El"),
    ("Подъёб", "Podeb"),
])
def test_russian_telegram(src, expected):
    assert translit(src, RussianTelegram) == expected
