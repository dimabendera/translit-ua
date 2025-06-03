import pytest
from translitua.translit import translit, RussianInternationalPassport1997

@pytest.mark.parametrize("src,expected", [
    ("Ёж", "Ezh"),
    ("Щёки", "Shcheki"),
    ("Подъезд", "Pod'ezd"),
    ("Полоний", "Poloniy"),
    ("Красный", "Krasnyy"),
    ("Варенье", "Varen'ye"),
    ("Соловьи", "Solovi"),
    ("Новьё", "Nov'ye"),
    ("Ель", "El"),
    ("Подъёб", "Pod'eb"),
])
def test_russian_international_passport1997(src, expected):
    assert translit(src, RussianInternationalPassport1997) == expected
