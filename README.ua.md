# translit-ua

Цей проект надає офіційну транслітерацію для української та російської мов. Він містить різні таблиці транслітерації (включно з офіційними).

## Таблиці транслітерації української мови

- UkrainianKMU (Національна 2010, чинна постанова Кабміну)
- UkrainianSimple (спрощена)
- UkrainianWWS (Woodrow Wilson School)
- UkrainianBritish (британський стандарт)
- UkrainianBGN (BGN/PGGN 1965)
- UkrainianISO9 (ISO 9)
- UkrainianFrench (Jean Girodet, 1976)
- UkrainianGerman (Duden, 2000)
- UkrainianGOST1971 (ГОСТ СРСР 1971)
- UkrainianGOST1986 (ГОСТ СРСР 1986)
- UkrainianPassport2007 (паспорт 2007–2010 рр.)
- UkrainianNational1996 (Комітет з питань правничої термінології, 1996)
- UkrainianPassport2004Alt (альтернативна таблиця 2004–2007 рр.)

## Таблиці транслітерації російської мови

- RussianGOST2006 (ГОСТ РФ 2006)
- RussianSimple (спрощена)
- RussianICAO (ICAO DOC9303)
- RussianTelegram (телеграми 2001)
- RussianInternationalPassport1997 (міжнародний паспорт 1997–2010)
- RussianInternationalPassport1997Reduced (те ж, з редукцією yy → y)
- RussianDriverLicense (водійські посвідчення від 2000 р.)
- RussianISOR9Table2 (ISO/R 9 (1968), таблиця 2)
- RussianISO9SystemA (ISO 9:1995, система A)
- RussianISO9SystemB (ISO 9:1995, система B)


Крім таблиць для транслітерації з кирилиці у латиницю, пакет також надає
конфігурації для зворотного напрямку. Для української це
`Lat2UkrKMU`, `Lat2UkrSimple` та `Lat2UkrWWS`, а для російської —
`Lat2RuSimple` і `Lat2RuISO9SystemB`. Вони згруповані у списках
`ALL_LATIN_TO_UKRAINIAN` та `ALL_LATIN_TO_RUSSIAN`.

Можна використовувати всі таблиці з `ALL_UKRAINIAN`, `ALL_RUSSIAN` та `ALL_TRANSLITERATIONS`.

## Встановлення

Встановити останню версію можна безпосередньо з GitHub:

```bash
pip install git+https://github.com/dimabendera/translit-ua.git
```

Або встановіть версію з PyPI:

```bash
pip install translitua
```

## Приклади використання

```python
from translitua import translit, UkrainianKMU, Lat2UkrKMU

print(translit("Дмитро Згуровський", UkrainianKMU))
# Dmytro Zghurovskyi

print(translit("Kharkiv", Lat2UkrKMU))
# Харків
```

Більше інформації про [українську транслітерацію](https://uk.wikipedia.org/wiki/%D0%A0%D0%BE%D0%BC%D0%B0%D0%BD%D1%96%D0%B7%D0%B0%D1%86%D1%96%D1%8F_%D1%83%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D0%BE%D1%97_%D0%BC%D0%BE%D0%B2%D0%B8)
і [російську транслітерацію](https://uk.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D1%96%D1%82%D0%B5%D1%80%D0%B0%D1%86%D1%96%D1%8F_%D1%80%D0%BE%D1%81%D1%96%D0%B9%D1%81%D1%8C%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D1%96%D1%82%D1%83_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D1%8E).
