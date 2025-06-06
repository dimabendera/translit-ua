# translit-ua

[Версія українською](README.ua.md)


Transliteration (romanization, latinization) for Ukrainian and russian languages with various transliteration tables (including official ones).
Translit-ua has 13 transliteration tables for the Ukrainian language:

- UkrainianKMU (National 2010, most recent one approved by The Cabinet)
- UkrainianSimple (Simple one)
- UkrainianWWS (WWS or Woodrow Wilson School or Scholarly)
- UkrainianBritish (British Standard)
- UkrainianBGN (BGN/PGGN 1965 System, United States Board on Geographic Names/Permanent Committee on Geographical Names)
- UkrainianISO9 (ISO 9, from International Organization for Standardization)
- UkrainianFrench (Jean Girodet (1976), Dictionnaire de la langue française)
- UkrainianGerman ((2000) Duden, v 22, Mannheim: Dudenverlag.)
- UkrainianGOST1971 (The Soviet Union's GOST from 1971)
- UkrainianGOST1986 (The Soviet Union's GOST from 1986)
- UkrainianPassport2007 (Used in Ukrainian passport in 2007-2010)
- UkrainianNational1996 (Codified by Committee on Issues of Legal Terminology in 1996)
- UkrainianPassport2004Alt (Yet another alternative that was sometimes used in Ukrainian passports in 2004-2007)

Translit-ua also has 10 transliteration tables for the russian language:

- RussianGOST2006 (The Russian Federation's GOST from 2006)
- RussianSimple (Simple one)
- RussianICAO (DOC9303 from ICAO, International Civil Aviation Organization)
- RussianTelegram (Russian standard for international telegrams from 2001)
- RussianInternationalPassport1997 (One that was used for international passports 1997-2010)
- RussianInternationalPassport1997Reduced (Same as above but with reduction of yy to y)
- RussianDriverLicense (One that has been used for driver licenses since 2000)
- RussianISOR9Table2 (ISO/R 9 (1968), table 2)
- RussianISO9SystemA (ISO 9:1995, System A, one with diacritics)
- RussianISO9SystemB (ISO 9:1995, System B, no diacritics)


Translit-ua can also transliterate *from* Latin back to Cyrillic.  For
Ukrainian there are tables `Lat2UkrKMU`, `Lat2UkrSimple` and
`Lat2UkrWWS`, while for Russian there are `Lat2RuSimple` and
`Lat2RuISO9SystemB`.  They are grouped in
`ALL_LATIN_TO_UKRAINIAN` and `ALL_LATIN_TO_RUSSIAN` respectively.


The minor difference in those tables is that the common apostrophe sign ' is used in every table.

For convenience, all Ukrainian tables are listed in ALL_UKRAINIAN variable, and all russian tables are listed in ALL_RUSSIAN variable. In ALL_TRANSLITERATIONS variable, you might find the complete list of tables.

Translit-ua works with python 2.6+ and python 3+ and has good doctests coverage.

## Installation

Install the latest version directly from GitHub:

```bash
$ pip install git+https://github.com/dimabendera/translit-ua.git
```

You can also install the library from PyPI as usual:

```bash
$ pip install translitua
```

## Usage

```python

    >>> from translitua import translit, RussianSimple

    >>> translit(
        u"""Берег моря. Чути розбещенi крики морських птахiв, ревiння моржа,
    а також iншi звуки, iздаваємиє різною морською сволотою. Входить Гамлєт,
    вдягнутий в зручну приємну товстовку і такі ж самі парусинові штани.
    Гамлєт красиво підперезаний вузеньким шкіряним пояском.
    Він босий, бородатий і пацаватий. В руках у нього дебелий дрючок.
    """)
    u'Bereh moria. Chuty rozbeshcheni kryky morskykh ptakhiv, revinnia morzha,\na takozh inshi zvuky, izdavaiemyie riznoiu morskoiu svolotoiu. Vkhodyt Hamliet,\nvdiahnutyi v zruchnu pryiemnu tovstovku i taki zh sami parusynovi shtany.\nHamliet krasyvo pidperezanyi vuzenkym shkirianym poiaskom.\nVin bosyi, borodatyi i patsavatyi. V rukakh u noho debelyi driuchok.\n'

    >>> translit(
        u"""Не выходи из комнаты, не совершай ошибку.
    Зачем тебе Солнце, если ты куришь Шипку?
    За дверью бессмысленно все, особенно - возглас счастья.
    Только в уборную - и сразу же возвращайся.""", RussianSimple
    )
    u"Ne vyhodi iz komnaty, ne sovershaj oshibku.\nZachem tebe Solntse, esli ty kurish' Shipku?\nZa dver'ju bessmyslenno vse, osobenno - vozglas schast'ja.\nTol'ko v ubornuju - i srazu zhe vozvraschajsja."

    >>> from translitua import Lat2UkrKMU
    >>> translit("Kharkiv", Lat2UkrKMU)
    'Харків'

    >>> from translitua import Lat2RuSimple
    >>> translit("SCHUKA", Lat2RuSimple)
    'ЩУКА'

    >>> translit("ЗГУРОВСЬКИЙ", preserve_case=False)
    'ZGhUROVSKYI'
```

More about [Ukrainian transliteration](https://en.wikipedia.org/wiki/Romanization_of_Ukrainian)

More about [Russian transliteration](https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9)
