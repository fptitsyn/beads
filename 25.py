def correct(seq, rules, size):
    if len(seq) != size:
        return False
    for ch, rule in zip(seq, rules):
        if ch not in rule:
            return False

    return seq[-1] not in seq[:-1]


if __name__ == "__main__":
    for s in ("ИЛХФ", "ИХЛФ", "ФИХЛ", "ИФЛХ"):
        if correct(s, ("ФИ", "ИЛ", "ХЛ", "ХФ"), 4):
            print(f"{s} is correct")
        else:
            print(f"{s} is not correct")
