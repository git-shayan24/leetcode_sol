def small_index_sum(arr):
    for i,ele in enumerate(arr):
        sum = 0
        while ele > 0: # extracts the given number
            rem = ele % 10
            sum = rem + sum
            ele = ele // 10
        if sum == i:
            return sum
    return -1
arr = [1,10,111]
result = small_index_sum(arr)
print(result)
