def field(lst: list, *keys):
    l: list = []
    if len(keys) == 1:
        for i in lst:
            a = i.get(keys[0])
            if a is not None:
                l.append(a)

    elif len(keys) > 1:
        d: dict = {}
        for i in lst:
            for j in keys:
                a = i.get(j)
                if a is not None:
                    d[j] = a

            if d:
                l.append(d.copy())
                d.clear()

    return l



