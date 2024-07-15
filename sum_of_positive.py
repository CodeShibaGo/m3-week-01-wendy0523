def positive_sum(arr):
    sum = 0
    if len(arr) == 0:
        return sum 
    for x in arr:
        if x > 0:
            sum += x
    return sum