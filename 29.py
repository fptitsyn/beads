def correct(seq, rules, size):
    if len(seq) != size:
        return False
    for ch, rule in zip(seq, rules):
        if ch[0] in ["C", "D", "G"]:
            rules[1] = "AE"
        if ch not in rule:
            return False

    return seq[-1] not in seq[:-1]


if __name__ == "__main__":
    for s in ("GCDA", "CEBA", "DADE", "EBAA"):
        if correct(s, ["CDEG", "BCDG", "ABEG", "AE"], 4):
            print(f"{s} is correct")
        else:
            print(f"{s} is not correct")