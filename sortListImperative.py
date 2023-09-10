
def sort_list_imperative (numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
nums = [45, 433, 4, 211, 10]
sort_list_imperative(nums)
print(nums)