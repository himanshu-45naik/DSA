# 1493. Longest Subarray of 1's after deleteing one element
# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. 
# Return 0 if there is no such subarray.

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        # We can remove element from the subarray to find the largest contigous 1's
        # We will use a sliding window approach
        # Using this approach, there will be two pointers.
            ## Left pointer and right pointer
            ## Lets say we have the example - [0,1,1,1,0,1,1,0,1]
            ## r = 0, nums[r] = 0, remove = 1, local_length = 0, max_length = 0, l = 0
            ## r = 1, nums[r] = 1, remove = 1, local_length = 1, max_length = 1, l = 0
            ## r = 2, nums[r] = 1, remove = 1, local_lenght = 2, max_length = 2, l = 0
            ## r = 3, nums[r] = 1, remove = 1, local_length = 3, max_length = 3, l = 0
            ## r = 4, nums[r] = 0, remove = 2, local_length = 3, max_length = 3, l = 1 
            ## .....using a while loop we will increase the l pointer when remove > 1
            ## continue same

        if not nums:
            return 0
         
        remove = 0
        max_length = 0
        n = len(nums)
        l = 0

        for r in range(0, n):
            if nums[r] == 0:
                remove += 1
            
            while remove > 1:
                if nums[l] == 0:
                    remove-=1
                l+=1
            
            max_length = max(max_length, r - l + 1)

        return max_length - 1  # One element has to be deleted

s = Solution()
print(s.longestSubarray([0,1,1,1,0,1,1,0,1]))
print(s.longestSubarray([1,1,0,1]))
print(s.longestSubarray([1,1,1]))