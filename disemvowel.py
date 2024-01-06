def disemvowel(s):
    return s.translate(str.maketrans("","","aeiou"))

#string.translate(table)可以指定字串中的每個字元替換,刪除,或新增
#string.maketrans(x[,y[,z]])


string = "appleisgoodtoyou" 
del_string = disemvowel(string)
print(del_string)

# delete = "aeiou"
# delete_string = "".join(x for x in string if x not in delete)
# print(delete_string)
#列表推導式 
#[x for x in iterable if expression]