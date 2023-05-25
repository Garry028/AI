# 5,3,8,6,7,2  find the min value and swap with first element
# 2,3,8,6,7,5  find the min value and swap with second element
# 2,3,5,6,7,8  find the min value and swap with third element
# Advantage of this sort is that we're not doing swapping multiple time
# we're doing swapping only once in each iteration
# Time complexity is O(n^2)
# Space complexity is O(1)

def sort(nums):
    for i in range(len(nums)-1):
        minpos = i
        for j in range(i,len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        print(f"Iteration:{i}-->",nums)

nums = [5,3,8,6,7,9,1,2]
sort(nums)