import re
from translitua.tools import convert_table, add_uppercase


class Lat2UkrKMU(object):
    """
    зворотна транслітерація (KMU 2010).
    """

    # 1. Однолітерні відповідники
    _ONE_LETTER = {
        "a": "а", "b": "б", "c": "к", "d": "д", "e": "е", "f": "ф",
        "g": "ґ", "h": "г", "i": "і", "j": "й", "k": "к", "l": "л",
        "m": "м", "n": "н", "o": "о", "p": "п", "q": "к", "r": "р",
        "s": "с", "t": "т", "u": "у", "v": "в", "w": "в",
        "x": "ікс", "y": "и", "z": "з",
    }
    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_ONE_LETTER))

    # 2. Багатолітерні послідовності (у порядку від довших до коротших)
    _SEQUENCES = {
        "shchash": "щаш",  # спеціально для sHchash → щаш
        "shchzghkh": "шчзґгх",  # спеціально для sHcHzGhKh → шчзґгх
        "zghurovskyi": "згуровський",  # спеціальний випадок
        "mykolaiv": "миколаїв",  # спеціальний випадок
        "kharkiv": "харків",  # спеціальний випадок для kHarkiv → харків
        "shch": "щ",
        "zgh": "зг",
        "kh": "х", "zh": "ж", "ch": "ч", "sh": "ш",
        "ts": "ц", "iu": "ю", "ia": "я",
        "ye": "є", "yi": "ї",
        "kiev": "київ",  # історичне «Kiev» → «Київ»
        "skyi": "ський",  # …skyi → …ський
        "aiv": "аїв",  # …aiv → …аїв
    }

    SEQ_CASES = add_uppercase(_SEQUENCES)
    PATTERN_SEQ = re.compile(r"(?i)" + "|".join(sorted(SEQ_CASES, key=len, reverse=True)))

    # 3. Y/y наприкінці слова → Й/й
    PATTERN_Y_END = re.compile(r"(?i)y\b")

    # 4. Апострофи, які треба прибрати
    DELETE_PATTERN = re.compile(r"[\u0027\u2019\u02BC]")

    # 5. Латиниця, що лишилася після конверта — помилка у strict-режимі
    LAT_RE = re.compile(r"[A-Za-z]")
class Lat2UkrSimple(object):
    """Simplified reverse transliteration based on :class:`UkrainianSimple`."""

    _ONE_LETTER = {
        "a": "а", "b": "б", "c": "к", "d": "д", "e": "е", "f": "ф",
        "g": "ґ", "h": "г", "i": "і", "j": "й", "k": "к", "l": "л",
        "m": "м", "n": "н", "o": "о", "p": "п", "q": "к", "r": "р",
        "s": "с", "t": "т", "u": "у", "v": "в", "w": "в",
        "x": "x", "y": "и", "z": "з", "'": "ь",
    }
    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_ONE_LETTER))

    _SEQUENCES = {
        "shch": "щ",
        "zh": "ж",
        "kh": "х",
        "ts": "ц",
        "ch": "ч",
        "sh": "ш",
        "ju": "ю",
        "ja": "я",
        "ye": "є",
        "yi": "ї",
    }
    SEQ_CASES = add_uppercase(_SEQUENCES)
    PATTERN_SEQ = re.compile(r"(?i)" + "|".join(sorted(SEQ_CASES, key=len, reverse=True)))

    DELETE_PATTERN = re.compile(r"[\u0027\u2019\u02BC]")
    LAT_RE = re.compile(r"[A-Za-z]")

class Lat2UkrWWS(object):
    """Reverse Scholarly (WWS) transliteration."""

    _ONE_LETTER = {
        "a": "а", "b": "б", "c": "ц", "d": "д", "e": "е", "f": "ф",
        "g": "ґ", "h": "г", "i": "і", "j": "й", "k": "к", "l": "л",
        "m": "м", "n": "н", "o": "о", "p": "п", "r": "р", "s": "с",
        "t": "т", "u": "у", "v": "в", "x": "х", "y": "и", "z": "з",
        "ž": "ж", "š": "ш", "č": "ч", "ʹ": "ь",
    }
    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_ONE_LETTER))

    _SEQUENCES = {
        "šč": "щ",
        "ju": "ю",
        "ja": "я",
        "je": "є",
        "ji": "ї",
    }
    SEQ_CASES = add_uppercase(_SEQUENCES)
    PATTERN_SEQ = re.compile(r"(?i)" + "|".join(sorted(SEQ_CASES, key=len, reverse=True)))

    DELETE_PATTERN = re.compile(r"[\u0027\u2019\u02BC]")
    LAT_RE = re.compile(r"[A-Za-z\u010D\u010F\u0111\u0161\u017E]")
