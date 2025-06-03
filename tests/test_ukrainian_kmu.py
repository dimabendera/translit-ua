import pytest
from translitua.translit import translit, UkrainianKMU

@pytest.mark.parametrize("src,expected", [
    ("Дмитро Згуровский",  "Dmytro Zghurovskyi"),
    ("Дмитро ЗГуровский",  "Dmytro ZGhurovskyi"),
    ("Дмитро згуровский",  "Dmytro zghurovskyi"),
    ("Євген Петренко",     "Yevhen Petrenko"),
    ("Петренко Євген",     "Petrenko Yevhen"),
    ("Петренко.Євген",     "Petrenko.Yevhen"),
    ("Петренко,Євген",     "Petrenko,Yevhen"),
    ("Петренко/Євген",     "Petrenko/Yevhen"),
    ("Євгєн",              "Yevhien"),
    ("Яготин",             "Yahotyn"),
    ("Ярошенко",           "Yaroshenko"),
    ("Костянтин",          "Kostiantyn"),
    ("Знам'янка",          "Znamianka"),
    ("Знам’янка",          "Znamianka"),
    ("Феодосія",           "Feodosiia"),
    ("Ньютон",             "Niuton"),
    ("піранья",            "pirania"),
    ("кур'єр",             "kurier"),
    ("ЗГУРОВСЬКИЙ",        "ZGHUROVSKYI"),
])
def test_ukrainian_kmu(src, expected):
    assert translit(src, UkrainianKMU) == expected


def test_preserve_case_false():
    assert translit("ЗГУРОВСЬКИЙ", UkrainianKMU, preserve_case=False) == "ZGhUROVSKYI"
