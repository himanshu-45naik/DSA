from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        step1 = Create a hashmap which creates a has of nums1 element with its index
                nums1(ele):nums1(index).
                Create an empty stack.
                Create an result list of size equal to nums1.
        step2 = Traverse through the nums2.
                2.1 Check if the current value is greater than top element of the stack.
                    If true, than pop the top element and append the current value to result.
                2.2 If the current element is present in the nums1, than append current value 
                    to stack
        step3 = Return the result list
        """

        nums1_ind = {n:i for i,n in enumerate(nums1)}
        res = [-1] * len(nums1)
        stk = []

        for i in range(len(nums2)):
            curr = nums2[i]
            while stk and curr > stk[-1]:  ## stk[-1] == stk[top]
                val = stk.pop()
                ind = nums1_ind[val]
                res[ind] = curr
            if curr in nums1:
                stk.append(curr)
        
        return res
    
s1 = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(s1.nextGreaterElement(nums1,nums2))