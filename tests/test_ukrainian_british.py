import pytest
from translitua.translit import translit, UkrainianBritish

@pytest.mark.parametrize("src,expected", [
    ("Щука", "Shchuka"),
    ("Дмитро", "Dmȳtro"),
    ("Євген", "Yevhen"),
    ("Юлія", "Yuliya"),
    ("Ярошенко", "Yaroshenko"),
    ("Знам'янка", "Znamyanka"),
    ("Яготин", "Yahotȳn"),
    ("Костянтин", "Kostyantȳn"),
    ("піранья", "piranya"),
    ("Феодосія", "Feodosiya"),
])
def test_ukrainian_british(src, expected):
    assert translit(src, UkrainianBritish) == expected
