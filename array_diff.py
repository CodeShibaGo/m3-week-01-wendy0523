def array_diff(a, b):
    arr = []
    for x in a :
        if x not in b:
            arr.append(x)
    return arr