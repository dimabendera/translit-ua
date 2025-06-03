import pytest
from translitua.translit import translit, UkrainianGOST1986

@pytest.mark.parametrize("src,expected", [
    ("Щука", "Ščuka"),
    ("Дмитро", "Dmitro"),
    ("Євген", "Jevgen"),
    ("Юлія", "Julija"),
    ("Ярошенко", "Jarošenko"),
    ("Знам'янка", "Znamjanka"),
    ("Яготин", "Jagotin"),
    ("Костянтин", "Kostjantin"),
    ("піранья", "piran'ja"),
    ("Феодосія", "Feodosija"),
])
def test_ukrainian_gost1986(src, expected):
    assert translit(src, UkrainianGOST1986) == expected
