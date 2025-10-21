# 27. Remove Element
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Using two pointers
        # One on the left and one of the right
        # Use the left pointer to check the element with the value and increase l accordinly.
        # Use the right pointer to swap the elements
        # Shrink r after swapping.

        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1  
            else:
                l += 1  
        
        return l  

s = Solution()
print(s.removeElement([3,2,2,3], 3))