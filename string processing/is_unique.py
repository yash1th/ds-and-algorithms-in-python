def is_unique(s):
    setS = set()
    for i in s:
        if i.isspace():
            continue
        if i.lower() in setS:
            return False
        else:
            setS.add(i.lower())
    return True