# 1004. Maximum Number of Consecutive Ones
# Given a binary array nums and an integer k, 
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # We wont literally flip the numbers but just keep the count of it
        # We will use two pointers for the window and slide it for finding the maximum subarray.
        # We will only check when the flip_count is more than the k.
            # When the flip count is more than k
            # we will increase the left pointer
         

        n = len(nums)
        left = 0               
        flip_count = 0         
        longest = 0           

        for right in range(n):  
            if nums[right] == 0:
                flip_count += 1   

            while flip_count > k:
                if nums[left] == 0:
                    flip_count -= 1   
                left += 1  # Slide the window

            longest = max(longest, right - left + 1)

        return longest

s = Solution()
print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
