import pytest
from translitua.translit import translit, RussianInternationalPassport1997Reduced

@pytest.mark.parametrize("src,expected", [
    ("Ёж", "Ezh"),
    ("Щёки", "Shcheki"),
    ("Подъезд", "Pod'ezd"),
    ("Полоний", "Polony"),
    ("Красный", "Krasny"),
    ("Варенье", "Varen'ye"),
    ("Соловьи", "Solovi"),
    ("Новьё", "Nov'ye"),
    ("Ель", "El"),
    ("Подъёб", "Pod'eb"),
])
def test_russian_international_passport1997reduced(src, expected):
    assert translit(src, RussianInternationalPassport1997Reduced) == expected
