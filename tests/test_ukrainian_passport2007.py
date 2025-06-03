import pytest
from translitua.translit import translit, UkrainianPassport2007

@pytest.mark.parametrize("src,expected", [
    ("Щука", "Shchuka"),
    ("Дмитро", "Dmytro"),
    ("Євген", "Ievgen"),
    ("Юлія", "Iuliia"),
    ("Ярошенко", "Iaroshenko"),
    ("Знам'янка", "Znamianka"),
    ("Яготин", "Iagotyn"),
    ("Костянтин", "Kostiantyn"),
    ("піранья", "pirania"),
    ("Феодосія", "Feodosiia"),
])
def test_ukrainian_passport2007(src, expected):
    assert translit(src, UkrainianPassport2007) == expected
