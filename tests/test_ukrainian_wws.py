import pytest
from translitua.translit import translit, UkrainianWWS

@pytest.mark.parametrize("src,expected", [
    ("Щука", "Ščuka"),
    ("Дмитро", "Dmytro"),
    ("Євген", "Jevhen"),
    ("Юлія", "Julija"),
    ("Ярошенко", "Jarošenko"),
    ("Знам'янка", "Znamjanka"),
    ("Яготин", "Jahotyn"),
    ("Костянтин", "Kostjantyn"),
    ("піранья", "piranʹja"),
    ("Феодосія", "Feodosija"),
])
def test_ukrainian_wws(src, expected):
    assert translit(src, UkrainianWWS) == expected
