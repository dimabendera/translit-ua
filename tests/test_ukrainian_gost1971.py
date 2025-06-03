import pytest
from translitua.translit import translit, UkrainianGOST1971

@pytest.mark.parametrize("src,expected", [
    ("Щука", "Shhuka"),
    ("Дмитро", "Dmitro"),
    ("Євген", "Jevgen"),
    ("Юлія", "Julija"),
    ("Ярошенко", "Jaroshenko"),
    ("Знам'янка", "Znam'janka"),
    ("Яготин", "Jagotin"),
    ("Костянтин", "Kostjantin"),
    ("піранья", "piran'ja"),
    ("Феодосія", "Feodosija"),
])
def test_ukrainian_gost1971(src, expected):
    assert translit(src, UkrainianGOST1971) == expected
