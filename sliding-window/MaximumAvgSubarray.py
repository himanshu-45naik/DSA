# 643. Maximum Average Subarray I
# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        # use a window of a k size
        # move the window over the array to find the contiguous subarray with maximum average subarray
        # How do we move the winodw?
            ## Compute sum for each element
            ## Increase the  pointer to slide the window.
            ## do not compute everything again instead  subtract the  previous element for the l pointer.
            ## Store the sum in a variable and keep track of avg maximum.
        n = len(nums)
        curr_sum = 0
        
        for i in range(k):
            curr_sum += nums[i]
        
        max_avg = curr_sum / k

        for i in range(k, n):
            curr_sum+=nums[i]
            curr_sum-=nums[i-k]

            avg = curr_sum / k
            max_avg = max(max_avg, avg)
        return max_avg
    
s = Solution()
print(s.findMaxAverage([1,12,-5,-6,50,3], 4))
