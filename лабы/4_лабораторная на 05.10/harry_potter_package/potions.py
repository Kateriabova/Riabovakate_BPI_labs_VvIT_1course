def amortentia(name_1, name_2):
    half_1 = name_1[:(len(name_1) + 1) // 2]
    half_2 = name_2[(len(name_2) - 1) // 2:]
    return half_1 + half_2

def polyjuice(name_1, hair):
    if hair == 'cat':
        return "error"
    return name_1 * len(str(hair))

