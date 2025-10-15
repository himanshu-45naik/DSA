# 334. Increasing Triplet Subsequence

# Given an integer array nums, 
# return true if there exists a triple of indices 
# (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        # Triplets be such that 
        # the index is i<j<k and nums has nums[i]<nums[j]<nums[k]

        # Solution -
        # Check each if the condition holds then flag is True else False
        # Use a loop
         ## Can we cut off the loop early? 
            # --> By returning True when the cnt reaches 3
        # The index do not necessarily need to be contagious 
        # So use last maximum number to compare with all the elements ahead.

        n = len(nums)

        # first -> smallest so far
        # second -> middle value after finding a smaller first
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False
    
s = Solution()
print(s.increasingTriplet([1,2,3,4,5]))