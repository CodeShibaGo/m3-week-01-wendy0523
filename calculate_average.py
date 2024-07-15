def calculate_average(nums):
    sum = 0
    len_nums = len(nums)
    for x in nums:
        sum += x
        result = sum / len_nums
    return result