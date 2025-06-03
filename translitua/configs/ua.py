import re
from translitua.tools import convert_table, add_uppercase


class UkrainianWWS(object):
    """
    According to Scholarly system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "h",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "je",
        "ж": "ž",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "ji",
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
        "ц": "c",
        "ч": "č",
        "ш": "š",
        "щ": "šč",
        "ь": "ʹ",
        "ю": "ju",
        "я": "ja",
        "\u0027": "",
        "\u2019": "",
        "\u02BC": "",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianBritish(object):
    """
    According to British system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "h",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "ye",
        "ж": "zh",
        "з": "z",
        "и": "ȳ",
        "і": "i",
        "ї": "yi",
        "й": "ĭ",
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
        "ь": "",
        "ю": "yu",
        "я": "ya",
        "\u0027": "",
        "\u2019": "",
        "\u02BC": "",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianBGN(object):
    """
    According to BGN system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "h",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "ye",
        "ж": "zh",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "yi",
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
        "ь": "'",
        "ю": "yu",
        "я": "ya",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianISO9(object):
    """
    According to ISO9 system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "ґ": "g̀",
        "д": "d",
        "е": "e",
        "є": "ê",
        "ж": "ž",
        "з": "z",
        "и": "i",
        "і": "ì",
        "ї": "ï",
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
        "ь": "′",
        "ю": "û",
        "я": "â",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianFrench(object):
    """
    According to French system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "h",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "ie",
        "ж": "j",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "ï",
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
        "у": "ou",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "tch",
        "ш": "ch",
        "щ": "chtch",
        "ь": "",
        "ю": "iou",
        "я": "ia",
        "\u0027": "",
        "\u2019": "",
        "\u02BC": "",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianSimple(object):
    """
    Borrowed from https://github.com/barseghyanartur/transliterate/blob/master/src/transliterate/contrib/languages/uk/data/python32.py
    by Artur Barseghyan <artur.barseghyan@gmail.com>
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "h",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "ye",
        "ж": "zh",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "yi",
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
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ь": "'",
        "ю": "ju",
        "я": "ja",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianKMU(object):
    """
    According to National system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "h",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "ie",
        "ж": "zh",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "i",
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
        "ю": "iu",
        "я": "ia",
    }

    _DELETE_CASES = [
        "ь",
        "Ь",
        "\u0027",
        "\u2019",
        "\u02BC",
    ]

    _SPECIAL_CASES = {
        "зг": "zgh",
        "ЗГ": "ZGh",
    }

    _FIRST_CHARACTERS = {"є": "ye", "ї": "yi", "й": "y", "ю": "yu", "я": "ya"}

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))
    FIRST_CHARACTERS = add_uppercase(_FIRST_CHARACTERS)
    SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)

    PATTERN1 = re.compile("(?mu)" + "|".join(SPECIAL_CASES.keys()))
    PATTERN2 = re.compile("(?mu)" + r"\b(" + "|".join(FIRST_CHARACTERS.keys()) + ")")
    DELETE_PATTERN = re.compile("(?mu)" + "|".join(_DELETE_CASES))


class UkrainianGerman(object):
    """
    According to German system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "w",
        "г": "h",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "je",
        "ж": "sh",
        "з": "s",
        "и": "y",
        "і": "i",
        "ї": "ji",
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
        "х": "ch",
        "ц": "z",
        "ч": "tsch",
        "ш": "sch",
        "щ": "schtsch",
        "ь": "",
        "ю": "ju",
        "я": "ja",
        "\u0027": "",
        "\u2019": "",
        "\u02BC": "",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianGOST1971(object):
    """
    According to Gost 1971 system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "je",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "і": "i",
        "ї": "ji",
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
        "х": "kh",
        "ц": "c",
        "ч": "ch",
        "ш": "sh",
        "щ": "shh",
        "ь": "'",
        "ю": "ju",
        "я": "ja",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianGOST1986(object):
    """
    According to Gost 1986 system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "je",
        "ж": "ž",
        "з": "z",
        "и": "i",
        "і": "i",
        "ї": "i",
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
        "щ": "šč",
        "ь": "'",
        "ю": "ju",
        "я": "ja",
        "\u0027": "",
        "\u2019": "",
        "\u02BC": "",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianPassport2007(object):
    """
    According to Passport 2007 system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "ie",
        "ж": "zh",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "i",
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
        "ь": "",
        "ю": "iu",
        "я": "ia",
        "\u0027": "",
        "\u2019": "",
        "\u02BC": "",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianNational1996(object):
    """
    According to National 1996 system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "h",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "ie",
        "ж": "zh",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "i",
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
        "щ": "sch",
        "ь": "'",
        "ю": "iu",
        "я": "ia",
    }

    _SPECIAL_CASES = {
        "зг": "zgh",
        "ЗГ": "ZGh",
    }

    _FIRST_CHARACTERS = {"є": "ye", "ї": "yi", "й": "y", "ю": "yu", "я": "ya"}

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))
    FIRST_CHARACTERS = add_uppercase(_FIRST_CHARACTERS)
    SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)

    PATTERN1 = re.compile("(?mu)" + "|".join(SPECIAL_CASES.keys()))
    PATTERN2 = re.compile("(?mu)" + r"\b(" + "|".join(FIRST_CHARACTERS.keys()) + ")")


class UkrainianPassport2004Alt(object):
    """
    According to Passport 2004 system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "ґ": "h",
        "д": "d",
        "е": "e",
        "є": "ie",
        "ж": "j",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "i",
        "й": "i",
        "к": "c",
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
        "ь": "'",
        "ю": "iu",
        "я": "ia",
    }

    _SPECIAL_CASES = {
        "зг": "zgh",
        "ЗГ": "ZGh",
    }

    _FIRST_CHARACTERS = {"є": "ye", "ї": "yi", "й": "y", "ю": "yu", "я": "ya"}

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))
    FIRST_CHARACTERS = add_uppercase(_FIRST_CHARACTERS)
    SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)

    PATTERN1 = re.compile("(?mu)" + "|".join(SPECIAL_CASES.keys()))
    PATTERN2 = re.compile("(?mu)" + r"\b(" + "|".join(FIRST_CHARACTERS.keys()) + ")")
