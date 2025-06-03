import pytest
from translitua.translit import translit, UkrainianPassport2004Alt

@pytest.mark.parametrize("src,expected", [
    ("Щука", "Shchuca"),
    ("Дмитро", "Dmytro"),
    ("Євген", "Yevgen"),
    ("Юлія", "Yuliia"),
    ("Ярошенко", "Yaroshenco"),
    ("Знам'янка", "Znam'yanca"),
    ("Яготин", "Yagotyn"),
    ("Костянтин", "Costiantyn"),
    ("піранья", "piran'ia"),
    ("Феодосія", "Feodosiia"),
])
def test_ukrainian_passport2004alt(src, expected):
    assert translit(src, UkrainianPassport2004Alt) == expected
