import pytest
from translitua.translit import translit, UkrainianBGN

@pytest.mark.parametrize("src,expected", [
    ("Щука", "Shchuka"),
    ("Дмитро", "Dmytro"),
    ("Євген", "Yevhen"),
    ("Юлія", "Yuliya"),
    ("Ярошенко", "Yaroshenko"),
    ("Знам'янка", "Znam'yanka"),
    ("Яготин", "Yahotyn"),
    ("Костянтин", "Kostyantyn"),
    ("піранья", "piran'ya"),
    ("Феодосія", "Feodosiya"),
])
def test_ukrainian_bgn(src, expected):
    assert translit(src, UkrainianBGN) == expected
