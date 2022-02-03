def correct(seq, rules, size):
    if len(seq) != size:
        return False
    for ch, rule in zip(seq, rules):
        if ch[0] in ["M", "N", "P"]:
            rules[2] = "MNP"
        if ch not in rule:
            return False

    return seq[-1] not in seq[:-1]


if __name__ == "__main__":
    for s in ("NPO", "MUN", "ONP", "NON"):
        if correct(s, ["MNO", "NOP", "OU"], 3):
            print(f"{s} is correct")
        else:
            print(f"{s} is not correct")
