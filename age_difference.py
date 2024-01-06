def age_difference(ages):
    if not ages:
        return 0
    max_age = max(ages)
    min_age = min(ages)
    
    subtract_age = max_age - min_age
    return subtract_age

user_input = input("請輸入家庭成員年紀：（空格分開）")

user_list = list(map(int,user_input.split()))

result = age_difference(user_list)
print("最年長跟最年輕的年齡差：",result)
