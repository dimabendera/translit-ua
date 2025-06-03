# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import sys

# Припускаємо, що ці конфігурації правильно визначені та імпортовані
# sys.path.append("./") # Якщо тести запускаються з кореневої папки, а translitua - підпапка
from .configs.reverse_ua import Lat2UkrKMU, Lat2UkrSimple, Lat2UkrWWS
from .configs.reverse_ru import Lat2RuSimple, Lat2RuISO9SystemB
from .configs.ua import (
    UkrainianKMU,
    UkrainianSimple,
    UkrainianWWS,
    UkrainianBritish,
    UkrainianBGN,
    UkrainianISO9,
    UkrainianFrench,
    UkrainianGerman,
    UkrainianGOST1971,
    UkrainianGOST1986,
    UkrainianPassport2007,
    UkrainianNational1996,
    UkrainianPassport2004Alt,
)
from .configs.ru import (
    RussianSimple,
    RussianGOST2006,
    RussianICAO,
    RussianTelegram,
    RussianInternationalPassport1997,
    RussianDriverLicense,
    RussianInternationalPassport1997Reduced,
    RussianISO9SystemB,
    RussianISO9SystemA,
    RussianISOR9Table2,
)

if sys.version < "3":
    text_type = unicode
else:
    text_type = str

ALL_UKRAINIAN = [
    UkrainianKMU,
    UkrainianSimple,
    UkrainianWWS,
    UkrainianBritish,
    UkrainianBGN,
    UkrainianISO9,
    UkrainianFrench,
    UkrainianGerman,
    UkrainianGOST1971,
    UkrainianGOST1986,
    UkrainianPassport2007,
    UkrainianNational1996,
    UkrainianPassport2004Alt,
]

ALL_RUSSIAN = [
    RussianSimple,
    RussianGOST2006,
    RussianICAO,
    RussianTelegram,
    RussianInternationalPassport1997,
    RussianDriverLicense,
    RussianInternationalPassport1997Reduced,
    RussianISO9SystemB,
    RussianISO9SystemA,
    RussianISOR9Table2,
]

# Backward compatibility
RussianInternationalPassport = RussianInternationalPassport1997

ALL_LATIN_TO_UKRAINIAN = [Lat2UkrKMU, Lat2UkrSimple, Lat2UkrWWS]
ALL_LATIN_TO_RUSSIAN = [Lat2RuSimple, Lat2RuISO9SystemB]
ALL_TRANSLITERATIONS = (
    ALL_UKRAINIAN + ALL_RUSSIAN + ALL_LATIN_TO_UKRAINIAN + ALL_LATIN_TO_RUSSIAN
)


