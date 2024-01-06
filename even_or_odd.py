def even_or_odd(number):
    if number % 2 == 0:
        return "{0}是Even ".format(number)
    else:
        return "{0}是Odd ".format(number)
    
user_input = int(input("請輸入一個整數："))
result_input = even_or_odd (user_input)
print(result_input)


