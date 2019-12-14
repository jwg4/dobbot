def sets_to_play(first, second):
    s1 = set(first)
    s2 = set(second)

    common = s1 & s2

    if len(common) == 1:
        return common[0]
    else:
        if common:
            raise Exception("More than one common element.")
        else:
            raise Exception("No common element.")
