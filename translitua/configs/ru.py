import re
from translitua.tools import convert_table, add_uppercase


class RussianSimple(object):
    """
    Borrowed from https://github.com/barseghyanartur/transliterate/blob/master/src/transliterate/contrib/languages/ru/data/python32.py
    by Artur Barseghyan <artur.barseghyan@gmail.com>
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "e",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "j",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "h",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "sch",
        "ъ": "'",
        "ы": "y",
        "ь": "'",
        "э": "e",
        "ю": "ju",
        "я": "ja",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class RussianGOST2006(object):
    """
    According to GOST 2006 system from
    https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#.D0.A1.D1.80.D0.B0.D0.B2.D0.BD.D0.B8.D1.82.D0.B5.D0.BB.D1.8C.D0.BD.D0.B0.D1.8F_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D0.B0_.D1.81.D0.B8.D1.81.D1.82.D0.B5.D0.BC_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BB.D0.B8.D1.82.D0.B5.D1.80.D0.B0.D1.86.D0.B8.D0.B8

    According to https://en.wikipedia.org/wiki/Romanization_of_Russian#Transliteration_of_the_names_in_Russian_passports
    (International Passport 2010)
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "e",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "i",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "tc",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "iu",
        "я": "ia",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class RussianICAO(object):
    """
    According to https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#.D0.A1.D1.80.D0.B0.D0.B2.D0.BD.D0.B8.D1.82.D0.B5.D0.BB.D1.8C.D0.BD.D0.B0.D1.8F_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D0.B0_.D1.81.D0.B8.D1.81.D1.82.D0.B5.D0.BC_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BB.D0.B8.D1.82.D0.B5.D1.80.D0.B0.D1.86.D0.B8.D0.B8
    (Doc 9303, ICAO)
    According to https://en.wikipedia.org/wiki/Romanization_of_Russian#Transliteration_of_the_names_in_Russian_passports
    (International Passport 2013)
    According to https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC_%D1%82%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8
    Приказ МИД N 4271 (2016-н/в)
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "e",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "i",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "ie",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "iu",
        "я": "ia",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class RussianISOR9Table2(object):
    """
    According to https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#.D0.A1.D1.80.D0.B0.D0.B2.D0.BD.D0.B8.D1.82.D0.B5.D0.BB.D1.8C.D0.BD.D0.B0.D1.8F_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D0.B0_.D1.81.D0.B8.D1.81.D1.82.D0.B5.D0.BC_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BB.D0.B8.D1.82.D0.B5.D1.80.D0.B0.D1.86.D0.B8.D0.B8
    (ISO/R 9 (1968), ГОСТ 16876-71, СТ СЭВ 1362-78, ООН (1987))
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "jo",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "jj",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "c",
        "ч": "ch",
        "ш": "sh",
        "щ": "shh",
        "ъ": "″",
        "ы": "y",
        "ь": "′",
        "э": "eh",
        "ю": "ju",
        "я": "ja",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class RussianTelegram(object):
    """
    According to https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#.D0.A1.D1.80.D0.B0.D0.B2.D0.BD.D0.B8.D1.82.D0.B5.D0.BB.D1.8C.D0.BD.D0.B0.D1.8F_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D0.B0_.D1.81.D0.B8.D1.81.D1.82.D0.B5.D0.BC_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BB.D0.B8.D1.82.D0.B5.D1.80.D0.B0.D1.86.D0.B8.D0.B8
    (telegrams)
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "e",
        "ж": "j",
        "з": "z",
        "и": "i",
        "й": "i",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "h",
        "ц": "c",
        "ч": "ch",
        "ш": "sh",
        "щ": "sc",
        "ъ": "",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "iu",
        "я": "ia",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class RussianISO9SystemA(object):
    """
    According to https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#.D0.A1.D1.80.D0.B0.D0.B2.D0.BD.D0.B8.D1.82.D0.B5.D0.BB.D1.8C.D0.BD.D0.B0.D1.8F_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D0.B0_.D1.81.D0.B8.D1.81.D1.82.D0.B5.D0.BC_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BB.D0.B8.D1.82.D0.B5.D1.80.D0.B0.D1.86.D0.B8.D0.B8
    (ISO 9:1995, ГОСТ 7.79-2000 система А)
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "ë",
        "ж": "ž",
        "з": "z",
        "и": "i",
        "й": "j",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "h",
        "ц": "c",
        "ч": "č",
        "ш": "š",
        "щ": "ŝ",
        "ъ": "″",
        "ы": "y",
        "ь": "′",
        "э": "è",
        "ю": "û",
        "я": "â",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class RussianISO9SystemB(object):
    """
    According to https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#.D0.A1.D1.80.D0.B0.D0.B2.D0.BD.D0.B8.D1.82.D0.B5.D0.BB.D1.8C.D0.BD.D0.B0.D1.8F_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D0.B0_.D1.81.D0.B8.D1.81.D1.82.D0.B5.D0.BC_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BB.D0.B8.D1.82.D0.B5.D1.80.D0.B0.D1.86.D0.B8.D0.B8
    (ISO 9:1995, ГОСТ 7.79-2000 система B)
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "yo",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "j",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "x",
        "ц": "cz",
        "ч": "ch",
        "ш": "sh",
        "щ": "shh",
        "ъ": "''",
        "ы": "y'",
        "ь": "'",
        "э": "e'",
        "ю": "yu",
        "я": "ya",
    }

    # 4: Рекомендуется использовать c перед буквами e, i, y, j; и cz — в остальных случаях.

    _SPECIAL_CASES = {
        "це": "ce",
        "цэ": "ce'",
        "ци": "ci",
        "цё": "cyo",
        "цы": "cy'",
        "цю": "cyu",
        "ця": "cya",
        "цй": "cj",
    }

    SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)
    PATTERN1 = re.compile("(?mu)" + "|".join(SPECIAL_CASES.keys()))

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class RussianInternationalPassport1997(object):
    """
    According to https://en.wikipedia.org/wiki/Romanization_of_Russian#Transliteration_of_the_names_in_Russian_passports
    (International Passport 1997)
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "e",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "'",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))

    _SPECIAL_CASES = {
        "ье": "'ye",
        "ьё": "'ye",
    }

    SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)
    PATTERN1 = re.compile("(?mu)" + "|".join(SPECIAL_CASES.keys()))


