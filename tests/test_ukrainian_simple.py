import pytest
from translitua.translit import translit, UkrainianSimple

@pytest.mark.parametrize("src,expected", [
    ("Щука", "Shchuka"),
    ("Дмитро", "Dmytro"),
    ("Євген", "Yevhen"),
    ("Юлія", "Julija"),
    ("Ярошенко", "Jaroshenko"),
    ("Знам'янка", "Znam'janka"),
    ("Яготин", "Jahotyn"),
    ("Костянтин", "Kostjantyn"),
    ("піранья", "piran'ja"),
    ("Феодосія", "Feodosija"),
])
def test_ukrainian_simple(src, expected):
    assert translit(src, UkrainianSimple) == expected
