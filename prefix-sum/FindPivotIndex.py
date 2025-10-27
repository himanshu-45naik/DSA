# 724. Find pivot index.
# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index,
#  where the sum of all the numbers strictly to the left of the index is 
# equal to the sum of all the numbers strictly to the index's right.


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:
                return i

            left_sum += nums[i]

        return -1
    
s = Solution()
print(s.pivotIndex([1,7,3,6,5,6]))
print(s.pivotIndex([1,2,3]))