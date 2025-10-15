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
        
        # Approach -
        # Hypothetically double the array.
        # Start from the last element (from right to left) of the hypothetical array.
        # If array is [2,1,3,4,3] than the hypothetical array would be [2,1,3,4,3,2,1,3,4,3]
        # Start from index 9 i.e 3
        # Create an empty monotonic stack. As we have to find the NGE of the actual array, 
        # We will only add the intial hypothetical elements in the stack such that the top element is larger, if not than pop the elements.
        # After the traversal of the hypothetical elements, we will find NGE of the elements of the actual array w.r.t the monotonic stack.
        # Calculate index of the hypothetical element --> ind = i % n. (n = length of array) 
        
        n = len(nums)
        nge = [-1] * n
        stk = []
        
        for i in range(2*n-1, -1, -1):
            ind = i % n
            while stk and stk[-1] <= nums[ind]:
                {
                    stk.pop()
                }
            if (i < n):
                nge[i] = -1 if not stk else stk[-1]
                
            stk.append(nums[ind])
            
        return nge
    
s = Solution()
print(s.nextGreaterElements([2,10,12,11,5,7]))