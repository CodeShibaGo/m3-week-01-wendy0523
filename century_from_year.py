def century(year):
    ad = year % 100
    if(ad > 0):
        return year // 100 + 1
    return year // 100