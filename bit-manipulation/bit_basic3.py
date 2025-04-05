class Solution:
    def countSetbits(self, n: int):
        # Approach
        # Find binary from the decimal number
        # If the bit is set increase count otherwise not.
        
        cnt = 0
        
        while n > 1:
            if (n % 2) == 1:
                cnt +=1
            
            n = n / 2
        if (n % 2) == 1:
            cnt+=1
        return cnt
    
s = Solution()
print(s.countSetbits(13))
print(s.countSetbits(1))