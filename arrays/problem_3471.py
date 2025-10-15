# Find largest among missing integer.


class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        """Array nums is given , int k is given
        We have to find integer k, which is largest such that it appears in less number of subarrays of size k as compared to other integers.

        Args:
            nums (list[int]): The list of integers.
            k (int): The size of subarrays.

        Returns:
            int: The largest number which appears least number of times in subarrays,
        """
        
        # Generate all subarrays and check how many times a integer is found
        # Store count of each intger in a hash.
        # Return the largest number which has appeared only once i.e almost missing.
        
        # Edge cases --
        # 1. if there are no elements in nums or the k is more than length of nums than return -1.
        # 2. We dont need to count an integer x more than once if it appears more than one time in an subarray (Use set).
        # 3. if the unique number of elements in the nums is 1 and k is also 1 than return -1.
        # 4. If all numbers appear the same number of times, we should return -1.
        if not nums or k > len(nums):
            return -1
        

        hash_count = {x: 0 for x in nums}
        n = len(nums)

       
        for i in range(n - k + 1):
            unique_numbers = set(nums[i:i + k])  
            for num in unique_numbers:
                hash_count[num] += 1

        result = -1
        for num, count in hash_count.items():
            if count == 1 and num > result: ## Almost missing
                result = num
        return result
                
                
s = Solution()
s.largestInteger([0,0], 1)
