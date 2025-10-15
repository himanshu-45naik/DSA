# 231. Power of Two

# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        # Approach
        # If a number has only 1 set bit than it is power of n.
        # Otherwise its not
        # If we do n&(n-1), than n-1 results to flipping of only set bit present to unset.
        # And if n&(n-1) is zero than n is the power of 2
        # Otherwise its not. 
        return n & (n-1) == 0

s = Solution()
print(s.isPowerOfTwo(16))
print(s.isPowerOfTwo(13))