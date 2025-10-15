from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        stk = []        
        nums.sort()  # Sort the array to handle duplicates
        
        
        def backtrack(start, stk):
            res.append(stk.copy())  # Append a copy of the current subset
            for i in range(start, len(nums)):
                # Skip duplicates in the same level
                if i > start and nums[i] == nums[i-1]:
                    continue
                stk.append(nums[i])
                backtrack(i + 1, stk)  # Move to the next index to avoid reusing elements
                stk.pop()
        
        backtrack(0, stk)
        return res
    
s = Solution()
nums = [1,2,2]
print(s.subsetsWithDup(nums))