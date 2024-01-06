def find_smallest_int(arr):
    return min (arr)
user_input = input("輸入整數陣列：（空格分開）")
user_list = list(map(int,user_input.split()))

result = find_smallest_int(user_list)
print("最小值：",result)
