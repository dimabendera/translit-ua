import pytest
from translitua.translit import translit, RussianDriverLicense

@pytest.mark.parametrize("src,expected", [
    ("Ёж", "Yozh"),
    ("Щёки", "Shcheki"),
    ("Подъезд", "Pod'yezd"),
    ("Полоний", "Poloniy"),
    ("Красный", "Krasnyy"),
    ("Варенье", "Varen'ye"),
    ("Соловьи", "Solov'yi"),
    ("Новьё", "Nov'yo"),
    ("Ель", "Yel'"),
    ("Подъёб", "Pod'yob"),
])
def test_russian_driver_license(src, expected):
    assert translit(src, RussianDriverLicense) == expected
