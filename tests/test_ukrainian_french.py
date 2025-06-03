import pytest
from translitua.translit import translit, UkrainianFrench

@pytest.mark.parametrize("src,expected", [
    ("Щука", "Chtchouka"),
    ("Дмитро", "Dmytro"),
    ("Євген", "Ievhen"),
    ("Юлія", "Iouliia"),
    ("Ярошенко", "Iarochenko"),
    ("Знам'янка", "Znamianka"),
    ("Яготин", "Iahotyn"),
    ("Костянтин", "Kostiantyn"),
    ("піранья", "pirania"),
    ("Феодосія", "Feodosiia"),
])
def test_ukrainian_french(src, expected):
    assert translit(src, UkrainianFrench) == expected
