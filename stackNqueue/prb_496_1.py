# The next greater element of some element x in an array is the first greater element 
# that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2,
# where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] 
# and determine the next greater element of nums2[j] in nums2. 
# If there is no next greater element, 
# then the answer for this query is -1

# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Find next greater element with respect to element nums1[i] in nums2.

        Args:
            nums1 (List[int]): The subset of nums2 such that next greater element is found in nums2 
                with respect to the element in nums1.
            nums2 (List[int]): The list in which the next greater element is found with respect to the nums1[i] element.

        Returns:
            List[int]: Result consisting of next greater elements.
        """
        
        result = []
        n1 = len(nums1)
        n2 = len(nums2)
        
        for i in range(n1):
            pov = nums1[i]  # Element from nums1
            n_greater = -1  # Default value if no next greater element is found
            found_pov = False
            
            for j in range(n2):
                if found_pov and nums2[j] > pov:
                    n_greater = nums2[j]
                    break
                if nums2[j] == pov:
                    found_pov = True
                    
            result.append(n_greater)
            
        return result
    
    
s1 = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(s1.nextGreaterElement(nums1,nums2))
 