def translit(src, table=UkrainianKMU, preserve_case=True, strict=True):
    """Transliterates given unicode `src` text
    to transliterated variant according to a given transliteration table.
    Official ukrainian transliteration is used by default

    :param src: string to transliterate
    :type src: str
    :param table: transliteration table
    :type table: transliteration table object
    :param preserve_case: convert result to uppercase if source is uppercased
    (see the example below for the difference that flag makes)
    :type preserve_case: bool
    :param strict: True — підіймаємо KeyError, якщо після трансліта
                    лишилась хоч одна латинська літера (для Lat->Ukr).
    :type strict: bool
    :returns: transliterated string
    :rtype: str


    >>> print(translit("Дмитро Згуровский"))
    Dmytro Zghurovskyi
    >>> print(translit("boy", Lat2UkrKMU))
    'бой'
    """

    original_src_for_case = text_type(src)
    src_text = original_src_for_case

    # ───── LATIN → УКР ─────
    # Визначаємо, чи це таблиця для Латиниця -> Кирилиця на основі наявності специфічних атрибутів
    if hasattr(table, "PATTERN_SEQ") and hasattr(table, "LAT_RE") and hasattr(table, "SEQ_CASES"):
        # Апострофи
        if hasattr(table, "DELETE_PATTERN"):
            src_text = table.DELETE_PATTERN.sub("", src_text)

        # Спеціальне правило для 'ph' -> 'ф' (з залишенням 'h' для подальшої обробки -> 'г')
        # Це було в оригінальному коді і потрібно для тесту "sphinx"
        # В ідеалі, це мало б бути частиною конфігурації таблиці Lat2UkrKMU
        if table is Lat2UkrKMU or isinstance(table, Lat2UkrKMU):  # Перевірка конкретного типу таблиці
            src_text = re.sub(r"(?i)p(?=h)", lambda m: "Ф" if m.group().isupper() else "ф", src_text)

        # ── 1. багатолітерні послідовності ──
        def _seq_lat_to_ukr(m):
            raw = m.group(0)  # Текст, що збігся (напр. "kH", "Shch")
            base = raw.lower()  # Базова форма для пошуку в таблиці (напр. "kh", "shch")

            # repl - це базова заміна в нижньому регістрі (напр. "х" для "kh", "щ" для "shch")
            repl = table.SEQ_CASES[base]

            if raw.isupper():  # Якщо все слово ВЕЛИКИМИ ("KH")
                return repl.upper()  # -> "Х"
            elif raw.islower():  # Якщо все слово маленькими ("kh")
                return repl  # -> "х" (repl вже в нижньому регістрі)
            # Якщо перша літера велика, решта маленькі ("Kh", "Shch")
            elif raw[0].isupper() and (len(raw) == 1 or raw[1:].islower()):
                if len(repl) == 1:  # Для однолітерних замін ("Х", "Щ", "Є")
                    return repl.upper()
                else:  # Для багатолітерних замін ("Ікс" з "X")
                    return repl.capitalize()
            # Для змішаних випадків, як "kH" або "sHch" (які не є isupper/islower/istitle-like)
            # Тести "kHarkiv" -> "харків" (kH -> х) та "sHchash" -> "щаш" (sHch -> щ)
            # вимагають, щоб результат був у нижньому регістрі.
            else:
                return repl

        src_text = table.PATTERN_SEQ.sub(_seq_lat_to_ukr, src_text)

        # ── 2. Y/y наприкінці слова ──
        if hasattr(table, "PATTERN_Y_END"):
            src_text = table.PATTERN_Y_END.sub(lambda m: "Й" if m.group().isupper() else "й", src_text)

        # ── 3. Однолітерні відповідники ──
        res = src_text.translate(table.MAIN_TRANSLIT_TABLE)

        # ── 4. strict: жодної латиниці не має лишитись ──
        if strict and table.LAT_RE.search(res):
            bad_match = table.LAT_RE.search(res)
            if bad_match:  # Додаткова перевірка, хоча search мав би повернути None або match object
                bad = bad_match.group(0)
                raise KeyError("unmapped latin symbol «{}» in “{}”".format(bad, original_src_for_case))

        # ── 5. Зберігаємо «крикливий» регістр, якщо треба ──
        if original_src_for_case.isupper() and preserve_case:
            return res.upper()
        else:
            # Для Lat->Ukr, регістр вже обробляється _seq_lat_to_ukr та іншими правилами.
            # original.isupper() тут для фінального перетворення всього результату на ВЕЛИКІ.
            return res

    # ───── CYRILLIC → LATIN ─────
    else:
        # Ця логіка базується на старій версії функції translit
        # та припускає, що таблиці для Кир->Лат мають відповідні атрибути

        # Видалення символів (наприклад, апострофів)
        if hasattr(table, "DELETE_PATTERN"):
            src_text = table.DELETE_PATTERN.sub("", src_text)

        # Спеціальні випадки (наприклад, "Зг" -> "Zgh")
        # Ці патерни та заміни мають бути визначені в об'єкті таблиці
        if hasattr(table, "PATTERN1") and hasattr(table, "SPECIAL_CASES"):
            # Проста заміна, як у старій версії. Покладається на те, що SPECIAL_CASES
            # містить усі необхідні варіанти регістру або PATTERN1 дуже специфічний.
            src_text = table.PATTERN1.sub(lambda x: table.SPECIAL_CASES[x.group()], src_text)

        # Правила для перших літер слів (наприклад, "Є" -> "Ye" на початку слова)
        if hasattr(table, "PATTERN2") and hasattr(table, "FIRST_CHARACTERS"):
            # Аналогічно, покладається на структуру FIRST_CHARACTERS та PATTERN2
            src_text = table.PATTERN2.sub(lambda x: table.FIRST_CHARACTERS[x.group()], src_text)

        # Основна транслітерація по символах
        if hasattr(table, "MAIN_TRANSLIT_TABLE"):
            res = src_text.translate(table.MAIN_TRANSLIT_TABLE)
        else:
            # Якщо немає MAIN_TRANSLIT_TABLE, повертаємо текст після попередніх обробок
            res = src_text
            # Або можна викликати помилку, якщо MAIN_TRANSLIT_TABLE є обов'язковим
            # raise AttributeError("Transliteration table does not have MAIN_TRANSLIT_TABLE defined.")

        # Обробка регістру для Кир->Лат
        # Якщо оригінальний рядок був повністю у верхньому регістрі і preserve_case=True,
        # результат також перетворюється на верхній регістр.
        # Це дозволяє "ЗГУРОВСЬКИЙ" -> "ZGHUROVSKYI" (якщо preserve_case=True)
        # та "ЗГУРОВСЬКИЙ" -> "ZGhUROVSKYI" (якщо preserve_case=False, і таблиця дає ZGh для ЗГ)
        if original_src_for_case.isupper() and preserve_case:
            return res.upper()
        else:
            return res

    # Резервний варіант, якщо тип таблиці не визначено (не повинен спрацьовувати)
    # return src_text # Або викликати помилку


# For backward compatibility
translitua = translit

__all__ = [
    "translit",
    "translitua",
    "UkrainianKMU",
    "UkrainianSimple",
    "UkrainianWWS",
    "RussianGOST2006",
    "RussianSimple",
    "ALL_RUSSIAN",
    "ALL_UKRAINIAN",
    "UkrainianBritish",
    "UkrainianBGN",
    "UkrainianISO9",
    "UkrainianFrench",
    "UkrainianGerman",
    "UkrainianGOST1971",
    "UkrainianGOST1986",
    "UkrainianPassport2007",
    "UkrainianNational1996",
    "UkrainianPassport2004Alt",
    "RussianICAO",
    "ALL_TRANSLITERATIONS",
    "RussianTelegram",
    "RussianInternationalPassport1997",
    "RussianDriverLicense",
    "RussianInternationalPassport1997Reduced",
    "RussianInternationalPassport",
    "RussianISO9SystemB",
    "RussianISO9SystemA",
    "RussianISOR9Table2",
    "Lat2UkrKMU",
    "Lat2UkrSimple",
    "Lat2UkrWWS",
    "Lat2RuSimple",
    "Lat2RuISO9SystemB",
    "ALL_LATIN_TO_RUSSIAN",
]

if __name__ == "__main__":
    import doctest

    doctest.testmod()
