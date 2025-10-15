## Minimum bit flips to convert number

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        """Number is converted from x to y.
        We have to find number of bits flipped during conversion.

        Args:
            start (int): The initial number.
            goal (int): The converted number.

        Returns:
            int: Number of bits flipped.
        """
        # If given number is 10 --> 1010
        # The converted number is 7 --> 0111
        # The no. of flipped bits are --> 3
        
        # Approach
        # First do bitwise XOR operator of start and goal such that,
        # we get ans which has bit 1s at position where the bit flipped.
        # We can use bitwise & such that by doing (ans & (1<<i)) 
        # we can determine if a given bit at that position is set or not.
        # If the result is non-zero than it is set else not set. 
        
        ans = start ^ goal
        cnt = 0
        
        for i in range(0,31):
            if (ans & (1 << i)):
                cnt+=1
                
        return cnt
    
s = Solution()
start = int(input())
goal = int(input())
print(s.minBitFlips(start, goal))
