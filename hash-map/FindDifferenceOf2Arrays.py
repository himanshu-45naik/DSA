# 2215. Find The Difference of 2 Arrays

# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        # answer[0] => in nums1 but not in nums2
        # answer[1] => in nums2 but not in nums1

        res = [[0]]  * 2 
        
        nums1 = set(nums1)
        nums2 = set(nums2)

        diff1 = nums1 - nums2
        diff2 = nums2 - nums1

        res[0] = list(diff1)
        res[1] =list(diff2)

        return res
        
        
s = Solution()
print(s.findDifference([1,2,3], [1,2,3]))
print(s.findDifference([1,2,3,3], [1,1,2,2]))