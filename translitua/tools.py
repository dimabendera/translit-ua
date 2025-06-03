def add_uppercase(table):
    """
    Extend the table with uppercase options

    >>> print("а" in add_uppercase({"а": "a"}))
    True
    >>> print(add_uppercase({"а": "a"})["а"] == "a")
    True
    >>> print("А" in add_uppercase({"а": "a"}))
    True
    >>> print(add_uppercase({"а": "a"})["А"] == "A")
    True
    >>> print(len(add_uppercase({"а": "a"}).keys()))
    2
    >>> print("Аа" in add_uppercase({"аа": "aa"}))
    True
    >>> print(add_uppercase({"аа": "aa"})["Аа"] == "Aa")
    True
    """
    out = table.copy()
    # Do not overwrite existing keys: custom mappings for uppercase may be
    # defined explicitly in the source table (e.g. "ЗГ" -> "ZGh").  When we
    # generate capitalised/upper variants we ensure we only add them if they are
    # missing so that such explicit definitions are preserved.
    for k, v in table.items():
        cap_key, cap_val = k.capitalize(), v.capitalize()
        if cap_key not in out:
            out[cap_key] = cap_val

        upper_key, upper_val = k.upper(), v.upper()
        if upper_key not in out:
            out[upper_key] = upper_val

    return out


def convert_table(table):
    """
    >>> print(1072 in convert_table({"а": "a"}))
    True
    >>> print(1073 in convert_table({"а": "a"}))
    False
    >>> print(convert_table({"а": "a"})[1072] == "a")
    True
    >>> print(len(convert_table({"а": "a"}).keys()) == 1)
    True
    """

    return {ord(k): v for k, v in table.items()}