import re
from translitua.tools import convert_table, add_uppercase


class Lat2RuSimple(object):
    """Reverse transliteration for :class:`RussianSimple`."""

    _ONE_LETTER = {
        "a": "а", "b": "б", "c": "к", "d": "д", "e": "е", "f": "ф",
        "g": "г", "h": "х", "i": "и", "j": "й", "k": "к", "l": "л",
        "m": "м", "n": "н", "o": "о", "p": "п", "q": "к", "r": "р",
        "s": "с", "t": "т", "u": "у", "v": "в", "w": "в",
        "x": "x", "y": "ы", "z": "з", "'": "ь",
    }
    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_ONE_LETTER))

    _SEQUENCES = {
        "shch": "щ",
        "sch": "щ",
        "zh": "ж",
        "kh": "х",
        "ts": "ц",
        "ch": "ч",
        "sh": "ш",
        "ju": "ю",
        "ja": "я",
        "yo": "ё",
    }
    SEQ_CASES = add_uppercase(_SEQUENCES)
    PATTERN_SEQ = re.compile(r"(?i)" + "|".join(sorted(SEQ_CASES, key=len, reverse=True)))

    PATTERN_Y_END = re.compile(r"(?i)y\b")
    DELETE_PATTERN = re.compile(r"[\u0027\u2019\u02BC]")
    LAT_RE = re.compile(r"[A-Za-z]")


class Lat2RuISO9SystemB(object):
    """Reverse transliteration for :class:`RussianISO9SystemB`."""

    _ONE_LETTER = {
        "a": "а", "b": "б", "v": "в", "g": "г", "d": "д", "e": "е",
        "z": "з", "i": "и", "j": "й", "k": "к", "l": "л", "m": "м",
        "n": "н", "o": "о", "p": "п", "r": "р", "s": "с", "t": "т",
        "u": "у", "f": "ф", "x": "х", "y": "ы", "'": "ь",
    }
    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_ONE_LETTER))

    _SEQUENCES = {
        "shh": "щ",
        "zh": "ж",
        "cz": "ц",
        "ch": "ч",
        "sh": "ш",
        "yo": "ё",
        "yu": "ю",
        "ya": "я",
        "e'": "э",
        "y'": "ы",
        "''": "ъ",
    }
    SEQ_CASES = add_uppercase(_SEQUENCES)
    PATTERN_SEQ = re.compile(r"(?i)" + "|".join(sorted(SEQ_CASES, key=len, reverse=True)))

    PATTERN_Y_END = re.compile(r"(?i)y\b")
    LAT_RE = re.compile(r"[A-Za-z']")

