def unique_in_order(iterable):
    if not iterable:
        return []
    result = [iterable[0]]
    
    for x in range(1,len(iterable)):
        if iterable[x] != result[-1]:
            result.append(iterable[x])
    return result