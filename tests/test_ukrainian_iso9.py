import pytest
from translitua.translit import translit, UkrainianISO9

@pytest.mark.parametrize("src,expected", [
    ("Щука", "Ŝuka"),
    ("Дмитро", "Dmitro"),
    ("Євген", "Êvgen"),
    ("Юлія", "Ûlìâ"),
    ("Ярошенко", "Ârošenko"),
    ("Знам'янка", "Znam'ânka"),
    ("Яготин", "Âgotin"),
    ("Костянтин", "Kostântin"),
    ("піранья", "pìran′â"),
    ("Феодосія", "Feodosìâ"),
])
def test_ukrainian_iso9(src, expected):
    assert translit(src, UkrainianISO9) == expected
