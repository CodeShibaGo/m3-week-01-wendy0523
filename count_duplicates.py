def count_duplicates(text):
    string = text.lower()
    result = 0
    for x in set(text):
        if string.count(x)>1:
            result += 1
    return result
