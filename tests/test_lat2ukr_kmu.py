"""
 test_lat2ukr_kmu.py

 pytest -q
"""
import sys
import pytest
sys.path.append("./")
from translitua import translit, Lat2UkrKMU

# ───────────────────── 1. позитивні сценарії ──────────────────────
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
    ],
)
def test_positive(latin, expected):
    assert translit(latin, Lat2UkrKMU) == expected


# ───────────────────── 2. відомі слабкі місця (очікуємо ❌) ──────────────────────
@pytest.mark.parametrize(
    "latin",
    [
        "kHarkiv",   # змішаний регістр у digraph: KeyError 'kH'
        "sHchash",   # 'sHch': SHCH matched, але sHch – ні
        "Zghurovskyi",  # має бути «…ський», отримуємо «…скї»
        "Kiev",      # rule ie → и/є не реалізоване
        "Mykolaiv",  # iv у кінці → їв (або й), зараз «ив»
    ],
)
def test_should_fail(latin):
    """Тести, що нині падають. Після фіксів перенесіть їх у позитивні."""
    with pytest.raises(Exception):
        translit(latin, Lat2UkrKMU)


# ───────────────────── 3. нестандартні злами ──────────────────────
def test_mixed_case_weird():
    """ Намагаємось зламати за допомогою хаотичного регістру. """
    latin = "sHcHzGhKh"
    with pytest.raises(KeyError):
        translit(latin, Lat2UkrKMU)

def test_unknown_bigram():
    """ Незареєстрований диграф → очікуваний KeyError. """
    with pytest.raises(KeyError):
        translit("qz", Lat2UkrKMU)

