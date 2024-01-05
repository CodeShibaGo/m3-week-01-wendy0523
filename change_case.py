def change_case(input_str, case):
    if case == "upper":
        return input_str.upper()
    elif case == "lower":
        return input_str.lower()
    else:
        return "請輸入upper或lower~"
    
user_string = input("請輸入你字串：")
change  = input("請輸入upper或lower:")

change_string = change_case(user_string , change)
print("已更改：",change_string)