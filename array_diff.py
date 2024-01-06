def array_diff(a, b):
    return [x for x in a if x not in b]

first_input = (input("請輸入一列數字：（空格分開）"))
second_input =(input("請輸入一列數字：（空格分開）"))

a = list(map(int,first_input.split()))
b = list(map(int,second_input.split()))

result = array_diff(a,b)
print("差異",result)