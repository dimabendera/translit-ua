import pytest
from translitua.translit import translit, UkrainianNational1996

@pytest.mark.parametrize("src,expected", [
    ("Щука", "Schuka"),
    ("Дмитро", "Dmytro"),
    ("Євген", "Yevhen"),
    ("Юлія", "Yuliia"),
    ("Ярошенко", "Yaroshenko"),
    ("Знам'янка", "Znam'yanka"),
    ("Яготин", "Yahotyn"),
    ("Костянтин", "Kostiantyn"),
    ("піранья", "piran'ia"),
    ("Феодосія", "Feodosiia"),
])
def test_ukrainian_national1996(src, expected):
    assert translit(src, UkrainianNational1996) == expected
