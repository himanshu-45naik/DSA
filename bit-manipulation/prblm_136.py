# SIngle number

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """A list is given, we have to return the number which appears only once.

        Args:
            nums (list[int]): The list of integers.

        Returns:
            int: The integer which appears once.
        """
        
        # We know that the XOR of same numbers is zero.
        # If we do XOR of all the numbers in the list, we will get the single number as the answer.
        
        n = len(nums)
        ans = 0
        for i in range(0,n):
            ans = ans ^ nums[i]
        return ans
    
s = Solution()
print(s.singleNumber([4,2,2,1,1]))