import pytest
from translitua.translit import translit, UkrainianGerman

@pytest.mark.parametrize("src,expected", [
    ("Щука", "Schtschuka"),
    ("Дмитро", "Dmytro"),
    ("Євген", "Jewhen"),
    ("Юлія", "Julija"),
    ("Ярошенко", "Jaroschenko"),
    ("Знам'янка", "Snamjanka"),
    ("Яготин", "Jahotyn"),
    ("Костянтин", "Kostjantyn"),
    ("піранья", "piranja"),
    ("Феодосія", "Feodosija"),
])
def test_ukrainian_german(src, expected):
    assert translit(src, UkrainianGerman) == expected
