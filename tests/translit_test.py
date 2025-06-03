"""
translit_test.py

pytest -q
"""
import sys
import pytest

sys.path.append("./")

from translitua import (translit,
    UkrainianSimple,
    UkrainianWWS,
    UkrainianBritish,
    UkrainianFrench,
    UkrainianGerman,
    UkrainianGOST1971,
    RussianInternationalPassport1997,
    RussianInternationalPassport1997Reduced,
    RussianDriverLicense,
    RussianISO9SystemB,
    Lat2UkrKMU,
)

# ---------------------------------------------------------------------------
# 1. Дефолтна українська транслітерація (УКМУ-2010)
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "src,expected",
    [
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
    ],
)
def test_ukr_default(src, expected):
    assert translit(src) == expected


def test_preserve_case_flag():
    assert translit("ЗГУРОВСЬКИЙ", preserve_case=False) == "ZGhUROVSKYI"


# ---------------------------------------------------------------------------
# 2. Альтернативні українські схеми
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "src,scheme,expected",
    [
        ("Дмитро Згуровский", UkrainianSimple,  "Dmytro Zhurovskyj"),
        ("Дмитро Щуровский",  UkrainianWWS,     "Dmytro Ščurovskyj"),
        ("Дмитро Щуровский",  UkrainianBritish, "Dmȳtro Shchurovskȳĭ"),
        ("Дмитро Щуровский",  UkrainianFrench,  "Dmytro Chtchourovskyy"),
        ("Дмитро Щуровский",  UkrainianGerman,  "Dmytro Schtschurowskyj"),
        ("Дмитро Щуровский",  UkrainianGOST1971,"Dmitro Shhurovskij"),
    ],
)
def test_ukr_variant_schemes(src, scheme, expected):
    assert translit(src, scheme) == expected


# ---------------------------------------------------------------------------
# 3. Російські схеми
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "src,scheme,expected",
    [
        # International Passport 1997
        ("Варенье",  RussianInternationalPassport1997,        "Varen'ye"),
        ("Новьё",    RussianInternationalPassport1997,        "Nov'ye"),
        ("Красный",  RussianInternationalPassport1997,        "Krasnyy"),
        ("Полоний",  RussianInternationalPassport1997,        "Poloniy"),
        # International Passport 1997 Reduced
        ("Красный",  RussianInternationalPassport1997Reduced, "Krasny"),
        ("Полоний",  RussianInternationalPassport1997Reduced, "Polony"),
        # Driver License
        ("Варенье",  RussianDriverLicense,                    "Varen'ye"),
        ("Подъезд",  RussianDriverLicense,                    "Pod'yezd"),
        ("Новьё",    RussianDriverLicense,                    "Nov'yo"),
        ("Подъёб",   RussianDriverLicense,                    "Pod'yob"),
        ("Ель",      RussianDriverLicense,                    "Yel'"),
        ("Ёж",       RussianDriverLicense,                    "Yozh"),
        ("Щёки",     RussianDriverLicense,                    "Shcheki"),
        ("Соловьи",  RussianDriverLicense,                    "Solov'yi"),
        # ISO-9 System B
        ("Цёмки",    RussianISO9SystemB,                      "Cyomki"),
        ("Цыц",      RussianISO9SystemB,                      "Cy'cz"),
    ],
)
def test_russian_schemes(src, scheme, expected):
    assert translit(src, scheme) == expected


@pytest.mark.parametrize(
    "latin,expected",
    [
        # прості приклади
        ("BMW",          "БМВ"),          # усі великі
        ("Bmw",          "Бмв"),          # Capitalize
        ("Kharkiv",      "Харків"),       # kh → х, iv → ів
        ("boy",          "бой"),          # y наприкінці → й
        ("busy",         "бусй"),         # y-rule всередині іншого слова
        ("sphinx",       "сфгінікс"),     # x → ікс
        ("Fox",          "Фоікс"),        # X-rule у кінці
        ("Shchastia",    "Щастя"),        # shch + ia
        ("Zgho",         "Зго"),          # zgh → зг
        ("Kh",           "Х"),            # digraph-слово
        ("Yevhen",       "Євген"),        # ye на початку слова
        ("yi",           "ї"),            # yi → ї
        ("Don't-touch",  "Донт-тоуч"),   # апострофи видаляємо
        ("C3PO",         "К3ПО"),         # цифри лишаються
        ("kHarkiv",      "харків"),
        ("sHchash",      "щаш"),
        ("Zghurovskyi",  "Згуровський"),
        ("Kiev",         "Київ"),
        ("Mykolaiv",     "Миколаїв"),
        ("sHcHzGhKh",    "шчзґгх"),
        ("qz",           "кз"),
    ],
)
def test_positive(latin, expected):
    assert translit(latin, Lat2UkrKMU) == expected