class RussianInternationalPassport1997Reduced(object):
    """
    According to https://en.wikipedia.org/wiki/Romanization_of_Russian#Transliteration_of_the_names_in_Russian_passports
    (International Passport 1997, reduced variant for ий, ый)
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "e",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "'",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))

    _SPECIAL_CASES = {
        "ье": "'ye",
        "ьё": "'ye",
        "ый": "y",
        "ий": "y",
    }

    SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)
    PATTERN1 = re.compile("(?mu)" + "|".join(SPECIAL_CASES.keys()))


class RussianDriverLicense(object):
    """
    According to https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#.D0.A1.D1.80.D0.B0.D0.B2.D0.BD.D0.B8.D1.82.D0.B5.D0.BB.D1.8C.D0.BD.D0.B0.D1.8F_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D0.B0_.D1.81.D0.B8.D1.81.D1.82.D0.B5.D0.BC_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BB.D0.B8.D1.82.D0.B5.D1.80.D0.B0.D1.86.D0.B8.D0.B8
    (Driver license)
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "ye",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "'",
        "ы": "y",
        "ь": "'",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))

    _SPECIAL_CASES = {
        # e, ye (В начале слов, а также после гласных и Ь, Ъ)
        "ье": "'ye",
        "ъе": "'ye",
        # e (После согласных Ч, Ш, Щ, Ж),
        # yo (В начале слов, а также после гласных и Ь, Ъ)
        # ye (После согласных, кроме Ч, Ш, Щ, Ж)
        "ьё": "'yo",
        "ъё": "'yo",
        "чё": "che",
        "шё": "she",
        "щё": "shche",
        "жё": "zhe",
        # yi (После Ь)
        "ьи": "'yi",
    }

    _FIRST_CHARACTERS = {
        # ye (В начале слов, а также после гласных и Ь, Ъ)
        "е": "ye",
        # yo (В начале слов, а также после гласных и Ь, Ъ)
        "ё": "yo",
    }

    SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)
    FIRST_CHARACTERS = add_uppercase(_FIRST_CHARACTERS)

    PATTERN1 = re.compile("(?mu)" + "|".join(SPECIAL_CASES.keys()))
    PATTERN2 = re.compile("(?mu)" + r"\b(" + "|".join(FIRST_CHARACTERS.keys()) + ")")
