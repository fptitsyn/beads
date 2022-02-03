def correct(seq, rules, size):
    if len(seq) != size:
        return False
    for ch, rule in zip(seq, rules):
        if ch in ["А", "Е"]:
            rules[1] = "БВГ"
        if ch not in rule:
            return False

    return seq[-1] not in seq[:-1]


if __name__ == "__main__":
    for s in ("АЕБ", "ГВА", "ГЕБ", "БАВ"):
        if correct(s, ["АГЕ", "Е", "АБВ"], 3):
            print(f"{s} is correct")
        else:
            print(f"{s} is not correct")
