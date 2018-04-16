def even_filter(nums):
    return filter(lambda num: num % 2 == 0, nums)

def multiply_by_three(nums):
    return map(lambda num: num * 3, nums)

def convert_to_strings(nums):
    return map(lambda num: "The number is %s" % num, nums )

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pipeline = convert_to_strings(multiply_by_three(even_filter(nums)))

for num in pipeline:
    print num


