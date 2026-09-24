def twoSum(nums, target):
    seen = {} # initially it is empty then it will be filled with array elements 
    for i, num in enumerate(nums): # i is index and num is the element  
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

arr =  [1,2,3,4,55,6,9]
target = 5
result = two_sum(arr,target)
