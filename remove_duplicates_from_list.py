def distinct(seq):
    arr_set = set()
    result = []
    for arr in seq:
        if arr not in arr_set:
            arr_set.add(arr)
            result.append(arr)
    return result
            
            
    