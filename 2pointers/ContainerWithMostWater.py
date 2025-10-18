# 11. Container With Most Water.

# you are given an integer array height of length n
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.

class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        # Bruteforce Approach
        # Check for all walls, to built an intuition.
        # contained = 0
        # n = len(height)

        # for i in range (n):
        #     for j in range(i + 1, n):
        #         smaller_wall = min(height[i], height[j])
        #         contained = max(contained, (j - i) * smaller_wall) 

        # return contained
        # --------------------------------------------------------------------------- #

        # Optimized
        # Using two pointer solution for getting O(n) time complexity.
        
        contained = 0
        l , r = 0, len(height) - 1

        while l < r:
            smaller_wall = min(height[l], height[r])
            contained = max(contained, (r - l) * smaller_wall)  
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return contained

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))    
print(s.maxArea([1,1]))