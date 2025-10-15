# 503. Next greater element - II

class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        """We have to find immediate next greater element of each element in an array.
        Here the array is circular i.e we can traverse the array again to find the next greater of the given element.

        Args:
            nums (list[int]): List of integers.

        Returns:
            list[int]: List of next greater element.
        """
        
        # Consider the array as a circular array.
        # We will have to check to the left side of element if the NGE is not present to the right.
        # Calculate index to the left by using ind = j % n.
        
        n = len(nums)
        res = [-1] * n
        for i in range(0,n):
            for j in range(i+1, i+n):
                ind = j % n
                if nums[ind] > nums[i]:
                    res[i] = nums[ind]
                    break
        return res 

        
        # T